# Story 6.2: Tutor Queries Knowledge Base for Module-Specific Content

Status: ready-for-dev

## Story

As the system,
I want the tutor to query the knowledge base for module-specific content,
so that tutoring responses are contextually relevant.

## Acceptance Criteria

1. **Given** A tutoring session is active **When** The tutor needs information **Then** Tutor queries knowledge base for module-specific content (FR31)
2. **Given** A tutoring session is active **When** The tutor needs information **Then** Knowledge base queries return relevant content for the current module
3. **Given** A tutoring session is active **When** The tutor needs information **Then** Tutor uses module context to provide accurate answers
4. **Given** A tutoring session is active **When** The tutor needs information **Then** Knowledge base queries are efficient and fast

## Tasks / Subtasks

- [ ] Task 1: Create knowledge base query service (AC: 1, 2, 4)
  - [ ] Update `backend/app/services/knowledge/knowledge_base.py`
  - [ ] Implement module-specific content queries
  - [ ] Query Supabase knowledge base
  - [ ] Filter by module/course context
  - [ ] Optimize query performance
- [ ] Task 2: Integrate knowledge base into tutor agent (AC: 1, 2, 3)
  - [ ] Create `backend/app/services/agents/tutor_agent.py`
  - [ ] Query knowledge base for module content
  - [ ] Use module context in queries
  - [ ] Integrate content into tutor responses
- [ ] Task 3: Create tutor agent (AC: 3)
  - [ ] Implement tutor agent using pydantic-ai
  - [ ] Use knowledge base content in responses
  - [ ] Provide contextually relevant answers
- [ ] Task 4: Update tutoring service (AC: 1, 2)
  - [ ] Update `backend/app/services/tutoring_service.py`
  - [ ] Query knowledge base when processing messages
  - [ ] Pass module context to tutor agent

## Dev Notes

- **Architecture Patterns**: Knowledge base integration. Context-aware queries. Agent-based tutoring.
- **Source Tree Components**: 
  - `backend/app/services/knowledge/knowledge_base.py` - Updated knowledge base service
  - `backend/app/services/agents/tutor_agent.py` - Tutor agent
  - `backend/app/services/tutoring_service.py` - Updated tutoring service
- **Testing Standards**: Unit tests for knowledge base queries, agent tests, integration tests
- **Dependencies**: Story 6.1 must be complete (Tutoring sessions), Story 4.7 must be complete (Knowledge base storage)
- **Context-Aware**: Use module/course context to query relevant content. Provide accurate, relevant answers.

### Project Structure Notes

- **Alignment**: Knowledge base queries follow architecture.md knowledge base patterns. Context-aware.
- **Query Performance**: Optimize queries for speed. Cache frequently accessed content.
- **Context**: Use module/course context to filter knowledge base queries
- **Agent Integration**: Tutor agent uses knowledge base content to provide accurate answers

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Interactive Tutoring] - Knowledge base integration (lines 2599-2602)
- [Source: _bmad-output/planning-artifacts/prd.md#FR31] - FR31: Knowledge Base Queries requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 6.2] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

