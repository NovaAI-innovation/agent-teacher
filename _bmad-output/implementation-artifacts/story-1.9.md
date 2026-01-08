# Story 1.9: Configure Backend Middleware and Utilities

Status: review

## Story

As a developer,
I want middleware (CORS, error handling, logging, rate limiting, security) and core utilities,
so that the backend has proper cross-cutting concerns handled.

## Acceptance Criteria

1. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/middleware/cors.py` contains functional CORS configuration allowing frontend origins from config
2. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/middleware/error_handler.py` contains global exception handler with standardized error response format
3. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/middleware/logging.py` contains structured logging middleware with correlation IDs
4. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/middleware/rate_limiting.py` contains rate limiting middleware with slowapi (basic structure)
5. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/middleware/security.py` contains security headers middleware (Content-Security-Policy, X-Frame-Options, HSTS)
6. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/utils/logger.py` contains structured logging configuration with JSON formatter
7. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** `backend/app/utils/exceptions.py` contains custom exception classes (APIException, ValidationError, NotFoundError) with error codes
8. **Given** The FastAPI application structure exists **When** I create middleware and utility files **Then** All middleware can be imported and registered in main.py without errors

## Tasks / Subtasks

- [x] Task 1: Create CORS middleware (AC: 1)
  - [x] Create `backend/app/middleware/cors.py`
  - [x] Import CORSMiddleware from fastapi.middleware.cors
  - [x] Configure CORS with frontend origins from config
  - [x] Allow appropriate methods (GET, POST, PUT, DELETE, etc.)
  - [x] Allow appropriate headers
  - [x] Export CORS configuration function
- [x] Task 2: Create error handler middleware (AC: 2)
  - [x] Create `backend/app/middleware/error_handler.py`
  - [x] Import FastAPI exception handlers
  - [x] Create global exception handler with standardized error response format
  - [x] Handle common exceptions (ValidationError, HTTPException, etc.)
  - [x] Return consistent error response structure: `{"error": {"code": "...", "message": "...", "details": {...}}}`
  - [x] Log errors appropriately
- [x] Task 3: Create logging middleware (AC: 3)
  - [x] Create `backend/app/middleware/logging.py`
  - [x] Import logging utilities
  - [x] Create middleware to add correlation IDs to requests
  - [x] Log request/response information
  - [x] Use structured logging format
- [x] Task 4: Create rate limiting middleware (AC: 4)
  - [x] Create `backend/app/middleware/rate_limiting.py`
  - [x] Import slowapi
  - [x] Configure basic rate limiting structure
  - [x] Set up rate limit rules (can be basic for now)
  - [x] Export rate limiter instance
- [x] Task 5: Create security headers middleware (AC: 5)
  - [x] Create `backend/app/middleware/security.py`
  - [x] Create middleware to add security headers
  - [x] Add Content-Security-Policy header
  - [x] Add X-Frame-Options header
  - [x] Add HSTS header (if HTTPS)
  - [x] Add other security headers as appropriate
- [x] Task 6: Create logging utility (AC: 6)
  - [x] Create `backend/app/utils/logger.py`
  - [x] Configure structured logging with JSON formatter
  - [x] Set up log levels and handlers
  - [x] Export logger instance
- [x] Task 7: Create custom exceptions (AC: 7)
  - [x] Create `backend/app/utils/exceptions.py`
  - [x] Create APIException base class with error code
  - [x] Create ValidationError exception
  - [x] Create NotFoundError exception
  - [x] Add other common exceptions as needed
  - [x] Each exception should have error code and message
- [x] Task 8: Register all middleware in main.py (AC: 8)
  - [x] Import all middleware modules
  - [x] Register CORS middleware
  - [x] Register error handlers
  - [x] Register logging middleware
  - [x] Register rate limiting middleware
  - [x] Register security headers middleware
  - [x] Verify no import errors

## Dev Notes

- **Architecture Patterns**: Middleware pattern for cross-cutting concerns. Structured logging with correlation IDs for request tracing.
- **Source Tree Components**:
  - `backend/app/middleware/cors.py` - CORS configuration
  - `backend/app/middleware/error_handler.py` - Global exception handlers
  - `backend/app/middleware/logging.py` - Request logging middleware
  - `backend/app/middleware/rate_limiting.py` - Rate limiting middleware
  - `backend/app/middleware/security.py` - Security headers middleware
  - `backend/app/utils/logger.py` - Logging configuration
  - `backend/app/utils/exceptions.py` - Custom exception classes
- **Testing Standards**: No tests required (infrastructure setup), but middleware should be tested manually
- **Dependencies**: Story 1.7 must be complete (FastAPI app initialized), Story 1.5 must be complete (config available)
- **Middleware Order**: Register middleware in correct order (CORS first, error handlers, logging, rate limiting, security)

### Project Structure Notes

