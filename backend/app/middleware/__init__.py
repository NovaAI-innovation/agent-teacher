"""Middleware package."""

from app.middleware.cors import setup_cors
from app.middleware.error_handler import setup_error_handlers
from app.middleware.logging import setup_logging_middleware
from app.middleware.rate_limiting import setup_rate_limiting
from app.middleware.security import setup_security_middleware


def setup_middleware(app) -> None:
    """Set up all middleware for FastAPI app."""
    # Order matters: CORS first, then error handlers, logging, rate limiting, security
    setup_cors(app)
    setup_error_handlers(app)
    setup_logging_middleware(app)
    setup_rate_limiting(app)
    setup_security_middleware(app)
