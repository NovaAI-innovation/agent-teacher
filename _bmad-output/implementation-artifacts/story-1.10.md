# Story 1.10: Set Up Backend Models and Database Migrations

Status: ready-for-dev

## Story

As a developer,
I want SQLModel base models and Alembic migration structure,
so that I can define database schemas and manage migrations.

## Acceptance Criteria

1. **Given** Database connection is configured **When** I create models structure and initialize Alembic **Then** `backend/app/models/base.py` contains BaseModel with common fields (id, created_at, updated_at) using SQLModel
2. **Given** Database connection is configured **When** I create models structure and initialize Alembic **Then** Alembic is initialized in `backend/migrations/` directory
3. **Given** Database connection is configured **When** I create models structure and initialize Alembic **Then** `backend/migrations/env.py` is configured for SQLModel with database URL from environment
4. **Given** Database connection is configured **When** I create models structure and initialize Alembic **Then** `backend/migrations/env.py` imports BaseModel and is ready to import all model classes for autogenerate
5. **Given** Database connection is configured **When** I create models structure and initialize Alembic **Then** `backend/migrations/alembic.ini` is configured with database connection
6. **Given** Database connection is configured **When** I create models structure and initialize Alembic **Then** Running `alembic current` connects to database and shows current revision (or "empty" if no migrations)

## Tasks / Subtasks

- [ ] Task 1: Create BaseModel with common fields (AC: 1)
  - [ ] Create `backend/app/models/base.py`
  - [ ] Import SQLModel
  - [ ] Create BaseModel class with common fields:
    - `id`: Primary key (UUID or integer)
    - `created_at`: Timestamp (datetime)
    - `updated_at`: Timestamp (datetime)
  - [ ] Configure timestamps to auto-update on modification
  - [ ] Export BaseModel for use in other models
- [ ] Task 2: Initialize Alembic (AC: 2)
  - [ ] Run `alembic init migrations` in backend directory
  - [ ] Verify `backend/migrations/` directory is created
  - [ ] Verify `backend/migrations/versions/` directory exists
  - [ ] Verify `backend/migrations/env.py` and `backend/migrations/alembic.ini` are created
- [ ] Task 3: Configure Alembic env.py for SQLModel (AC: 3, 4)
  - [ ] Edit `backend/migrations/env.py`
  - [ ] Import database URL from config
  - [ ] Configure SQLModel engine creation
  - [ ] Import BaseModel from `app.models.base`
  - [ ] Configure autogenerate to detect model changes
  - [ ] Set up target_metadata to include all models
- [ ] Task 4: Configure alembic.ini (AC: 5)
  - [ ] Edit `backend/migrations/alembic.ini`
  - [ ] Set sqlalchemy.url (can use environment variable or placeholder)
  - [ ] Configure script location and version location
  - [ ] Set up logging configuration
- [ ] Task 5: Verify Alembic setup (AC: 6)
  - [ ] Run `cd backend && alembic current`
  - [ ] Verify connection to database works
  - [ ] Verify shows "empty" or current revision
  - [ ] Test creating a test migration: `alembic revision --autogenerate -m "test"`
  - [ ] Verify migration file is created in `migrations/versions/`

## Dev Notes

- **Architecture Patterns**: SQLModel for ORM, Alembic for database migrations. BaseModel pattern for common fields across all models.
- **Source Tree Components**: 
  - `backend/app/models/base.py` - BaseModel with common fields
  - `backend/migrations/` - Alembic migration directory
  - `backend/migrations/env.py` - Alembic environment configuration
  - `backend/migrations/alembic.ini` - Alembic configuration file
  - `backend/migrations/versions/` - Migration version files
- **Testing Standards**: No tests required (infrastructure setup), but Alembic commands should be tested manually
- **Dependencies**: Story 1.6 must be complete (database connection configured), Story 1.4 must be complete (alembic dependency installed)
- **Migration Strategy**: Use autogenerate for initial migrations, manual migrations for complex changes

### Project Structure Notes

- **Alignment**: SQLModel and Alembic setup follows architecture.md database patterns
- **BaseModel**: Common fields (id, created_at, updated_at) should be in all models via inheritance
- **Alembic Configuration**: Should use database URL from config, not hardcoded
- **Model Discovery**: env.py should be configured to discover all models automatically
- **No Conflicts**: Greenfield setup, no existing models or migrations

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Database & ORM] - SQLModel and Alembic patterns
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 9] - Task 9: Set up backend models and database migrations
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.10] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

