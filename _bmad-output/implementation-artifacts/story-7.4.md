# Story 7.4: View Progress Across All Enrolled Courses

Status: ready-for-dev

## Story

As a learner,
I want to view my progress across all enrolled courses,
so that I can see my overall learning journey.

## Acceptance Criteria

1. **Given** I am enrolled in multiple courses **When** I view my progress dashboard **Then** I can see progress across all enrolled courses (FR38)
2. **Given** I am enrolled in multiple courses **When** I view my progress dashboard **Then** Progress is displayed for each course
3. **Given** I am enrolled in multiple courses **When** I view my progress dashboard **Then** Progress includes completion percentages
4. **Given** I am enrolled in multiple courses **When** I view my progress dashboard **Then** Progress is displayed in a clear, visual format
5. **Given** I am enrolled in multiple courses **When** I view my progress dashboard **Then** I can navigate to individual course progress details

## Tasks / Subtasks

- [ ] Task 1: Create progress dashboard API (AC: 1, 2, 3)
  - [ ] Update `backend/app/api/v1/progress.py`
  - [ ] Create get all courses progress endpoint
  - [ ] Return progress for all enrolled courses
  - [ ] Include completion percentages
- [ ] Task 2: Create progress dashboard page (AC: 1, 2, 3, 4, 5)
  - [ ] Create `frontend/app/learning/page.tsx` or `frontend/app/progress/page.tsx`
  - [ ] Display progress for all courses
  - [ ] Show completion percentages
  - [ ] Use visual progress indicators
  - [ ] Make clear and accessible
- [ ] Task 3: Create progress card component (AC: 2, 3, 4, 5)
  - [ ] Create `frontend/components/progress/CourseProgressCard.tsx`
  - [ ] Display course progress
  - [ ] Show completion percentage
  - [ ] Link to course progress details
  - [ ] Visual progress indicator
- [ ] Task 4: Create progress visualization (AC: 4)
  - [ ] Create progress bar component
  - [ ] Visualize completion percentages
  - [ ] Make accessible

## Dev Notes

- **Architecture Patterns**: Progress dashboard. Multi-course view. Visual progress indicators.
- **Source Tree Components**: 
  - `backend/app/api/v1/progress.py` - Progress dashboard API
  - `frontend/app/learning/page.tsx` or `frontend/app/progress/page.tsx` - Progress dashboard
  - `frontend/components/progress/CourseProgressCard.tsx` - Progress card component
  - `frontend/components/progress/ProgressBar.tsx` - Progress visualization
- **Testing Standards**: Unit tests for components, integration tests for API, E2E tests for dashboard
- **Dependencies**: Story 7.3 must be complete (Course progress)
- **Visualization**: Use progress bars, percentages, visual indicators. Make accessible.

### Project Structure Notes

- **Alignment**: Progress dashboard follows architecture.md UX patterns. Clear and visual.
- **Multi-Course**: Display progress for all enrolled courses. Easy navigation.
- **Visualization**: Use progress bars, charts, or other visual indicators
- **Accessibility**: Make progress visualization accessible. Screen reader support.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Progress Tracking] - Progress dashboard patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR38] - FR38: View Progress requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 7.4] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