- **Alignment**: Middleware structure follows FastAPI best practices and architecture.md patterns
- **Error Handling**: Standardized error response format for consistent API responses
- **Logging**: Structured JSON logging for better log analysis and monitoring
- **Security**: Security headers follow OWASP best practices
- **No Conflicts**: Greenfield setup, no existing middleware

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Middleware] - Middleware patterns and error handling
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 8] - Task 8: Configure backend middleware and utilities
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.9] - Original story definition

## Dev Agent Record

### Agent Model Used

gpt-4o

### Debug Log References

N/A - No errors encountered during implementation

### Completion Notes List

✅ **Story 1.9 Implementation Complete**

**Summary:**
- Created all middleware files: CORS, error handler, logging, rate limiting, security
- Created utility files: logger, exceptions
- Registered all middleware in main.py via setup_middleware() function
- All middleware and utilities can be imported without errors

**Acceptance Criteria Verification:**
- ✅ AC1: `backend/app/middleware/cors.py` contains functional CORS configuration allowing frontend origins from config
- ✅ AC2: `backend/app/middleware/error_handler.py` contains global exception handler with standardized error response format
- ✅ AC3: `backend/app/middleware/logging.py` contains structured logging middleware with correlation IDs
- ✅ AC4: `backend/app/middleware/rate_limiting.py` contains rate limiting middleware with slowapi (basic structure)
- ✅ AC5: `backend/app/middleware/security.py` contains security headers middleware (Content-Security-Policy, X-Frame-Options, HSTS)
- ✅ AC6: `backend/app/utils/logger.py` contains structured logging configuration with JSON formatter
- ✅ AC7: `backend/app/utils/exceptions.py` contains custom exception classes (APIException, ValidationError, NotFoundError) with error codes
- ✅ AC8: All middleware can be imported and registered in main.py without errors

**Implementation Details:**
- **CORS Middleware (`backend/app/middleware/cors.py`):**
  - `setup_cors()` function configures CORS with frontend URLs from config
  - Allows all methods and headers for development
  - Handles missing config gracefully with fallback values

- **Error Handler Middleware (`backend/app/middleware/error_handler.py`):**
  - Global exception handlers for APIException, RequestValidationError, HTTPException, and general Exception
  - Standardized error response format: `{"error": {"code": "...", "message": "...", "details": {...}}}`
  - Error logging with correlation IDs and context

- **Logging Middleware (`backend/app/middleware/logging.py`):**
  - LoggingMiddleware class adds correlation IDs to requests
  - Logs request method, path, client IP, status code, and process time
  - Adds X-Correlation-ID header to responses
  - Structured logging with JSON format

- **Rate Limiting Middleware (`backend/app/middleware/rate_limiting.py`):**
  - Uses slowapi for rate limiting
  - Configurable rate limit per minute from config (default: 60/minute)
  - Rate limit key based on client IP address
  - Exception handler for rate limit exceeded

- **Security Headers Middleware (`backend/app/middleware/security.py`):**
  - SecurityHeadersMiddleware adds security headers to all responses
  - Content-Security-Policy, X-Frame-Options, X-Content-Type-Options
  - X-XSS-Protection, Referrer-Policy, Permissions-Policy
  - HSTS header (only in production with HTTPS)

- **Logging Utility (`backend/app/utils/logger.py`):**
  - JSONFormatter for structured JSON logging
  - setup_logger() function configures logger with JSON formatter
  - Supports correlation IDs and extra fields
  - Default logger instance exported

- **Custom Exceptions (`backend/app/utils/exceptions.py`):**
  - APIException base class with error_code, status_code, message, details
  - ValidationError (400), NotFoundError (404), AuthenticationError (401)
  - AuthorizationError (403), InternalServerError (500)
  - All exceptions follow consistent structure

- **Middleware Setup (`backend/app/middleware/__init__.py`):**
  - `setup_middleware()` function registers all middleware in correct order
  - Order: CORS → Error handlers → Logging → Rate limiting → Security
  - Centralized middleware configuration

- **Main.py Integration:**
  - Updated main.py to use `setup_middleware(app)` instead of manual CORS setup
  - All middleware registered automatically

**Testing:**
- No tests required for this infrastructure setup story (as per Dev Notes)
- Verified all middleware and utilities can be imported successfully
- Verified middleware setup function works correctly
- Verified exception classes are properly structured

### File List

- `backend/app/middleware/__init__.py` (created)
- `backend/app/middleware/cors.py` (created)
- `backend/app/middleware/error_handler.py` (created)
- `backend/app/middleware/logging.py` (created)
- `backend/app/middleware/rate_limiting.py` (created)
- `backend/app/middleware/security.py` (created)
- `backend/app/utils/logger.py` (created)
- `backend/app/utils/exceptions.py` (created)
- `backend/app/main.py` (updated to use setup_middleware)
