# Story 6.6: Persist and Restore Tutoring Sessions

Status: ready-for-dev

## Story

As a learner,
I want my tutoring sessions to persist and restore,
so that I can continue conversations after interruptions.

## Acceptance Criteria

1. **Given** I have an active tutoring session **When** I navigate away or close the browser **Then** Tutoring session is persisted (FR76)
2. **Given** I have an active tutoring session **When** I navigate away or close the browser **Then** I can restore the session when I return
3. **Given** I have an active tutoring session **When** I navigate away or close the browser **Then** Conversation history is preserved
4. **Given** I have an active tutoring session **When** I navigate away or close the browser **Then** Session context (module/course) is maintained

## Tasks / Subtasks

- [ ] Task 1: Update session persistence (AC: 1, 3, 4)
  - [ ] Update `backend/app/models/tutoring_session.py`
  - [ ] Add session state (active, paused, closed)
  - [ ] Persist session data
  - [ ] Store conversation history
  - [ ] Store session context
- [ ] Task 2: Create session restore API (AC: 2)
  - [ ] Create `backend/app/api/v1/tutoring.py` restore endpoint
  - [ ] Load session by ID
  - [ ] Return session data and history
  - [ ] Require authentication
- [ ] Task 3: Implement session restore (AC: 2, 3, 4)
  - [ ] Update `backend/app/services/tutoring_service.py`
  - [ ] Restore session from database
  - [ ] Load conversation history
  - [ ] Restore session context
- [ ] Task 4: Create session restore UI (AC: 2)
  - [ ] Update `frontend/components/tutoring/TutoringChat.tsx`
  - [ ] Check for existing sessions on load
  - [ ] Offer to restore session
  - [ ] Load conversation history
- [ ] Task 5: Handle session lifecycle (AC: 1)
  - [ ] Mark sessions as paused on disconnect
  - [ ] Allow session resumption
  - [ ] Handle session expiration

## Dev Notes

- **Architecture Patterns**: Session persistence. State management. Session restoration.
- **Source Tree Components**: 
  - `backend/app/models/tutoring_session.py` - Updated with persistence
  - `backend/app/api/v1/tutoring.py` - Session restore API
  - `backend/app/services/tutoring_service.py` - Session restore service
  - `frontend/components/tutoring/TutoringChat.tsx` - Session restore UI
- **Testing Standards**: Unit tests for persistence, integration tests for restore, E2E tests for session restore
- **Dependencies**: Story 6.4 must be complete (Conversation history)
- **Persistence**: Store sessions and history. Allow restoration. Maintain context.

### Project Structure Notes

- **Alignment**: Session persistence follows architecture.md tutoring patterns. Reliable and user-friendly.
- **Session State**: Track active, paused, closed states. Allow resumption.
- **History Preservation**: Preserve conversation history across sessions
- **Context Maintenance**: Maintain module/course context when restoring

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Interactive Tutoring] - Session persistence patterns (lines 2599-2602)
- [Source: _bmad-output/planning-artifacts/prd.md#FR76] - FR76: Session Persistence requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 6.6] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

