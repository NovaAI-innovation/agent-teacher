# Story 7.3: Track Learner Progress at Course Level

Status: ready-for-dev

## Story

As the system,
I want to track learner progress at the course level,
so that I can show learners their overall course completion.

## Acceptance Criteria

1. **Given** A learner is enrolled in a course **When** The learner progresses through units and modules **Then** Course-level progress is tracked (FR37)
2. **Given** A learner is enrolled in a course **When** The learner progresses through units and modules **Then** Course progress is calculated from unit progress
3. **Given** A learner is enrolled in a course **When** The learner progresses through units and modules **Then** Course progress includes completion percentage
4. **Given** A learner is enrolled in a course **When** The learner progresses through units and modules **Then** Course progress is stored in the database
5. **Given** A learner is enrolled in a course **When** The learner progresses through units and modules **Then** Course progress is updated when units are completed

## Tasks / Subtasks

- [ ] Task 1: Create course progress model (AC: 1, 4)
  - [ ] Create `backend/app/models/course_progress.py` or update enrollment model
  - [ ] Store progress (user_id, course_id, completion_percentage, completed_units_count, total_units)
  - [ ] Create database migration
- [ ] Task 2: Calculate course progress (AC: 2, 3, 5)
  - [ ] Update `backend/app/services/progress_service.py`
  - [ ] Calculate course progress from unit progress
  - [ ] Calculate completion percentage
  - [ ] Update when units are completed
- [ ] Task 3: Create course progress API (AC: 1)
  - [ ] Update `backend/app/api/v1/progress.py`
  - [ ] Add course progress endpoint
  - [ ] Return course progress data

## Dev Notes

- **Architecture Patterns**: Aggregated progress tracking. Hierarchical calculation. Course-level metrics.
- **Source Tree Components**: 
  - `backend/app/models/course_progress.py` - Course progress model
  - `backend/app/services/progress_service.py` - Updated progress service
  - `backend/app/api/v1/progress.py` - Updated progress API
- **Testing Standards**: Unit tests for progress calculation, integration tests
- **Dependencies**: Story 7.2 must be complete (Unit progress)
- **Calculation**: Course progress = (completed units / total units) * 100

### Project Structure Notes

- **Alignment**: Course progress follows architecture.md progress patterns. Calculated from unit progress.
- **Aggregation**: Calculate course progress from unit progress. Update when units complete.
- **Percentage**: Calculate completion percentage for courses
- **Hierarchy**: Maintain Course → Unit → Module progress hierarchy

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Progress Tracking] - Course progress patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR37] - FR37: Course Progress Tracking requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 7.3] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

