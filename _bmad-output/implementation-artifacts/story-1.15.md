# Story 1.15: Set Up Frontend API Client and WebSocket Structure

Status: ready-for-dev

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

- [ ] Task 1: Create Axios API client (AC: 1, 2)
  - [ ] Create `frontend/lib/api/client.ts`
  - [ ] Import axios
  - [ ] Create axios instance with baseURL from `process.env.NEXT_PUBLIC_API_URL`
  - [ ] Add request interceptor for adding auth tokens (structure only, no actual token yet)
  - [ ] Add response interceptor for error handling
  - [ ] Add response interceptor for token refresh (structure only)
  - [ ] Export configured axios instance
- [ ] Task 2: Create API endpoint constants (AC: 3)
  - [ ] Create `frontend/lib/api/endpoints.ts`
  - [ ] Define endpoint constants matching backend routes: `/api/v1/auth/*`, `/api/v1/courses/*`, etc.
  - [ ] Export endpoint constants
- [ ] Task 3: Create placeholder API modules (AC: 4)
  - [ ] Create `frontend/lib/api/auth.ts` with placeholder functions
  - [ ] Create `frontend/lib/api/courses.ts` with placeholder functions
  - [ ] Create `frontend/lib/api/learning.ts` with placeholder functions
  - [ ] Create `frontend/lib/api/assessments.ts` with placeholder functions
  - [ ] Create `frontend/lib/api/tutoring.ts` with placeholder functions
  - [ ] Create `frontend/lib/api/progress.ts` with placeholder functions
  - [ ] Create `frontend/lib/api/admin.ts` with placeholder functions
  - [ ] Each module should import the API client and export placeholder functions
- [ ] Task 4: Create WebSocket client structure (AC: 5, 6)
  - [ ] Create `frontend/lib/websocket/client.ts`
  - [ ] Create WebSocket client class with connection management
  - [ ] Add methods for connect, disconnect, send, onMessage
  - [ ] Create `frontend/lib/websocket/handlers.ts` with message handler structure
  - [ ] Create `frontend/lib/websocket/reconnect.ts` with reconnection logic structure
- [ ] Task 5: Verify API client can be imported (AC: 7)
  - [ ] Test importing API client in a test component
  - [ ] Verify no import errors
  - [ ] Verify API client instance is created correctly

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

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

