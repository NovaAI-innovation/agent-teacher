"""Course model with status management."""

from __future__ import annotations

import uuid
from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Column, Field, Relationship, Text

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.unit import Unit


class CourseStatus(str, Enum):
    """Course status enum."""

    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Course(BaseModel, table=True):
    """Course model representing a course in the catalog."""

    __tablename__ = "courses"

    title: str = Field(max_length=255, description="Course title")
    description: str | None = Field(
        default=None, sa_column=Column(Text), description="Course description"
    )
    topic: str | None = Field(default=None, max_length=100, description="Course topic/category")
    status: CourseStatus = Field(
        default=CourseStatus.DRAFT,
        description="Course status (draft, published, archived)",
    )

    # Relationships
    units: list["Unit"] = Relationship(
        back_populates="course",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )

    class Config:
        """SQLModel configuration."""

        json_encoders = {uuid.UUID: str, CourseStatus: str}
