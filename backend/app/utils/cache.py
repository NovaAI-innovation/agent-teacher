"""Cache utility functions for Redis caching."""

import json
from typing import Any

from app.utils.redis_client import get_redis_client


class CacheUtils:
    """Utility class for cache operations."""

    def __init__(self):
        """Initialize cache utils with Redis client."""
        self.redis = get_redis_client()

    async def get(self, key: str) -> Any | None:
        """Get value from cache."""
        cached = await self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None

    async def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """Set value in cache with TTL."""
        await self.redis.setex(key, ttl, json.dumps(value, default=str))

    async def delete(self, *keys: str) -> None:
        """Delete one or more keys from cache."""
        if keys:
            await self.redis.delete(*keys)

    async def delete_pattern(self, pattern: str) -> None:
        """Delete all keys matching a pattern."""
        keys = await self.redis.keys(pattern)
        if keys:
            await self.redis.delete(*keys)

    async def exists(self, key: str) -> bool:
        """Check if a key exists in cache."""
        return bool(await self.redis.exists(key))

    async def get_many(self, keys: list[str]) -> dict[str, Any]:
        """Get multiple values from cache."""
        if not keys:
            return {}

        values = await self.redis.mget(keys)
        result = {}
        for key, value in zip(keys, values, strict=False):
            if value:
                result[key] = json.loads(value)
        return result

    async def set_many(self, mapping: dict[str, Any], ttl: int = 3600) -> None:
        """Set multiple values in cache with TTL."""
        if not mapping:
            return

        # Convert values to JSON strings
        json_mapping = {k: json.dumps(v, default=str) for k, v in mapping.items()}

        # Use pipeline for efficiency
        pipe = self.redis.pipeline()
        for key, value in json_mapping.items():
            pipe.setex(key, ttl, value)
        await pipe.execute()


# Cache key pattern builders
class CacheKeys:
    """Cache key pattern builders."""

    @staticmethod
    def course_list() -> str:
        """Get cache key for course list."""
        return "course:catalog:list"

    @staticmethod
    def course_detail(course_id: str) -> str:
        """Get cache key for course detail."""
        return f"course:catalog:{course_id}"

    @staticmethod
    def course_filter(filter_hash: str) -> str:
        """Get cache key for filtered course list."""
        return f"course:catalog:filter:{filter_hash}"

    @staticmethod
    def course_pattern() -> str:
        """Get cache key pattern for all course-related keys."""
        return "course:catalog:*"
