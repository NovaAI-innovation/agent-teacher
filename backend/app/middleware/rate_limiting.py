"""Rate limiting middleware using slowapi."""

from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.config import get_settings


def get_rate_limit_key(request: Request) -> str:
    """Get rate limit key from request (IP address)."""
    return get_remote_address(request)


def setup_rate_limiting(app: FastAPI) -> None:
    """Configure rate limiting middleware."""
    try:
        settings = get_settings()
        rate_limit_per_minute = getattr(settings, "rate_limit_per_minute", 60)
    except Exception:
        rate_limit_per_minute = 60

    # Create limiter instance
    limiter = Limiter(
        key_func=get_rate_limit_key,
        default_limits=[f"{rate_limit_per_minute}/minute"],
    )

    # Store limiter in app state
    app.state.limiter = limiter

    # Register rate limit exceeded handler
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


def get_limiter(app: FastAPI) -> Limiter:
    """Get rate limiter from app state."""
    return app.state.limiter
