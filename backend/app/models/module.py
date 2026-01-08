"""Module model representing a module within a unit."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.unit import Unit


class Module(BaseModel, table=True):
    """Module model representing a module within a unit."""

    __tablename__ = "modules"

    unit_id: uuid.UUID = Field(foreign_key="units.id", description="Parent unit ID")
    title: str = Field(max_length=255, description="Module title")
    order: int = Field(default=0, description="Order/sequence within unit")

    # Relationships
    unit: "Unit" = Relationship(back_populates="modules")

    class Config:
        """SQLModel configuration."""

        json_encoders = {uuid.UUID: str}
