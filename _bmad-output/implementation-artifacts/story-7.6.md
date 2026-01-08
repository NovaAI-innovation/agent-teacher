# Story 7.6: Calculate and Display Progress Percentages

Status: ready-for-dev

## Story

As a learner,
I want to see progress percentages,
so that I understand how much of a course I've completed.

## Acceptance Criteria

1. **Given** I am enrolled in a course **When** I view my progress **Then** Progress percentages are calculated and displayed (FR40)
2. **Given** I am enrolled in a course **When** I view my progress **Then** Progress percentages are accurate
3. **Given** I am enrolled in a course **When** I view my progress **Then** Progress percentages are displayed at module, unit, and course levels
4. **Given** I am enrolled in a course **When** I view my progress **Then** Progress percentages are updated in real-time
5. **Given** I am enrolled in a course **When** I view my progress **Then** Progress percentages are displayed clearly and accessibly

## Tasks / Subtasks

- [ ] Task 1: Calculate progress percentages (AC: 1, 2, 3)
  - [ ] Update `backend/app/services/progress_service.py`
  - [ ] Calculate module progress percentage
  - [ ] Calculate unit progress percentage (from modules)
  - [ ] Calculate course progress percentage (from units)
  - [ ] Ensure accuracy
- [ ] Task 2: Include percentages in API (AC: 1, 3)
  - [ ] Update `backend/app/api/v1/progress.py`
  - [ ] Include percentages in progress responses
  - [ ] Return percentages at all levels
- [ ] Task 3: Display progress percentages (AC: 1, 4, 5)
  - [ ] Update progress components
  - [ ] Display percentages prominently
  - [ ] Update in real-time
  - [ ] Make accessible
- [ ] Task 4: Create percentage display component (AC: 5)
  - [ ] Create `frontend/components/progress/ProgressPercentage.tsx`
  - [ ] Display percentage clearly
  - [ ] Make accessible (screen reader announces percentage)

## Dev Notes

- **Architecture Patterns**: Percentage calculation. Real-time updates. Accessible display.
- **Source Tree Components**: 
  - `backend/app/services/progress_service.py` - Updated with percentage calculation
  - `backend/app/api/v1/progress.py` - Updated with percentages
  - `frontend/components/progress/ProgressPercentage.tsx` - Percentage display component
- **Testing Standards**: Unit tests for percentage calculation, integration tests, accessibility tests
- **Dependencies**: Story 7.1, 7.2, 7.3 must be complete (Progress tracking)
- **Calculation**: Accurate percentage calculation. Update in real-time. Display clearly.

### Project Structure Notes

- **Alignment**: Progress percentages follow architecture.md progress patterns. Accurate and accessible.
- **Calculation**: Module = (completed items / total items) * 100. Unit = (completed modules / total modules) * 100. Course = (completed units / total units) * 100.
- **Real-time**: Update percentages as progress changes
- **Accessibility**: Announce percentages to screen readers. Clear visual display.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Progress Tracking] - Percentage calculation patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR40] - FR40: Progress Percentages requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 7.6] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

