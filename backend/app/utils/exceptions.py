"""Custom exception classes."""

from typing import Any


class APIException(Exception):
    """Base API exception with error code and message."""

    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int = 500,
        details: dict[str, Any] | None = None,
    ):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(APIException):
    """Validation error exception."""

    def __init__(
        self,
        message: str = "Validation error",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
            status_code=400,
            details=details,
        )


class NotFoundError(APIException):
    """Resource not found exception."""

    def __init__(
        self,
        message: str = "Resource not found",
        resource_type: str | None = None,
        resource_id: str | None = None,
    ):
        details = {}
        if resource_type:
            details["resource_type"] = resource_type
        if resource_id:
            details["resource_id"] = resource_id

        super().__init__(
            message=message,
            error_code="NOT_FOUND",
            status_code=404,
            details=details,
        )


class AuthenticationError(APIException):
    """Authentication error exception."""

    def __init__(
        self,
        message: str = "Authentication failed",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code="AUTHENTICATION_ERROR",
            status_code=401,
            details=details,
        )


class AuthorizationError(APIException):
    """Authorization error exception."""

    def __init__(
        self,
        message: str = "Authorization failed",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code="AUTHORIZATION_ERROR",
            status_code=403,
            details=details,
        )


class InternalServerError(APIException):
    """Internal server error exception."""

    def __init__(
        self,
        message: str = "Internal server error",
        details: dict[str, Any] | None = None,
    ):
        super().__init__(
            message=message,
            error_code="INTERNAL_SERVER_ERROR",
            status_code=500,
            details=details,
        )
