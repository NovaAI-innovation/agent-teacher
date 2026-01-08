"""SQLModel database engine and session management."""

from collections.abc import AsyncGenerator

from sqlmodel import Session, SQLModel, create_engine

from app.config import get_settings

# Lazy initialization - engine will be created when needed
engine: object | None = None


def get_engine():
    """Get or create SQLModel engine."""
    global engine

    if engine is None:
        settings = get_settings()

        # Create database connection string from Supabase URL
        # Supabase provides PostgreSQL connection string in format:
        # postgresql://postgres:[PASSWORD]@[PROJECT_REF].supabase.co:5432/postgres
        # For now, we'll construct it from the Supabase URL
        # In production, use the direct connection string from Supabase dashboard
        # Extract project reference from Supabase URL
        supabase_url = settings.supabase_url
        if supabase_url.startswith("https://"):
            project_ref = supabase_url.replace("https://", "").replace(".supabase.co", "")
            # Note: In production, use actual password from environment or
            # Supabase connection string. For now, this is a placeholder that
            # will be configured properly.
            database_url = (
                f"postgresql+psycopg2://postgres:[PASSWORD]@"
                f"{project_ref}.supabase.co:5432/postgres"
            )
        else:
            # Assume it's already a connection string
            database_url = supabase_url

        # Create SQLModel engine
        # Use echo=True for development to see SQL queries
        engine = create_engine(
            database_url,
            echo=settings.debug,
            pool_pre_ping=True,  # Verify connections before using
            pool_size=10,
            max_overflow=20,
        )

    return engine


def get_session():
    """Get database session dependency for FastAPI."""
    db_engine = get_engine()
    with Session(db_engine) as session:
        yield session


async def get_async_session() -> AsyncGenerator[Session, None]:
    """Get async database session dependency for FastAPI."""
    # Note: SQLModel/SQLAlchemy 2.0+ supports async sessions
    # For now, using sync session with async wrapper
    db_engine = get_engine()
    with Session(db_engine) as session:
        yield session


def init_db() -> None:
    """Initialize database - create all tables."""
    db_engine = get_engine()
    SQLModel.metadata.create_all(db_engine)
