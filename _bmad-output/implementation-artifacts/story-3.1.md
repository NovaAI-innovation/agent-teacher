# Story 3.1: Maintain Course Catalog

Status: ready-for-dev

## Story

As the system,
I want to maintain a catalog of available courses,
so that learners can discover and access courses.

## Acceptance Criteria

1. **Given** The system has course data **When** Courses are generated or updated **Then** Course catalog is updated in the database
2. **Given** The system has course data **When** Courses are generated or updated **Then** Course metadata (title, description, topic, status) is stored
3. **Given** The system has course data **When** Courses are generated or updated **Then** Course hierarchy (Course → Unit → Module) is maintained
4. **Given** The system has course data **When** Courses are generated or updated **Then** Course catalog supports querying and filtering
5. **Given** The system has course data **When** Courses are generated or updated **Then** Course status (draft, published, archived) is tracked
6. **Given** The system has course data **When** Courses are generated or updated **Then** Course catalog is cached in Redis for performance

## Tasks / Subtasks

- [ ] Task 1: Create Course models (AC: 1, 2, 3, 5)
  - [ ] Create `backend/app/models/course.py` - Course model (id, title, description, topic, status, created_at, updated_at)
  - [ ] Create `backend/app/models/unit.py` - Unit model (id, course_id, title, order, created_at, updated_at)
  - [ ] Create `backend/app/models/module.py` - Module model (id, unit_id, title, order, created_at, updated_at)
  - [ ] Define relationships (Course has many Units, Unit has many Modules)
  - [ ] Add status enum (draft, published, archived)
  - [ ] Create database migrations
- [ ] Task 2: Create course service (AC: 1, 2, 3, 4, 5)
  - [ ] Create `backend/app/services/course_service.py`
  - [ ] Implement create/update course methods
  - [ ] Implement query methods (with filtering)
  - [ ] Implement status management
  - [ ] Maintain course hierarchy
- [ ] Task 3: Implement Redis caching (AC: 6)
  - [ ] Create cache utility functions
  - [ ] Cache course catalog data in Redis
  - [ ] Implement cache invalidation on course updates
  - [ ] Add cache key patterns
- [ ] Task 4: Create course catalog API endpoint (AC: 4)
  - [ ] Create `backend/app/api/v1/courses.py` catalog endpoint
  - [ ] Support querying (search, filter by topic, status)
  - [ ] Support pagination
  - [ ] Return cached data when available
- [ ] Task 5: Create database indexes (AC: 4)
  - [ ] Add indexes for common queries (topic, status, created_at)
  - [ ] Update migration

## Dev Notes

- **Architecture Patterns**: Hierarchical data model (Course → Unit → Module). Redis caching for performance. Status-based workflow.
- **Source Tree Components**:
  - `backend/app/models/course.py` - Course model
  - `backend/app/models/unit.py` - Unit model
  - `backend/app/models/module.py` - Module model
  - `backend/app/services/course_service.py` - Course catalog service
  - `backend/app/api/v1/courses.py` - Course catalog API
  - `backend/migrations/versions/` - Course models migrations
- **Testing Standards**: Unit tests for models and service, integration tests for API, performance tests for caching
- **Dependencies**: Epic 1 must be complete (database, Redis, API structure)
- **Caching Strategy**: Cache course catalog in Redis. Invalidate on updates. Use appropriate TTL.

### Project Structure Notes

- **Alignment**: Course models follow architecture.md data architecture patterns. Hierarchy matches content structure.
- **Status Workflow**: Draft → Published → Archived. Only published courses visible to learners.
- **Caching**: Cache course list and individual courses. Invalidate on create/update/delete.
- **No Conflicts**: Greenfield setup, no existing course models

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Course Management] - Course model patterns (lines 2573-2581)
- [Source: _bmad-output/planning-artifacts/prd.md#FR5, FR7] - FR5: Course Catalog, FR7: Course Structure requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 3.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
