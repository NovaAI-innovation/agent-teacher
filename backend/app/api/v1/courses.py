"""Course management API routes."""

import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from app.models.course import CourseStatus
from app.models.database import get_session
from app.services.course_service import CourseService

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)


@router.get("", status_code=status.HTTP_200_OK)
async def list_courses(
    topic: str | None = Query(default=None, description="Filter by topic/category"),
    status_filter: CourseStatus | None = Query(
        default=None, alias="status", description="Filter by course status"
    ),
    search: str | None = Query(default=None, description="Search in title and description"),
    skip: int = Query(default=0, ge=0, description="Number of records to skip"),
    limit: int = Query(
        default=100, ge=1, le=1000, description="Maximum number of records to return"
    ),
    session: Session = Depends(get_session),
) -> list[dict[str, Any]]:
    """
    List courses with optional filtering, searching, and pagination.

    Returns a list of courses matching the specified filters.
    Results are cached in Redis for performance.
    """
    service = CourseService(session)

    # Use search if provided, otherwise use list
    if search:
        courses = await service.search_courses(
            query=search, topic=topic, status=status_filter, skip=skip, limit=limit
        )
    else:
        courses = await service.list_courses(
            topic=topic, status=status_filter, skip=skip, limit=limit
        )

    # Convert to dict for JSON serialization
    return [course.model_dump() for course in courses]


@router.get("/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(
    course_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> dict[str, Any]:
    """
    Get a course by ID.

    Returns course details from cache if available, otherwise queries the database.
    """
    service = CourseService(session)
    course = await service.get_course_by_id(course_id)

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found",
        )

    return course.model_dump()


@router.get("/{course_id}/hierarchy", status_code=status.HTTP_200_OK)
async def get_course_hierarchy(
    course_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> dict[str, Any]:
    """
    Get a course with its full hierarchy (units and modules).

    Returns the complete course structure including all units and their modules.
    """
    service = CourseService(session)
    course = await service.get_course_hierarchy(course_id)

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found",
        )

    return course.model_dump()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_course(
    title: str,
    description: str | None = None,
    topic: str | None = None,
    status: CourseStatus = CourseStatus.DRAFT,
    session: Session = Depends(get_session),
) -> JSONResponse:
    """
    Create a new course.

    Creates a course in the catalog with the specified metadata.
    """
    service = CourseService(session)
    course = await service.create_course(
        title=title, description=description, topic=topic, status=status
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=course.model_dump(),
        headers={"Location": f"/api/v1/courses/{course.id}"},
    )


@router.put("/{course_id}", status_code=status.HTTP_200_OK)
async def update_course(
    course_id: uuid.UUID,
    title: str | None = None,
    description: str | None = None,
    topic: str | None = None,
    status: CourseStatus | None = None,
    session: Session = Depends(get_session),
) -> dict[str, Any]:
    """
    Update an existing course.

    Updates course metadata. Only provided fields will be updated.
    """
    service = CourseService(session)
    course = await service.update_course(
        course_id=course_id, title=title, description=description, topic=topic, status=status
    )

    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found",
        )

    return course.model_dump()


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(
    course_id: uuid.UUID,
    session: Session = Depends(get_session),
) -> None:
    """
    Delete a course.

    Deletes a course and all its related units and modules.
    """
    service = CourseService(session)
    deleted = await service.delete_course(course_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found",
        )
