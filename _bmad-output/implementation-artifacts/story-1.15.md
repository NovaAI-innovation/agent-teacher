# Story 1.15: Set Up Frontend API Client and WebSocket Structure

Status: completed

## Story

As a developer,
I want API client configuration and WebSocket client structure,
so that the frontend can communicate with backend services.

## Acceptance Criteria

1. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** `frontend/lib/api/client.ts` contains Axios client with base URL from NEXT_PUBLIC_API_URL
2. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** API client includes request/response interceptors, error handling, and token management structure
3. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** `frontend/lib/api/endpoints.ts` contains API endpoint constants matching backend routes
4. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** Placeholder API modules exist: `auth.ts`, `courses.ts`, `learning.ts`, `assessments.ts`, `tutoring.ts`, `progress.ts`, `admin.ts`
5. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** `frontend/lib/websocket/client.ts` contains WebSocket client with connection management structure
6. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** `frontend/lib/websocket/handlers.ts` and `frontend/lib/websocket/reconnect.ts` exist with basic structure
7. **Given** Frontend dependencies are installed **When** I create API client and WebSocket structure **Then** API client can be imported and used without errors

## Tasks / Subtasks

- [x] Task 1: Create Axios API client (AC: 1, 2)
  - [x] Create `frontend/lib/api/client.ts`
  - [x] Import axios
  - [x] Create axios instance with baseURL from `process.env.NEXT_PUBLIC_API_URL`
  - [x] Add request interceptor for adding auth tokens (structure only, no actual token yet)
  - [x] Add response interceptor for error handling
  - [x] Add response interceptor for token refresh (structure only)
  - [x] Export configured axios instance
- [x] Task 2: Create API endpoint constants (AC: 3)
  - [x] Create `frontend/lib/api/endpoints.ts`
  - [x] Define endpoint constants matching backend routes: `/api/v1/auth/*`, `/api/v1/courses/*`, etc.
  - [x] Export endpoint constants
- [x] Task 3: Create placeholder API modules (AC: 4)
  - [x] Create `frontend/lib/api/auth.ts` with placeholder functions
  - [x] Create `frontend/lib/api/courses.ts` with placeholder functions
  - [x] Create `frontend/lib/api/learning.ts` with placeholder functions
  - [x] Create `frontend/lib/api/assessments.ts` with placeholder functions
  - [x] Create `frontend/lib/api/tutoring.ts` with placeholder functions
  - [x] Create `frontend/lib/api/progress.ts` with placeholder functions
  - [x] Create `frontend/lib/api/admin.ts` with placeholder functions
  - [x] Each module should import the API client and export placeholder functions
- [x] Task 4: Create WebSocket client structure (AC: 5, 6)
  - [x] Create `frontend/lib/websocket/client.ts`
  - [x] Create WebSocket client class with connection management
  - [x] Add methods for connect, disconnect, send, onMessage
  - [x] Create `frontend/lib/websocket/handlers.ts` with message handler structure
  - [x] Create `frontend/lib/websocket/reconnect.ts` with reconnection logic structure
- [x] Task 5: Verify API client can be imported (AC: 7)
  - [x] Test importing API client in a test component
  - [x] Verify no import errors
  - [x] Verify API client instance is created correctly

## Dev Notes

- **Architecture Patterns**: Axios instance with interceptors for authentication and error handling. WebSocket client for real-time communication.
- **Source Tree Components**:
  - `frontend/lib/api/client.ts` - Axios client configuration
  - `frontend/lib/api/endpoints.ts` - API endpoint constants
  - `frontend/lib/api/*.ts` - API module files (auth, courses, learning, etc.)
  - `frontend/lib/websocket/client.ts` - WebSocket client
  - `frontend/lib/websocket/handlers.ts` - WebSocket message handlers
  - `frontend/lib/websocket/reconnect.ts` - WebSocket reconnection logic
- **Testing Standards**: No tests required (structure setup only), but imports should be tested manually
- **Dependencies**: Story 1.14 must be complete (axios installed, environment configured)
- **API Structure**: Placeholder functions for now, full implementation in feature stories

### Project Structure Notes

- **Alignment**: API client structure matches architecture.md frontend API patterns. WebSocket structure for tutoring feature.
- **Interceptors**: Request/response interceptors for token management and error handling (structure only, implementation in auth stories)
- **Endpoint Constants**: Should match backend API routes exactly
- **No Conflicts**: Greenfield setup, no existing API client

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Frontend API Client] - API client patterns and WebSocket structure
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 14] - Task 14: Set up frontend API client and WebSocket structure
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.15] - Original story definition

## Dev Agent Record

### Agent Model Used

Claude Sonnet 4.5

### Debug Log References

- Build verification: `npm run build` completed successfully
- All TypeScript types resolved correctly
- No linting errors

### Completion Notes List

1. **API Client Created**: `frontend/lib/api/client.ts` with Axios instance, request/response interceptors for auth token management and error handling (structure only, implementation in auth stories)
2. **Endpoint Constants**: `frontend/lib/api/endpoints.ts` with all API endpoint constants matching backend routes (`/api/v1/auth/*`, `/api/v1/courses/*`, etc.)
3. **API Modules**: Created placeholder modules for all API domains:
   - `frontend/lib/api/auth.ts` - Authentication endpoints
   - `frontend/lib/api/courses.ts` - Course management
   - `frontend/lib/api/learning.ts` - Learning content
   - `frontend/lib/api/assessments.ts` - Assessments
   - `frontend/lib/api/tutoring.ts` - Tutoring sessions
   - `frontend/lib/api/progress.ts` - Progress tracking
   - `frontend/lib/api/admin.ts` - Admin functions
4. **WebSocket Client**: `frontend/lib/websocket/client.ts` with connection management, message handling, and automatic reconnection with exponential backoff
5. **WebSocket Handlers**: `frontend/lib/websocket/handlers.ts` with structure for message handlers
6. **WebSocket Reconnect**: `frontend/lib/websocket/reconnect.ts` with reconnection utilities
7. **Index Exports**: Created `frontend/lib/api/index.ts` and `frontend/lib/websocket/index.ts` for convenient imports
8. **Import Verification**: Created test page `frontend/app/test-api-imports/page.tsx` to verify all imports work correctly
9. **Build Verification**: All files compile successfully with no TypeScript or linting errors

### File List

- `frontend/lib/api/client.ts` - Axios API client with interceptors
- `frontend/lib/api/endpoints.ts` - API endpoint constants
- `frontend/lib/api/auth.ts` - Authentication API module
- `frontend/lib/api/courses.ts` - Courses API module
- `frontend/lib/api/learning.ts` - Learning API module
- `frontend/lib/api/assessments.ts` - Assessments API module
- `frontend/lib/api/tutoring.ts` - Tutoring API module
- `frontend/lib/api/progress.ts` - Progress API module
- `frontend/lib/api/admin.ts` - Admin API module
- `frontend/lib/api/index.ts` - API module exports
- `frontend/lib/websocket/client.ts` - WebSocket client class
- `frontend/lib/websocket/handlers.ts` - WebSocket message handlers
- `frontend/lib/websocket/reconnect.ts` - WebSocket reconnection utilities
- `frontend/lib/websocket/index.ts` - WebSocket module exports
- `frontend/app/test-api-imports/page.tsx` - Test page for import verification (can be removed after verification)
