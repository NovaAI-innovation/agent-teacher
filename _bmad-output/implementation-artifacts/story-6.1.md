# Story 6.1: Initiate Chat-Based Tutoring Sessions

Status: ready-for-dev

## Story

As a learner,
I want to initiate chat-based tutoring sessions,
so that I can get help while learning.

## Acceptance Criteria

1. **Given** I am learning course content **When** I want help from a tutor **Then** I can initiate a chat-based tutoring session (FR30)
2. **Given** I am learning course content **When** I want help from a tutor **Then** Tutoring session is connected via WebSocket
3. **Given** I am learning course content **When** I want help from a tutor **Then** I can send messages to the tutor
4. **Given** I am learning course content **When** I want help from a tutor **Then** I receive responses from the tutor in real-time
5. **Given** I am learning course content **When** I want help from a tutor **Then** Tutoring session is linked to my current module/course context

## Tasks / Subtasks

- [ ] Task 1: Create WebSocket endpoint (AC: 2, 3, 4)
  - [ ] Create `backend/app/api/v1/tutoring.py` WebSocket endpoint
  - [ ] Implement WebSocket connection handler
  - [ ] Handle message sending/receiving
  - [ ] Require authentication
- [ ] Task 2: Create tutoring session model (AC: 1, 5)
  - [ ] Create `backend/app/models/tutoring_session.py`
  - [ ] Store session data (user_id, course_id, module_id, started_at)
  - [ ] Link to course/module context
  - [ ] Create database migration
- [ ] Task 3: Create tutoring service (AC: 1, 4)
  - [ ] Create `backend/app/services/tutoring_service.py`
  - [ ] Handle session initiation
  - [ ] Process tutor messages
  - [ ] Manage session lifecycle
- [ ] Task 4: Create frontend WebSocket client (AC: 2, 3, 4)
  - [ ] Update `frontend/lib/websocket/client.ts`
  - [ ] Connect to tutoring WebSocket endpoint
  - [ ] Send/receive messages
  - [ ] Handle connection events
- [ ] Task 5: Create tutoring interface (AC: 1, 3, 4, 5)
  - [ ] Create `frontend/components/tutoring/TutoringChat.tsx`
  - [ ] Display chat interface
  - [ ] Allow message input
  - [ ] Display messages in real-time
  - [ ] Show course/module context
- [ ] Task 6: Integrate tutoring into learning page (AC: 1, 5)
  - [ ] Add tutoring button to module page
  - [ ] Open tutoring chat
  - [ ] Pass course/module context

## Dev Notes

- **Architecture Patterns**: WebSocket for real-time communication. Session management. Context-aware tutoring.
- **Source Tree Components**: 
  - `backend/app/api/v1/tutoring.py` - WebSocket tutoring endpoint
  - `backend/app/models/tutoring_session.py` - Tutoring session model
  - `backend/app/services/tutoring_service.py` - Tutoring service
  - `frontend/lib/websocket/client.ts` - WebSocket client
  - `frontend/components/tutoring/TutoringChat.tsx` - Tutoring chat component
- **Testing Standards**: Unit tests for service, integration tests for WebSocket, E2E tests for tutoring flow
- **Dependencies**: Story 5.2 must be complete (Course content access), Story 1.15 must be complete (WebSocket structure)
- **Real-time**: WebSocket for bidirectional real-time communication. Low latency for responsive tutoring.

### Project Structure Notes

- **Alignment**: Tutoring follows architecture.md WebSocket patterns. Real-time, context-aware.
- **WebSocket**: Use FastAPI WebSocket for backend. Browser WebSocket API for frontend.
- **Context**: Pass course/module context to tutor for relevant help
- **Session Management**: Track active sessions. Manage session lifecycle.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Interactive Tutoring] - Tutoring patterns (lines 2599-2602)
- [Source: _bmad-output/planning-artifacts/prd.md#FR30] - FR30: Chat-Based Tutoring requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 6.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

