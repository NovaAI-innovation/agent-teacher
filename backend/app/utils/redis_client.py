"""Redis client with connection pooling."""

try:
    import redis.asyncio as redis
    from redis.asyncio.connection import ConnectionPool
except ImportError:
    # Handle case where redis is not installed
    redis = None
    ConnectionPool = None


from typing import Any

from app.config import get_settings

# Redis connection pool (lazy initialization)
redis_pool: Any | None = None
redis_client: Any | None = None


def get_redis_pool():
    """Get or create Redis connection pool."""
    global redis_pool

    if redis is None:
        raise ImportError("redis package is not installed. Install it with: uv add redis")

    if redis_pool is None:
        settings = get_settings()
        redis_pool = ConnectionPool.from_url(
            settings.redis_url,
            max_connections=50,
            decode_responses=True,
        )

    return redis_pool


def get_redis_client():
    """Get or create Redis client instance."""
    global redis_client

    if redis is None:
        raise ImportError("redis package is not installed. Install it with: uv add redis")

    if redis_client is None:
        pool = get_redis_pool()
        redis_client = redis.Redis(connection_pool=pool)

    return redis_client


async def close_redis_connection() -> None:
    """Close Redis connection pool."""
    global redis_client, redis_pool

    if redis_client:
        await redis_client.close()
        redis_client = None

    if redis_pool:
        await redis_pool.disconnect()
        redis_pool = None


# Initialize client on module import (lazy initialization)
# Connection will be established when actually used
