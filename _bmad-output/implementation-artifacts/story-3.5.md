# Story 3.5: Enroll in a Course

Status: ready-for-dev

## Story

As a learner,
I want to enroll in a course,
so that I can access the course content and start learning.

## Acceptance Criteria

1. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** My enrollment is created in the database
2. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** I am redirected to the course learning page
3. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** I receive confirmation that I've successfully enrolled
4. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** The course appears in my enrolled courses list
5. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** Enrollment status is tracked (enrolled, in-progress, completed)
6. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** Duplicate enrollment attempts are handled gracefully
7. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** Enrollment count for the course is updated
8. **Given** I am logged in and viewing a course detail page **When** I click the "Enroll" button **Then** Enrollment event is logged for analytics

## Tasks / Subtasks

- [ ] Task 1: Create Enrollment model (AC: 1, 5)
  - [ ] Create `backend/app/models/enrollment.py`
  - [ ] Define Enrollment model (id, user_id, course_id, status, enrolled_at, completed_at)
  - [ ] Add status enum (enrolled, in-progress, completed)
  - [ ] Add unique constraint (user_id, course_id)
  - [ ] Create database migration
- [ ] Task 2: Create enrollment API endpoint (AC: 1, 6, 7, 8)
  - [ ] Update `backend/app/api/v1/courses.py` with enroll endpoint
  - [ ] Require authentication
  - [ ] Check for duplicate enrollment
  - [ ] Create enrollment record
  - [ ] Update course enrollment count
  - [ ] Log enrollment event
  - [ ] Return success response
- [ ] Task 3: Create enrollment service (AC: 1, 5, 6, 7, 8)
  - [ ] Create `backend/app/services/enrollment_service.py`
  - [ ] Implement enroll user logic
  - [ ] Handle duplicate enrollment (return existing or error)
  - [ ] Update enrollment count
  - [ ] Log enrollment events
- [ ] Task 4: Create enroll button component (AC: 1, 2, 3, 6)
  - [ ] Create `frontend/components/course/EnrollButton.tsx`
  - [ ] Check if user is enrolled
  - [ ] Display "Enroll" or "Already Enrolled" button
  - [ ] Handle enrollment API call
  - [ ] Show loading state
  - [ ] Show success message
  - [ ] Handle errors gracefully
- [ ] Task 5: Integrate enroll button (AC: 1, 2, 3)
  - [ ] Update `frontend/app/courses/[slug]/page.tsx`
  - [ ] Add EnrollButton component
  - [ ] Handle redirect after enrollment
- [ ] Task 6: Create enrolled courses API endpoint (AC: 4)
  - [ ] Update `backend/app/api/v1/courses.py` with enrolled courses endpoint
  - [ ] Return user's enrolled courses
  - [ ] Include enrollment status
- [ ] Task 7: Update API client (AC: 1, 4)
  - [ ] Update `frontend/lib/api/courses.ts` with enrollCourse function
  - [ ] Add getEnrolledCourses function

## Dev Notes

- **Architecture Patterns**: Enrollment tracking with status. Duplicate prevention. Analytics logging.
- **Source Tree Components**:
  - `backend/app/models/enrollment.py` - Enrollment model
  - `backend/app/api/v1/courses.py` - Enrollment endpoint
  - `backend/app/services/enrollment_service.py` - Enrollment service
  - `frontend/components/course/EnrollButton.tsx` - Enroll button component
  - `frontend/app/courses/[slug]/page.tsx` - Updated course detail page
  - `frontend/lib/api/courses.ts` - Enrollment API client
- **Testing Standards**: Unit tests for enrollment service, integration tests for enrollment API, E2E tests for enrollment flow
- **Dependencies**: Story 2.2 must be complete (Authentication), Story 3.1 must be complete (Course models), Story 3.4 must be complete (Course detail page)
- **Enrollment Logic**: Prevent duplicate enrollments. Track enrollment status. Update course statistics.

### Project Structure Notes

- **Alignment**: Enrollment follows architecture.md enrollment patterns. Status tracking for progress.
- **Duplicate Handling**: Check for existing enrollment before creating. Return existing enrollment or error message.
- **Analytics**: Log enrollment events for tracking and analytics
- **Status Tracking**: Initial status is "enrolled", changes to "in-progress" when learning starts, "completed" when finished

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Course Management] - Enrollment patterns (lines 2573-2581)
- [Source: _bmad-output/planning-artifacts/prd.md#FR12] - FR12: Enroll in Course requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 3.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
