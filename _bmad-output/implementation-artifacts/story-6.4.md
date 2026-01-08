# Story 6.4: Maintain Tutoring Conversation History

Status: ready-for-dev

## Story

As the system,
I want to maintain tutoring conversation history,
so that tutoring sessions can reference previous conversations.

## Acceptance Criteria

1. **Given** A tutoring session is active **When** Messages are exchanged **Then** Conversation history is maintained (FR33)
2. **Given** A tutoring session is active **When** Messages are exchanged **Then** All messages (learner and tutor) are stored
3. **Given** A tutoring session is active **When** Messages are exchanged **Then** Conversation history is available for the tutor to reference
4. **Given** A tutoring session is active **When** Messages are exchanged **Then** Conversation history persists across session reconnections

## Tasks / Subtasks

- [ ] Task 1: Create conversation message model (AC: 1, 2)
  - [ ] Create `backend/app/models/tutoring_message.py`
  - [ ] Store messages (session_id, sender, content, timestamp)
  - [ ] Link to tutoring session
  - [ ] Create database migration
- [ ] Task 2: Store conversation messages (AC: 1, 2)
  - [ ] Update `backend/app/services/tutoring_service.py`
  - [ ] Store learner messages
  - [ ] Store tutor responses
  - [ ] Persist to database
- [ ] Task 3: Load conversation history (AC: 3, 4)
  - [ ] Load conversation history on session start
  - [ ] Load history on reconnection
  - [ ] Pass history to tutor agent
- [ ] Task 4: Update tutor agent (AC: 3)
  - [ ] Update `backend/app/services/agents/tutor_agent.py`
  - [ ] Use conversation history in responses
  - [ ] Reference previous messages
- [ ] Task 5: Display conversation history (AC: 4)
  - [ ] Update `frontend/components/tutoring/TutoringChat.tsx`
  - [ ] Load and display conversation history
  - [ ] Show history on reconnection

## Dev Notes

- **Architecture Patterns**: Conversation persistence. History management. Session continuity.
- **Source Tree Components**:
  - `backend/app/models/tutoring_message.py` - Conversation message model
  - `backend/app/services/tutoring_service.py` - Updated with history management
  - `backend/app/services/agents/tutor_agent.py` - Updated to use history
  - `frontend/components/tutoring/TutoringChat.tsx` - Updated to display history
- **Testing Standards**: Unit tests for history management, integration tests, E2E tests
- **Dependencies**: Story 6.1 must be complete (Tutoring sessions)
- **History Management**: Store all messages. Load history on session start/reconnection. Use in responses.

### Project Structure Notes

- **Alignment**: Conversation history follows architecture.md tutoring patterns. Persistent and accessible.
- **Persistence**: Store all messages in database. Link to session. Enable history retrieval.
- **Context**: Use conversation history to provide context-aware responses
- **Reconnection**: Load history on reconnection to maintain conversation continuity

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Interactive Tutoring] - Conversation history patterns (lines 2599-2602)
- [Source: _bmad-output/planning-artifacts/prd.md#FR33] - FR33: Conversation History requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 6.4] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
