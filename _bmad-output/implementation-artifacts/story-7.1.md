# Story 7.1: Track Learner Progress at Module Level

Status: ready-for-dev

## Story

As the system,
I want to track learner progress at the module level,
so that I can show learners their completion status for individual modules.

## Acceptance Criteria

1. **Given** A learner is enrolled in a course **When** The learner accesses or completes module content **Then** Module-level progress is tracked (FR35)
2. **Given** A learner is enrolled in a course **When** The learner accesses or completes module content **Then** Progress includes: started, in-progress, completed status
3. **Given** A learner is enrolled in a course **When** The learner accesses or completes module content **Then** Progress is stored in the database
4. **Given** A learner is enrolled in a course **When** The learner accesses or completes module content **Then** Progress is updated in real-time as learners interact with content
5. **Given** A learner is enrolled in a course **When** The learner accesses or completes module content **Then** Progress data is accurate and consistent

## Tasks / Subtasks

- [ ] Task 1: Create module progress model (AC: 1, 3)
  - [ ] Create `backend/app/models/module_progress.py`
  - [ ] Store progress (user_id, module_id, status, started_at, completed_at)
  - [ ] Define status enum (started, in-progress, completed)
  - [ ] Create database migration
- [ ] Task 2: Create progress tracking service (AC: 1, 2, 4, 5)
  - [ ] Create `backend/app/services/progress_service.py`
  - [ ] Track module access (mark as started)
  - [ ] Update progress status
  - [ ] Mark module as completed (content viewed + assessment passed)
  - [ ] Update in real-time
- [ ] Task 3: Create progress API endpoints (AC: 1, 3)
  - [ ] Create `backend/app/api/v1/progress.py`
  - [ ] Create get progress endpoint
  - [ ] Create update progress endpoint
  - [ ] Require authentication
- [ ] Task 4: Integrate progress tracking (AC: 1, 4)
  - [ ] Update learning service to track progress
  - [ ] Track on module access
  - [ ] Track on module completion
  - [ ] Update in real-time

## Dev Notes

- **Architecture Patterns**: Progress tracking. Real-time updates. Status management.
- **Source Tree Components**:
  - `backend/app/models/module_progress.py` - Module progress model
  - `backend/app/services/progress_service.py` - Progress tracking service
  - `backend/app/api/v1/progress.py` - Progress API
- **Testing Standards**: Unit tests for progress tracking, integration tests for API, E2E tests
- **Dependencies**: Story 5.3 must be complete (Module access), Story 5.5 must be complete (Assessment completion)
- **Progress States**: Started (first access), In-progress (actively learning), Completed (content + assessment done)

### Project Structure Notes

- **Alignment**: Progress tracking follows architecture.md progress patterns. Real-time and accurate.
- **Status Tracking**: Track started, in-progress, completed states. Update in real-time.
- **Completion Criteria**: Module completed = content viewed + assessment passed
- **Data Consistency**: Ensure progress data is accurate and consistent

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Progress Tracking] - Progress tracking patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR35] - FR35: Module Progress Tracking requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 7.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
