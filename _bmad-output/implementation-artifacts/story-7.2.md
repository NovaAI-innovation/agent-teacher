# Story 7.2: Track Learner Progress at Unit Level

Status: ready-for-dev

## Story

As the system,
I want to track learner progress at the unit level,
so that I can show learners their completion status for course units.

## Acceptance Criteria

1. **Given** A learner is enrolled in a course **When** The learner progresses through modules **Then** Unit-level progress is tracked (FR36)
2. **Given** A learner is enrolled in a course **When** The learner progresses through modules **Then** Unit progress is calculated from module progress
3. **Given** A learner is enrolled in a course **When** The learner progresses through modules **Then** Unit progress includes completion percentage
4. **Given** A learner is enrolled in a course **When** The learner progresses through modules **Then** Unit progress is stored in the database
5. **Given** A learner is enrolled in a course **When** The learner progresses through modules **Then** Unit progress is updated when modules are completed

## Tasks / Subtasks

- [ ] Task 1: Create unit progress model (AC: 1, 4)
  - [ ] Create `backend/app/models/unit_progress.py`
  - [ ] Store progress (user_id, unit_id, completion_percentage, completed_modules_count, total_modules)
  - [ ] Create database migration
- [ ] Task 2: Calculate unit progress (AC: 2, 3, 5)
  - [ ] Update `backend/app/services/progress_service.py`
  - [ ] Calculate unit progress from module progress
  - [ ] Calculate completion percentage
  - [ ] Update when modules are completed
- [ ] Task 3: Create unit progress API (AC: 1)
  - [ ] Update `backend/app/api/v1/progress.py`
  - [ ] Add unit progress endpoint
  - [ ] Return unit progress data

## Dev Notes

- **Architecture Patterns**: Aggregated progress tracking. Percentage calculation. Hierarchical progress.
- **Source Tree Components**: 
  - `backend/app/models/unit_progress.py` - Unit progress model
  - `backend/app/services/progress_service.py` - Updated progress service
  - `backend/app/api/v1/progress.py` - Updated progress API
- **Testing Standards**: Unit tests for progress calculation, integration tests
- **Dependencies**: Story 7.1 must be complete (Module progress)
- **Calculation**: Unit progress = (completed modules / total modules) * 100

### Project Structure Notes

- **Alignment**: Unit progress follows architecture.md progress patterns. Calculated from module progress.
- **Aggregation**: Calculate unit progress from module progress. Update when modules complete.
- **Percentage**: Calculate completion percentage for units
- **Hierarchy**: Maintain Course → Unit → Module progress hierarchy

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Progress Tracking] - Unit progress patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR36] - FR36: Unit Progress Tracking requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 7.2] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

