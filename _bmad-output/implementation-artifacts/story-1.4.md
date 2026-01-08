# Story 1.4: Configure Backend Dependencies and Package Management

Status: ready-for-dev

## Story

As a developer,
I want backend pyproject.toml with all dependencies configured,
so that I can install and manage Python packages with uv.

## Acceptance Criteria

1. **Given** The backend directory structure exists **When** I create `backend/pyproject.toml` **Then** It contains project metadata (name, version, description, Python version >=3.12)
2. **Given** The backend directory structure exists **When** I create `backend/pyproject.toml` **Then** It includes all required dependencies: FastAPI, SQLModel, pydantic-ai, Prefect, slowapi>=0.1.9, pydantic-settings, and all other dependencies from architecture.md
3. **Given** The backend directory structure exists **When** I create `backend/pyproject.toml` **Then** It includes dev dependencies: pytest, pytest-asyncio, black, ruff, mypy, flake8, pre-commit, testcontainers
4. **Given** The backend directory structure exists **When** I create `backend/pyproject.toml` **Then** It includes tool configurations for Black, Ruff, and mypy
5. **Given** The backend directory structure exists **When** I create `backend/pyproject.toml` **Then** Running `cd backend && uv sync` installs all dependencies successfully and generates `uv.lock`

## Tasks / Subtasks

- [ ] Task 1: Create pyproject.toml with project metadata (AC: 1)
  - [ ] Add project name: "agent-teacher-backend"
  - [ ] Add version: "0.1.0"
  - [ ] Add description
  - [ ] Set Python version requirement: ">=3.12"
  - [ ] Add authors and license information
- [ ] Task 2: Add all required dependencies (AC: 2)
  - [ ] Add FastAPI and uvicorn[standard]
  - [ ] Add SQLModel and supabase
  - [ ] Add pydantic-ai
  - [ ] Add Prefect
  - [ ] Add slowapi>=0.1.9
  - [ ] Add pydantic-settings
  - [ ] Add python-dotenv
  - [ ] Add alembic
  - [ ] Add python-jose[cryptography] for JWT
  - [ ] Add passlib[bcrypt] for password hashing
  - [ ] Add redis (redis-py)
  - [ ] Add aio-pika for RabbitMQ
  - [ ] Add all other dependencies from architecture.md lines 711-764
- [ ] Task 3: Add dev dependencies (AC: 3)
  - [ ] Add pytest and pytest-asyncio
  - [ ] Add black
  - [ ] Add ruff
  - [ ] Add mypy
  - [ ] Add flake8
  - [ ] Add pre-commit
  - [ ] Add testcontainers
- [ ] Task 4: Configure tool settings (AC: 4)
  - [ ] Configure Black settings (line length, target version)
  - [ ] Configure Ruff settings (line length, select rules, ignore patterns)
  - [ ] Configure mypy settings (strict mode, Python version, ignore patterns)
- [ ] Task 5: Verify dependency installation (AC: 5)
  - [ ] Run `cd backend && uv sync`
  - [ ] Verify all dependencies install successfully
  - [ ] Verify `uv.lock` file is generated
  - [ ] Check for version conflicts

## Dev Notes

- **Architecture Patterns**: Use `uv` package manager exclusively (per user rules). All dependencies must be pinned in uv.lock
- **Source Tree Components**: 
  - `backend/pyproject.toml` - Main dependency configuration
  - `backend/uv.lock` - Generated lock file (should be committed)
- **Testing Standards**: No tests required (configuration only)
- **Dependencies**: Story 1.3 must be complete (backend directory structure exists)
- **Package Manager**: Must use `uv` (not pip, pip-tools, or poetry) per project rules

### Project Structure Notes

- **Alignment**: pyproject.toml follows Python packaging standards and uv requirements
- **Dependency Versions**: Reference architecture.md lines 711-764 for exact dependency versions
- **Lock File**: uv.lock should be committed to version control
- **No Conflicts**: Greenfield project, no existing dependencies to conflict with

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Dependencies] - Complete dependency list (lines 711-764)
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 4] - Task 4: Create backend pyproject.toml
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.4] - Original story definition
- [Source: User Rules] - Must use `uv` package manager exclusively

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

