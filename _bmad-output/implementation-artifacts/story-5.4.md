# Story 5.4: Take Assessments for Completed Modules

Status: ready-for-dev

## Story

As a learner,
I want to take assessments after completing modules,
so that I can demonstrate my understanding.

## Acceptance Criteria

1. **Given** I have completed a module **When** I navigate to the assessment **Then** I can access the assessment for that module
2. **Given** I have completed a module **When** I navigate to the assessment **Then** Assessment questions are displayed clearly
3. **Given** I have completed a module **When** I navigate to the assessment **Then** I can submit my answers
4. **Given** I have completed a module **When** I navigate to the assessment **Then** Assessment interface is accessible and responsive
5. **Given** I have completed a module **When** I navigate to the assessment **Then** I can see my progress through the assessment
6. **Given** I have completed a module **When** I navigate to the assessment **Then** Assessment submission is validated before processing

## Tasks / Subtasks

- [ ] Task 1: Create assessment access API (AC: 1)
  - [ ] Update `backend/app/api/v1/assessments.py` with get assessment endpoint
  - [ ] Verify module completion
  - [ ] Return assessment questions
  - [ ] Require authentication
- [ ] Task 2: Create assessment page (AC: 1, 2, 3, 4, 5)
  - [ ] Create `frontend/app/learning/[courseId]/modules/[moduleId]/assessment/page.tsx`
  - [ ] Display assessment questions
  - [ ] Create assessment form
  - [ ] Show progress indicator
  - [ ] Make accessible and responsive
- [ ] Task 3: Create assessment form component (AC: 2, 3, 6)
  - [ ] Create `frontend/components/assessment/AssessmentForm.tsx`
  - [ ] Support multiple question types
  - [ ] Validate answers before submission
  - [ ] Handle form submission
- [ ] Task 4: Create progress indicator (AC: 5)
  - [ ] Show question number (e.g., "Question 3 of 10")
  - [ ] Show completion percentage
  - [ ] Update as user progresses
- [ ] Task 5: Create assessment submission API (AC: 3, 6)
  - [ ] Create `backend/app/api/v1/assessments.py` submit endpoint
  - [ ] Validate submission
  - [ ] Store assessment responses
  - [ ] Trigger grading

## Dev Notes

- **Architecture Patterns**: Assessment access with module completion check. Form validation. Accessible assessment interface.
- **Source Tree Components**:
  - `backend/app/api/v1/assessments.py` - Assessment API
  - `frontend/app/learning/[courseId]/modules/[moduleId]/assessment/page.tsx` - Assessment page
  - `frontend/components/assessment/AssessmentForm.tsx` - Assessment form
- **Testing Standards**: Unit tests for form, integration tests for API, E2E tests for assessment flow, accessibility tests
- **Dependencies**: Story 5.3 must be complete (Module completion), Story 4.8 must be complete (Assessment generation)
- **Accessibility**: WCAG 2.1 AA compliant. Screen reader support. Keyboard navigation.

### Project Structure Notes

- **Alignment**: Assessment access follows architecture.md assessment patterns. Accessible and user-friendly.
- **Module Completion**: Verify module is completed before allowing assessment access
- **Question Types**: Support multiple choice, short answer, and other types from assessment generation
- **Validation**: Validate answers before submission. Provide clear error messages.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Learning & Assessment] - Assessment patterns (lines 2590-2597)
- [Source: _bmad-output/planning-artifacts/prd.md#FR24] - FR24: Take Assessments requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.4] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
