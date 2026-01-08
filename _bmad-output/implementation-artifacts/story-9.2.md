# Story 9.2: Monitor Course Generation Activities

Status: ready-for-dev

## Story

As an administrator,
I want to monitor course generation activities,
so that I can track content creation progress and issues.

## Acceptance Criteria

1. **Given** I am an administrator **When** I access the admin dashboard **Then** I can monitor course generation activities (FR55)
2. **Given** I am an administrator **When** I access the admin dashboard **Then** I can see active generation jobs
3. **Given** I am an administrator **When** I access the admin dashboard **Then** I can see generation progress and status
4. **Given** I am an administrator **When** I access the admin dashboard **Then** I can see generation history
5. **Given** I am an administrator **When** I access the admin dashboard **Then** I can see generation errors and failures
6. **Given** I am an administrator **When** I access the admin dashboard **Then** Generation monitoring is real-time or near real-time

## Tasks / Subtasks

- [ ] Task 1: Create generation monitoring API (AC: 1, 2, 3, 4, 5, 6)
  - [ ] Create `backend/app/api/v1/admin/course_generation.py`
  - [ ] Return active generation jobs
  - [ ] Return generation progress
  - [ ] Return generation history
  - [ ] Return errors and failures
  - [ ] Support real-time updates
- [ ] Task 2: Create generation monitoring dashboard (AC: 1, 2, 3, 4, 5, 6)
  - [ ] Create `frontend/app/admin/course-generation/page.tsx`
  - [ ] Display active jobs
  - [ ] Show generation progress
  - [ ] Display generation history
  - [ ] Show errors and failures
  - [ ] Support real-time updates
- [ ] Task 3: Create generation job component (AC: 2, 3)
  - [ ] Create `frontend/components/admin/GenerationJobCard.tsx`
  - [ ] Display job status and progress
  - [ ] Show job details
- [ ] Task 4: Integrate with Prefect (AC: 1, 2, 3)
  - [ ] Query Prefect for job status
  - [ ] Display Prefect workflow status
  - [ ] Show workflow progress

## Dev Notes

- **Architecture Patterns**: Generation monitoring. Job tracking. Real-time updates.
- **Source Tree Components**:
  - `backend/app/api/v1/admin/course_generation.py` - Generation monitoring API
  - `frontend/app/admin/course-generation/page.tsx` - Generation dashboard
  - `frontend/components/admin/GenerationJobCard.tsx` - Job component
- **Testing Standards**: Unit tests for components, integration tests for API, E2E tests
- **Dependencies**: Story 4.5 must be complete (Course generation)
- **Monitoring**: Track active jobs, progress, history, errors. Real-time updates.

### Project Structure Notes

- **Alignment**: Generation monitoring follows architecture.md admin patterns. Comprehensive tracking.
- **Job Tracking**: Track all generation jobs. Show status and progress.
- **History**: Maintain generation history. Show past jobs and outcomes.
- **Errors**: Display errors and failures. Help with debugging.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Monitoring] - Generation monitoring patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR55] - FR55: Monitor Course Generation requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 9.2] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
