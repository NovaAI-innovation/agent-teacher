# Story 5.8: Retake Assessments

Status: ready-for-dev

## Story

As a learner,
I want to retake assessments if needed,
so that I can improve my understanding and score.

## Acceptance Criteria

1. **Given** I have completed an assessment **When** I choose to retake the assessment **Then** I can retake the assessment (FR28)
2. **Given** I have completed an assessment **When** I choose to retake the assessment **Then** Previous attempts are preserved in my history
3. **Given** I have completed an assessment **When** I choose to retake the assessment **Then** I can see my improvement across attempts
4. **Given** I have completed an assessment **When** I choose to retake the assessment **Then** Retake functionality is clearly available
5. **Given** I have completed an assessment **When** I choose to retake the assessment **Then** Assessment retakes are tracked for analytics

## Tasks / Subtasks

- [ ] Task 1: Update assessment response model (AC: 2)
  - [ ] Update `backend/app/models/assessment_response.py`
  - [ ] Support multiple attempts per assessment
  - [ ] Track attempt number
  - [ ] Preserve all attempts
- [ ] Task 2: Create retake API endpoint (AC: 1)
  - [ ] Update `backend/app/api/v1/assessments.py` with retake endpoint
  - [ ] Create new assessment attempt
  - [ ] Preserve previous attempts
  - [ ] Return new attempt ID
- [ ] Task 3: Add retake button (AC: 1, 4)
  - [ ] Update results page
  - [ ] Add "Retake Assessment" button
  - [ ] Make button clearly visible
  - [ ] Handle retake action
- [ ] Task 4: Create attempt history view (AC: 2, 3)
  - [ ] Create component to show attempt history
  - [ ] Display all attempts with scores
  - [ ] Show improvement trends
  - [ ] Compare attempts
- [ ] Task 5: Track retakes for analytics (AC: 5)
  - [ ] Log retake events
  - [ ] Track retake frequency
  - [ ] Store analytics data

## Dev Notes

- **Architecture Patterns**: Multiple attempts tracking. Attempt history. Improvement tracking.
- **Source Tree Components**: 
  - `backend/app/models/assessment_response.py` - Updated with attempt tracking
  - `backend/app/api/v1/assessments.py` - Retake API
  - `frontend/app/learning/[courseId]/modules/[moduleId]/assessment/results/page.tsx` - Updated with retake button
  - `frontend/components/assessment/AttemptHistory.tsx` - Attempt history component
- **Testing Standards**: Unit tests for retake logic, integration tests for API, E2E tests for retake flow
- **Dependencies**: Story 5.7 must be complete (View results)
- **Attempt Tracking**: Preserve all attempts. Track attempt numbers. Show improvement.

### Project Structure Notes

- **Alignment**: Retake functionality follows architecture.md assessment patterns. Multiple attempts supported.
- **Attempt Preservation**: Keep all attempts. Don't delete previous attempts on retake.
- **Improvement Tracking**: Show scores across attempts. Visualize improvement trends.
- **User Experience**: Make retake option clear and accessible.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Learning & Assessment] - Retake patterns (lines 2590-2597)
- [Source: _bmad-output/planning-artifacts/prd.md#FR28] - FR28: Retake Assessments requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.8] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

