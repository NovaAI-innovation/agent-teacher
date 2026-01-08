"""Configuration management using pydantic-settings."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "agent-teacher"
    environment: str = "development"
    debug: bool = False
    secret_key: str = Field(..., description="Secret key for cryptographic operations")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440

    # Database (Supabase)
    supabase_url: str = Field(..., description="Supabase project URL")
    supabase_key: str = Field(..., description="Supabase anonymous/public key")
    supabase_service_key: str = Field(..., description="Supabase service role key")
    database_url: str | None = Field(
        default=None,
        description=(
            "PostgreSQL database connection URL (for Alembic). "
            "If not provided, will be constructed from supabase_url"
        ),
    )

    # Semantic Memory (mem0)
    mem0_api_url: str = Field(default="http://localhost:8001", description="mem0 API URL")
    mem0_api_key: str = Field(..., description="mem0 API key")

    # Agent Framework (pydantic-ai)
    # pydantic-ai is model-agnostic - configure your LLM provider API keys:
    openai_api_key: str = Field(..., description="OpenAI API key (primary LLM provider)")
    anthropic_api_key: str | None = Field(default=None, description="Anthropic API key (optional)")
    gemini_api_key: str | None = Field(default=None, description="Google Gemini API key (optional)")

    # Orchestration (Prefect)
    prefect_api_url: str = Field(default="http://localhost:4200/api", description="Prefect API URL")
    prefect_api_key: str | None = Field(default=None, description="Prefect API key")

    # Message Queue & Caching
    rabbitmq_url: str = Field(
        default="amqp://guest:guest@localhost:5672/", description="RabbitMQ connection URL"
    )
    redis_url: str = Field(default="redis://localhost:6379/0", description="Redis connection URL")

    # API Gateway (Kong) - Optional
    kong_admin_url: str = Field(default="http://localhost:8001", description="Kong Admin API URL")
    kong_api_url: str = Field(default="http://localhost:8000", description="Kong API URL")

    # Frontend URLs (for CORS)
    frontend_urls: list[str] = Field(
        default=["http://localhost:3000", "http://localhost:3001"],
        description="Allowed frontend URLs for CORS",
    )

    # External APIs
    brave_search_api_key: str | None = Field(default=None, description="Brave Search API key")
    youtube_api_key: str | None = Field(default=None, description="YouTube API key")

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Global settings instance (lazy-loaded to avoid validation errors at import time)
# Access via get_settings() function instead of direct import
# settings = get_settings()  # Commented out to avoid validation errors without .env file


def get_database_url() -> str:
    """Get database URL for Alembic migrations.

    Returns the database_url if set, otherwise constructs it from supabase_url.
    """
    settings = get_settings()

    if settings.database_url:
        return settings.database_url

    # Construct from supabase_url if database_url not provided
    supabase_url = settings.supabase_url
    if supabase_url.startswith("https://"):
        project_ref = supabase_url.replace("https://", "").replace(".supabase.co", "")
        # Note: Password should be provided via environment variable DATABASE_URL
        # For Alembic, use the full connection string from Supabase dashboard
        database_url = (
            f"postgresql+psycopg2://postgres:[PASSWORD]@{project_ref}.supabase.co:5432/postgres"
        )
    else:
        # Assume it's already a connection string
        database_url = supabase_url

    return database_url
