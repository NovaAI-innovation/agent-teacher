# Story 3.6: Unenroll from a Course

Status: ready-for-dev

## Story

As a learner,
I want to unenroll from a course,
so that I can remove courses I no longer want to take.

## Acceptance Criteria

1. **Given** I am enrolled in a course **When** I navigate to my enrolled courses and click "Unenroll" **Then** My enrollment is removed from the database
2. **Given** I am enrolled in a course **When** I navigate to my enrolled courses and click "Unenroll" **Then** I receive confirmation that I've unenrolled
3. **Given** I am enrolled in a course **When** I navigate to my enrolled courses and click "Unenroll" **Then** The course no longer appears in my enrolled courses list
4. **Given** I am enrolled in a course **When** I navigate to my enrolled courses and click "Unenroll" **Then** My progress data for the course is preserved (for potential re-enrollment)
5. **Given** I am enrolled in a course **When** I navigate to my enrolled courses and click "Unenroll" **Then** I can re-enroll in the course later if desired
6. **Given** I am enrolled in a course **When** I navigate to my enrolled courses and click "Unenroll" **Then** Unenrollment event is logged

## Tasks / Subtasks

- [ ] Task 1: Create unenroll API endpoint (AC: 1, 6)
  - [ ] Update `backend/app/api/v1/courses.py` with unenroll endpoint
  - [ ] Require authentication
  - [ ] Verify user is enrolled
  - [ ] Soft delete enrollment (mark as inactive) or hard delete
  - [ ] Preserve progress data (don't delete progress records)
  - [ ] Log unenrollment event
  - [ ] Return success response
- [ ] Task 2: Create unenroll service (AC: 1, 4, 6)
  - [ ] Update `backend/app/services/enrollment_service.py` with unenroll logic
  - [ ] Handle enrollment removal
  - [ ] Preserve progress data
  - [ ] Log unenrollment events
- [ ] Task 3: Create enrolled courses page (AC: 3)
  - [ ] Create `frontend/app/my-courses/page.tsx`
  - [ ] Fetch user's enrolled courses
  - [ ] Display enrolled courses list
  - [ ] Add unenroll button for each course
- [ ] Task 4: Create unenroll button component (AC: 1, 2, 3)
  - [ ] Create `frontend/components/course/UnenrollButton.tsx`
  - [ ] Add confirmation dialog (confirm before unenrolling)
  - [ ] Handle unenroll API call
  - [ ] Show loading state
  - [ ] Show success message
  - [ ] Refresh enrolled courses list
- [ ] Task 5: Update API client (AC: 1, 3)
  - [ ] Update `frontend/lib/api/courses.ts` with unenrollCourse function
  - [ ] Update getEnrolledCourses function

## Dev Notes

- **Architecture Patterns**: Soft delete or hard delete enrollment. Preserve progress data. Confirmation dialog for destructive action.
- **Source Tree Components**: 
  - `backend/app/api/v1/courses.py` - Unenroll endpoint
  - `backend/app/services/enrollment_service.py` - Unenroll service
  - `frontend/app/my-courses/page.tsx` - Enrolled courses page
  - `frontend/components/course/UnenrollButton.tsx` - Unenroll button component
  - `frontend/lib/api/courses.ts` - Unenroll API client
- **Testing Standards**: Unit tests for unenroll service, integration tests for unenroll API, E2E tests for unenroll flow
- **Dependencies**: Story 3.5 must be complete (Enrollment), Story 2.2 must be complete (Authentication)
- **Data Preservation**: Preserve progress data when unenrolling. Allow re-enrollment later.

### Project Structure Notes

- **Alignment**: Unenrollment follows architecture.md enrollment patterns. Progress data preservation.
- **Confirmation**: Require user confirmation before unenrolling (destructive action)
- **Progress Data**: Keep progress records even after unenrollment. Restore on re-enrollment.
- **Re-enrollment**: User can re-enroll later. Restore previous progress if available.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Course Management] - Unenrollment patterns (lines 2573-2581)
- [Source: _bmad-output/planning-artifacts/prd.md#FR13] - FR13: Unenroll from Course requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 3.6] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

