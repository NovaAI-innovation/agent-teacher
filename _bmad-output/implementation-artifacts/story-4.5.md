# Story 4.5: Generate Course Introductions from Topic Requests

Status: ready-for-dev

## Story

As the system,
I want to autonomously generate course introductions,
so that courses can be created from topic requests without human content creators.

## Acceptance Criteria

1. **Given** An administrator triggers a course generation request (FR66) **When** A topic request is received **Then** Curriculum Designer Agent generates a course introduction
2. **Given** An administrator triggers a course generation request (FR66) **When** A topic request is received **Then** Course introduction includes: title, description, learning objectives, prerequisites, estimated duration
3. **Given** An administrator triggers a course generation request (FR66) **When** A topic request is received **Then** Generated content is stored in the knowledge base (FR19)
4. **Given** An administrator triggers a course generation request (FR66) **When** A topic request is received **Then** Course introduction meets quality benchmark standards (FR18)
5. **Given** An administrator triggers a course generation request (FR66) **When** A topic request is received **Then** Course is organized in Course → Unit → Module hierarchy (FR7)
6. **Given** An administrator triggers a course generation request (FR66) **When** A topic request is received **Then** Generation completes within performance targets (30 minutes for first module)

## Tasks / Subtasks

- [ ] Task 1: Implement Curriculum Designer Agent (AC: 1, 2, 5)
  - [ ] Create `backend/app/services/agents/curriculum_designer_agent.py`
  - [ ] Implement course introduction generation using pydantic-ai
  - [ ] Generate course title, description, learning objectives, prerequisites, estimated duration
  - [ ] Create Course → Unit → Module hierarchy structure
  - [ ] Use LLM service client for content generation
- [ ] Task 2: Create course generation API endpoint (AC: 1)
  - [ ] Create `backend/app/api/v1/admin/courses.py` generation endpoint
  - [ ] Accept topic request
  - [ ] Trigger course generation workflow
  - [ ] Return generation job ID
- [ ] Task 3: Create course generation workflow (AC: 1, 6)
  - [ ] Update `backend/orchestration/workflows/course_generation_workflow.py`
  - [ ] Integrate Curriculum Designer Agent
  - [ ] Set performance targets (30 minutes for first module)
  - [ ] Track generation progress
- [ ] Task 4: Store generated content in knowledge base (AC: 3)
  - [ ] Update knowledge base service
  - [ ] Store course introduction in Supabase
  - [ ] Link to course record
- [ ] Task 5: Quality evaluation integration (AC: 4)
  - [ ] Integrate with QA Agent for quality checks
  - [ ] Ensure content meets quality benchmarks
  - [ ] Handle quality failures

## Dev Notes

- **Architecture Patterns**: Agent-based content generation using pydantic-ai. Prefect workflow orchestration. Knowledge base storage.
- **Source Tree Components**:
  - `backend/app/services/agents/curriculum_designer_agent.py` - Curriculum Designer Agent
  - `backend/app/api/v1/admin/courses.py` - Course generation endpoint
  - `backend/orchestration/workflows/course_generation_workflow.py` - Generation workflow
  - `backend/app/services/knowledge/knowledge_base.py` - Knowledge base service
- **Testing Standards**: Unit tests for agent, integration tests for workflow, E2E tests for generation
- **Dependencies**: Story 4.1 must be complete (Agent orchestration), Story 4.4 must be complete (LLM services)
- **Performance**: Target 30 minutes for first module generation. Track and optimize generation time.

### Project Structure Notes

- **Alignment**: Course generation follows architecture.md agent patterns. pydantic-ai for agent implementation.
- **Agent Implementation**: Use pydantic-ai framework for structured agent responses
- **Quality Gates**: Integrate quality checks before storing content
- **Hierarchy**: Generate complete Course → Unit → Module structure

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Content Generation] - Course generation patterns (lines 2583-2588)
- [Source: _bmad-output/planning-artifacts/prd.md#FR6, FR16, FR17] - FR6: Course Generation, FR16-17: Content Generation requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 4.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
