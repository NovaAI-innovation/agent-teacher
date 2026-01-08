"""Base model with common fields for all database models."""

import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    """Base model with common fields: id, created_at, updated_at."""

    id: uuid.UUID | None = Field(
        default_factory=uuid.uuid4, primary_key=True, description="Unique identifier for the record"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime, default=datetime.utcnow, nullable=False),
        description="Timestamp when the record was created",
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(
            DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
        ),
        description="Timestamp when the record was last updated",
    )

    class Config:
        """SQLModel configuration."""

        # Enable JSON serialization for UUID
        json_encoders = {uuid.UUID: str}

    def update_timestamp(self) -> None:
        """Update the updated_at timestamp manually if needed."""
        self.updated_at = datetime.utcnow()
