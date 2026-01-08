"""Health check router."""

from typing import Any

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, Any]:
    """
    Health check endpoint.

    Checks connectivity to:
    - Database (Supabase/PostgreSQL)
    - Redis
    - RabbitMQ

    Returns service status for each component.
    """
    health_status: dict[str, Any] = {
        "status": "healthy",
        "service": "backend-api",
        "database": "unknown",
        "redis": "unknown",
        "rabbitmq": "unknown",
    }

    # Check database connection
    try:
        from sqlalchemy import text

        from app.models.database import get_engine

        engine = get_engine()
        # Test connection with a simple query
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        health_status["database"] = "connected"
    except Exception as e:
        health_status["database"] = f"disconnected: {str(e)}"
        health_status["status"] = "degraded"

    # Check Redis connection
    try:
        from app.utils.redis_client import get_redis_client

        redis_client = get_redis_client()
        await redis_client.ping()
        health_status["redis"] = "connected"
    except Exception as e:
        health_status["redis"] = f"disconnected: {str(e)}"
        health_status["status"] = "degraded"

    # Check RabbitMQ connection
    try:
        from app.utils.rabbitmq_client import get_rabbitmq_connection

        connection = await get_rabbitmq_connection()
        if connection and not connection.is_closed:
            health_status["rabbitmq"] = "connected"
        else:
            health_status["rabbitmq"] = "disconnected"
            health_status["status"] = "degraded"
    except Exception as e:
        health_status["rabbitmq"] = f"disconnected: {str(e)}"
        health_status["status"] = "degraded"

    # Return appropriate status code
    if health_status["status"] == "healthy":
        return JSONResponse(content=health_status, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content=health_status, status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
