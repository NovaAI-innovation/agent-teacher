# Story 6.3: Provide Context-Aware Responses to Learner Questions

Status: ready-for-dev

## Story

As the system,
I want to provide context-aware responses to learner questions,
so that tutoring is relevant and helpful.

## Acceptance Criteria

1. **Given** A learner asks a question in a tutoring session **When** The tutor processes the question **Then** Tutor provides context-aware responses (FR32)
2. **Given** A learner asks a question in a tutoring session **When** The tutor processes the question **Then** Responses consider the learner's current module/course context
3. **Given** A learner asks a question in a tutoring session **When** The tutor processes the question **Then** Responses are relevant to the learning material
4. **Given** A learner asks a question in a tutoring session **When** The tutor processes the question **Then** Responses are educational and helpful

## Tasks / Subtasks

- [ ] Task 1: Enhance tutor agent (AC: 1, 2, 3, 4)
  - [ ] Update `backend/app/services/agents/tutor_agent.py`
  - [ ] Use module/course context in responses
  - [ ] Query knowledge base for relevant content
  - [ ] Generate context-aware responses
  - [ ] Ensure responses are educational
- [ ] Task 2: Create context management (AC: 2)
  - [ ] Track learner's current module/course
  - [ ] Pass context to tutor agent
  - [ ] Update context during session
- [ ] Task 3: Update tutoring service (AC: 1, 3, 4)
  - [ ] Update `backend/app/services/tutoring_service.py`
  - [ ] Process learner questions with context
  - [ ] Generate context-aware responses
  - [ ] Return responses via WebSocket

## Dev Notes

- **Architecture Patterns**: Context-aware agent responses. Knowledge base integration. Educational responses.
- **Source Tree Components**:
  - `backend/app/services/agents/tutor_agent.py` - Enhanced tutor agent
  - `backend/app/services/tutoring_service.py` - Updated tutoring service
- **Testing Standards**: Unit tests for context-aware responses, integration tests, E2E tests
- **Dependencies**: Story 6.2 must be complete (Knowledge base queries)
- **Context Awareness**: Use module/course context to provide relevant, helpful responses.

### Project Structure Notes

- **Alignment**: Context-aware responses follow architecture.md agent patterns. Educational and relevant.
- **Context Usage**: Leverage module/course context for relevant answers
- **Response Quality**: Ensure responses are educational, helpful, and contextually relevant
- **Knowledge Integration**: Use knowledge base content to inform responses

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Interactive Tutoring] - Context-aware patterns (lines 2599-2602)
- [Source: _bmad-output/planning-artifacts/prd.md#FR32] - FR32: Context-Aware Responses requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 6.3] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
