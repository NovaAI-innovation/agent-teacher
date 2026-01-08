"""Course catalog service with CRUD operations and caching."""

import json
import uuid
from typing import Any

from sqlmodel import Session, select
from sqlmodel.sql import Select

from app.models.course import Course, CourseStatus
from app.models.module import Module
from app.models.unit import Unit
from app.utils.redis_client import get_redis_client

# Cache TTL in seconds (1 hour)
CACHE_TTL = 3600

# Cache key patterns
CACHE_KEY_COURSE_LIST = "course:catalog:list"
CACHE_KEY_COURSE_DETAIL = "course:catalog:{course_id}"
CACHE_KEY_COURSE_FILTER = "course:catalog:filter:{filter_hash}"


class CourseService:
    """Service for managing course catalog operations."""

    def __init__(self, session: Session):
        """Initialize course service with database session."""
        self.session = session
        self.redis = get_redis_client()

    async def create_course(
        self,
        title: str,
        description: str | None = None,
        topic: str | None = None,
        status: CourseStatus = CourseStatus.DRAFT,
    ) -> Course:
        """Create a new course."""
        course = Course(
            title=title,
            description=description,
            topic=topic,
            status=status,
        )
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)

        # Invalidate cache
        await self._invalidate_course_cache()

        return course

    async def update_course(
        self,
        course_id: uuid.UUID,
        title: str | None = None,
        description: str | None = None,
        topic: str | None = None,
        status: CourseStatus | None = None,
    ) -> Course | None:
        """Update an existing course."""
        course = await self.get_course_by_id(course_id)
        if not course:
            return None

        if title is not None:
            course.title = title
        if description is not None:
            course.description = description
        if topic is not None:
            course.topic = topic
        if status is not None:
            course.status = status

        course.update_timestamp()
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)

        # Invalidate cache
        await self._invalidate_course_cache(course_id)

        return course

    async def get_course_by_id(self, course_id: uuid.UUID) -> Course | None:
        """Get a course by ID, checking cache first."""
        # Try cache first
        cache_key = CACHE_KEY_COURSE_DETAIL.format(course_id=str(course_id))
        cached = await self.redis.get(cache_key)
        if cached:
            course_data = json.loads(cached)
            return Course(**course_data)

        # Query database
        statement = select(Course).where(Course.id == course_id)
        course = self.session.exec(statement).first()

        # Cache if found
        if course:
            await self.redis.setex(
                cache_key, CACHE_TTL, json.dumps(course.model_dump(), default=str)
            )

        return course

    async def list_courses(
        self,
        topic: str | None = None,
        status: CourseStatus | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Course]:
        """List courses with optional filtering and pagination."""
        # Build filter hash for cache key
        filter_hash = self._build_filter_hash(topic=topic, status=status, skip=skip, limit=limit)
        cache_key = CACHE_KEY_COURSE_FILTER.format(filter_hash=filter_hash)

        # Try cache first
        cached = await self.redis.get(cache_key)
        if cached:
            courses_data = json.loads(cached)
            return [Course(**data) for data in courses_data]

        # Build query
        statement: Select[Course] = select(Course)

        # Apply filters
        if topic:
            statement = statement.where(Course.topic == topic)
        if status:
            statement = statement.where(Course.status == status)

        # Apply ordering and pagination
        statement = statement.order_by(Course.created_at.desc()).offset(skip).limit(limit)

        # Execute query
        courses = list(self.session.exec(statement).all())

        # Cache results
        courses_data = [course.model_dump() for course in courses]
        await self.redis.setex(cache_key, CACHE_TTL, json.dumps(courses_data, default=str))

        return courses

    async def search_courses(
        self,
        query: str,
        topic: str | None = None,
        status: CourseStatus | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> list[Course]:
        """Search courses by title or description."""
        # Build query
        statement: Select[Course] = select(Course)

        # Search in title or description
        search_pattern = f"%{query}%"
        statement = statement.where(
            (Course.title.ilike(search_pattern)) | (Course.description.ilike(search_pattern))
        )

        # Apply additional filters
        if topic:
            statement = statement.where(Course.topic == topic)
        if status:
            statement = statement.where(Course.status == status)

        # Apply ordering and pagination
        statement = statement.order_by(Course.created_at.desc()).offset(skip).limit(limit)

        # Execute query
        courses = list(self.session.exec(statement).all())

        return courses

    async def delete_course(self, course_id: uuid.UUID) -> bool:
        """Delete a course and its related units/modules."""
        course = await self.get_course_by_id(course_id)
        if not course:
            return False

        self.session.delete(course)
        self.session.commit()

        # Invalidate cache
        await self._invalidate_course_cache(course_id)

        return True

    async def get_course_hierarchy(self, course_id: uuid.UUID) -> Course | None:
        """Get a course with its full hierarchy (units and modules)."""
        course = await self.get_course_by_id(course_id)
        if not course:
            return None

        # Load units
        units_statement = select(Unit).where(Unit.course_id == course_id).order_by(Unit.order)
        units = list(self.session.exec(units_statement).all())
        course.units = units

        # Load modules for each unit
        for unit in units:
            modules_statement = (
                select(Module).where(Module.unit_id == unit.id).order_by(Module.order)
            )
            modules = list(self.session.exec(modules_statement).all())
            unit.modules = modules

        return course

    async def _invalidate_course_cache(self, course_id: uuid.UUID | None = None) -> None:
        """Invalidate course cache entries."""
        # Invalidate list cache
        await self.redis.delete(CACHE_KEY_COURSE_LIST)

        # Invalidate filter caches (delete all filter keys)
        pattern = CACHE_KEY_COURSE_FILTER.format(filter_hash="*")
        keys = await self.redis.keys(pattern)
        if keys:
            await self.redis.delete(*keys)

        # Invalidate specific course cache if provided
        if course_id:
            cache_key = CACHE_KEY_COURSE_DETAIL.format(course_id=str(course_id))
            await self.redis.delete(cache_key)

    def _build_filter_hash(self, **kwargs: Any) -> str:
        """Build a hash from filter parameters for cache key."""
        import hashlib

        filter_str = json.dumps(kwargs, sort_keys=True, default=str)
        return hashlib.md5(filter_str.encode()).hexdigest()
