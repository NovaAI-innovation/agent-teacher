# Story 1.9: Configure Backend Middleware and Utilities

Status: ready-for-dev

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

- [ ] Task 1: Create CORS middleware (AC: 1)
  - [ ] Create `backend/app/middleware/cors.py`
  - [ ] Import CORSMiddleware from fastapi.middleware.cors
  - [ ] Configure CORS with frontend origins from config
  - [ ] Allow appropriate methods (GET, POST, PUT, DELETE, etc.)
  - [ ] Allow appropriate headers
  - [ ] Export CORS configuration function
- [ ] Task 2: Create error handler middleware (AC: 2)
  - [ ] Create `backend/app/middleware/error_handler.py`
  - [ ] Import FastAPI exception handlers
  - [ ] Create global exception handler with standardized error response format
  - [ ] Handle common exceptions (ValidationError, HTTPException, etc.)
  - [ ] Return consistent error response structure: `{"error": {"code": "...", "message": "...", "details": {...}}}`
  - [ ] Log errors appropriately
- [ ] Task 3: Create logging middleware (AC: 3)
  - [ ] Create `backend/app/middleware/logging.py`
  - [ ] Import logging utilities
  - [ ] Create middleware to add correlation IDs to requests
  - [ ] Log request/response information
  - [ ] Use structured logging format
- [ ] Task 4: Create rate limiting middleware (AC: 4)
  - [ ] Create `backend/app/middleware/rate_limiting.py`
  - [ ] Import slowapi
  - [ ] Configure basic rate limiting structure
  - [ ] Set up rate limit rules (can be basic for now)
  - [ ] Export rate limiter instance
- [ ] Task 5: Create security headers middleware (AC: 5)
  - [ ] Create `backend/app/middleware/security.py`
  - [ ] Create middleware to add security headers
  - [ ] Add Content-Security-Policy header
  - [ ] Add X-Frame-Options header
  - [ ] Add HSTS header (if HTTPS)
  - [ ] Add other security headers as appropriate
- [ ] Task 6: Create logging utility (AC: 6)
  - [ ] Create `backend/app/utils/logger.py`
  - [ ] Configure structured logging with JSON formatter
  - [ ] Set up log levels and handlers
  - [ ] Export logger instance
- [ ] Task 7: Create custom exceptions (AC: 7)
  - [ ] Create `backend/app/utils/exceptions.py`
  - [ ] Create APIException base class with error code
  - [ ] Create ValidationError exception
  - [ ] Create NotFoundError exception
  - [ ] Add other common exceptions as needed
  - [ ] Each exception should have error code and message
- [ ] Task 8: Register all middleware in main.py (AC: 8)
  - [ ] Import all middleware modules
  - [ ] Register CORS middleware
  - [ ] Register error handlers
  - [ ] Register logging middleware
  - [ ] Register rate limiting middleware
  - [ ] Register security headers middleware
  - [ ] Verify no import errors

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

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

