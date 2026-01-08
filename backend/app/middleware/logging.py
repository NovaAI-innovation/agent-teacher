"""Request logging middleware with correlation IDs."""

import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for request/response logging with correlation IDs."""

    async def dispatch(self, request: Request, call_next):
        """Process request and log with correlation ID."""
        # Generate correlation ID
        correlation_id = str(uuid.uuid4())
        request.state.correlation_id = correlation_id

        # Add correlation ID to logger context
        log_extra = {
            "correlation_id": correlation_id,
            "method": request.method,
            "path": request.url.path,
            "client_ip": request.client.host if request.client else None,
        }

        # Log request
        start_time = time.time()
        logger.info(f"Request: {request.method} {request.url.path}", extra=log_extra)

        # Process request
        try:
            response = await call_next(request)

            # Calculate processing time
            process_time = time.time() - start_time

            # Log response
            logger.info(
                f"Response: {request.method} {request.url.path} - {response.status_code}",
                extra={
                    **log_extra,
                    "status_code": response.status_code,
                    "process_time": process_time,
                },
            )

            # Add correlation ID to response header
            response.headers["X-Correlation-ID"] = correlation_id

            return response

        except Exception as e:
            # Log exception
            process_time = time.time() - start_time
            logger.error(
                f"Request failed: {request.method} {request.url.path} - {type(e).__name__}",
                extra={
                    **log_extra,
                    "exception_type": type(e).__name__,
                    "exception_message": str(e),
                    "process_time": process_time,
                },
                exc_info=True,
            )
            raise


def setup_logging_middleware(app) -> None:
    """Add logging middleware to FastAPI app."""
    app.add_middleware(LoggingMiddleware)
