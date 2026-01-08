"""Unit model representing a unit within a course."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.module import Module


class Unit(BaseModel, table=True):
    """Unit model representing a unit within a course."""

    __tablename__ = "units"

    course_id: uuid.UUID = Field(foreign_key="courses.id", description="Parent course ID")
    title: str = Field(max_length=255, description="Unit title")
    order: int = Field(default=0, description="Order/sequence within course")

    # Relationships
    course: "Course" = Relationship(back_populates="units")
    modules: list["Module"] = Relationship(
        back_populates="unit",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )

    class Config:
        """SQLModel configuration."""

        json_encoders = {uuid.UUID: str}
