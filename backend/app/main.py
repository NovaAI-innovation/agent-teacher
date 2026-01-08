"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import health
from app.config import get_settings
from app.middleware import setup_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown."""
    # Startup: Initialize connections, start background tasks
    # Initialize Prefect client, RabbitMQ, Redis connections
    # Initialize agent services
    yield
    # Shutdown: Close connections, cleanup
    # Close Redis connection
    try:
        from app.utils.redis_client import close_redis_connection

        await close_redis_connection()
    except Exception:
        pass

    # Close RabbitMQ connection
    try:
        from app.utils.rabbitmq_client import close_rabbitmq_connection

        await close_rabbitmq_connection()
    except Exception:
        pass


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    # Get settings (will fail if .env not configured, which is expected)
    try:
        settings = get_settings()
        app_name = settings.app_name
    except Exception:
        # Fallback values if settings can't be loaded
        app_name = "agent-teacher"

    app = FastAPI(
        title=app_name,
        description="agent-teacher: Autonomous learning platform API",
        version="0.1.0",
        lifespan=lifespan,
    )

    return app


# Create app instance
app = create_app()

# Set up all middleware (CORS, error handlers, logging, rate limiting, security)
setup_middleware(app)

# Include API routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "agent-teacher API",
        "version": "0.1.0",
        "docs": "/docs",
    }
