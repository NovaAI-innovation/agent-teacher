# Story 9.3: Trigger Course Generation Requests

Status: ready-for-dev

## Story

As an administrator,
I want to trigger course generation requests,
so that I can create new courses on demand.

## Acceptance Criteria

1. **Given** I am an administrator **When** I want to create a new course **Then** I can trigger a course generation request (FR66)
2. **Given** I am an administrator **When** I want to create a new course **Then** I can specify the course topic
3. **Given** I am an administrator **When** I want to create a new course **Then** Generation request is submitted to the system
4. **Given** I am an administrator **When** I want to create a new course **Then** I receive confirmation that generation has started
5. **Given** I am an administrator **When** I want to create a new course **Then** I can track the generation progress

## Tasks / Subtasks

- [ ] Task 1: Create course generation request API (AC: 1, 2, 3, 4)
  - [ ] Update `backend/app/api/v1/admin/courses.py`
  - [ ] Create trigger generation endpoint
  - [ ] Accept topic request
  - [ ] Start generation workflow
  - [ ] Return generation job ID
  - [ ] Return confirmation
- [ ] Task 2: Create generation request form (AC: 1, 2, 3, 4, 5)
  - [ ] Create `frontend/app/admin/course-generation/new/page.tsx`
  - [ ] Create form for topic input
  - [ ] Submit generation request
  - [ ] Show confirmation
  - [ ] Link to progress tracking
- [ ] Task 3: Integrate with generation workflow (AC: 1, 3)
  - [ ] Trigger Prefect workflow
  - [ ] Pass topic to workflow
  - [ ] Start generation process

## Dev Notes

- **Architecture Patterns**: Course generation trigger. Workflow integration. Progress tracking.
- **Source Tree Components**: 
  - `backend/app/api/v1/admin/courses.py` - Generation trigger API
  - `frontend/app/admin/course-generation/new/page.tsx` - Generation request form
  - `backend/orchestration/workflows/course_generation_workflow.py` - Generation workflow
- **Testing Standards**: Unit tests for form, integration tests for API, E2E tests for generation trigger
- **Dependencies**: Story 4.5 must be complete (Course generation workflow)
- **User Experience**: Simple form. Clear confirmation. Progress tracking.

### Project Structure Notes

- **Alignment**: Generation trigger follows architecture.md admin patterns. Simple and clear.
- **Form**: Simple form for topic input. Clear submission process.
- **Confirmation**: Confirm generation started. Provide job ID for tracking.
- **Integration**: Integrate with Prefect workflow. Start generation process.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Course Generation] - Generation trigger patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR66] - FR66: Trigger Course Generation requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 9.3] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

