# Story 5.10: Reset Progress Within a Course

Status: ready-for-dev

## Story

As a learner,
I want to reset my progress within a course,
so that I can start over if I want to retake the course.

## Acceptance Criteria

1. **Given** I am enrolled in a course with progress **When** I choose to reset my progress **Then** My progress for that course is reset (FR15)
2. **Given** I am enrolled in a course with progress **When** I choose to reset my progress **Then** All module completion statuses are cleared
3. **Given** I am enrolled in a course with progress **When** I choose to reset my progress **Then** All assessment results are preserved (or cleared, based on requirements)
4. **Given** I am enrolled in a course with progress **When** I choose to reset my progress **Then** I receive confirmation that progress has been reset
5. **Given** I am enrolled in a course with progress **When** I choose to reset my progress **Then** I can start the course from the beginning
6. **Given** I am enrolled in a course with progress **When** I choose to reset my progress **Then** Reset action is logged

## Tasks / Subtasks

- [ ] Task 1: Create progress reset API endpoint (AC: 1, 2, 3, 6)
  - [ ] Create `backend/app/api/v1/learning.py` reset progress endpoint
  - [ ] Require authentication
  - [ ] Reset module completion statuses
  - [ ] Handle assessment results (preserve or clear based on requirements)
  - [ ] Log reset action
  - [ ] Return success response
- [ ] Task 2: Create progress reset service (AC: 1, 2, 3)
  - [ ] Create `backend/app/services/learning_service.py` reset method
  - [ ] Clear module completions
  - [ ] Handle assessment results
  - [ ] Reset progress tracking
- [ ] Task 3: Create reset confirmation dialog (AC: 4)
  - [ ] Create confirmation component
  - [ ] Warn user about reset action
  - [ ] Require confirmation
  - [ ] Show what will be reset
- [ ] Task 4: Add reset button (AC: 1, 4, 5)
  - [ ] Add reset progress button to course page
  - [ ] Show confirmation dialog
  - [ ] Handle reset action
  - [ ] Refresh course view after reset
- [ ] Task 5: Update progress display (AC: 5)
  - [ ] Update progress indicators after reset
  - [ ] Show course as starting from beginning
  - [ ] Allow access to first module

## Dev Notes

- **Architecture Patterns**: Progress reset with confirmation. Selective data clearing. Action logging.
- **Source Tree Components**:
  - `backend/app/api/v1/learning.py` - Reset progress API
  - `backend/app/services/learning_service.py` - Reset progress service
  - `frontend/components/learning/ResetProgressDialog.tsx` - Reset confirmation dialog
  - `frontend/app/learning/[courseId]/page.tsx` - Updated with reset button
- **Testing Standards**: Unit tests for reset logic, integration tests for API, E2E tests for reset flow
- **Dependencies**: Story 5.2 must be complete (Course content access), Story 5.3 must be complete (Progress tracking)
- **Data Handling**: Decide whether to preserve or clear assessment results on reset. Document decision.

### Project Structure Notes

- **Alignment**: Progress reset follows architecture.md learning patterns. Confirmation required for destructive action.
- **Confirmation**: Require user confirmation before resetting progress (destructive action)
- **Selective Reset**: Reset module completions. Decide on assessment results (preserve for history or clear for fresh start)
- **User Experience**: Clear confirmation dialog. Explain what will be reset. Allow cancellation.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Learning & Assessment] - Progress reset patterns (lines 2590-2597)
- [Source: _bmad-output/planning-artifacts/prd.md#FR15] - FR15: Reset Progress requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.10] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
