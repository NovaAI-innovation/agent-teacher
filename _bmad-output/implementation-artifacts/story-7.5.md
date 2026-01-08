# Story 7.5: View Completion Status for Modules, Units, and Courses

Status: ready-for-dev

## Story

As a learner,
I want to view completion status for modules, units, and courses,
so that I know what I've completed and what's remaining.

## Acceptance Criteria

1. **Given** I am enrolled in a course **When** I view course details **Then** I can see completion status for modules, units, and course (FR39)
2. **Given** I am enrolled in a course **When** I view course details **Then** Completion status is clearly indicated (completed, in-progress, not started)
3. **Given** I am enrolled in a course **When** I view course details **Then** Completion status is displayed at all levels (module, unit, course)
4. **Given** I am enrolled in a course **When** I view course details **Then** Completion indicators are accessible and visually clear

## Tasks / Subtasks

- [ ] Task 1: Create completion status API (AC: 1)
  - [ ] Update `backend/app/api/v1/progress.py`
  - [ ] Create get completion status endpoint
  - [ ] Return completion status for modules, units, course
  - [ ] Include status indicators
- [ ] Task 2: Create completion status component (AC: 2, 4)
  - [ ] Create `frontend/components/progress/CompletionStatus.tsx`
  - [ ] Display completion indicators (checkmark, in-progress, not started)
  - [ ] Make visually clear
  - [ ] Make accessible
- [ ] Task 3: Integrate completion status (AC: 1, 3)
  - [ ] Update course detail page
  - [ ] Show module completion status
  - [ ] Show unit completion status
  - [ ] Show course completion status
- [ ] Task 4: Create status indicators (AC: 2, 4)
  - [ ] Design completion indicators
  - [ ] Use icons or badges
  - [ ] Ensure accessibility

## Dev Notes

- **Architecture Patterns**: Completion status display. Multi-level status. Accessible indicators.
- **Source Tree Components**:
  - `backend/app/api/v1/progress.py` - Completion status API
  - `frontend/components/progress/CompletionStatus.tsx` - Completion status component
  - Course detail pages updated with completion status
- **Testing Standards**: Unit tests for components, integration tests, accessibility tests
- **Dependencies**: Story 7.1, 7.2, 7.3 must be complete (Progress tracking)
- **Status Display**: Clear indicators for completed, in-progress, not started. Accessible format.

### Project Structure Notes

- **Alignment**: Completion status follows architecture.md UX patterns. Clear and accessible.
- **Multi-Level**: Show status at module, unit, and course levels
- **Visual Indicators**: Use clear icons/badges for status. Color coding if appropriate.
- **Accessibility**: Make status indicators accessible. Screen reader support. Clear labels.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Progress Tracking] - Completion status patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR39] - FR39: Completion Status requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 7.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
