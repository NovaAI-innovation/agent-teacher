# Story 1.11: Configure Backend Testing Infrastructure

Status: ready-for-dev

## Story

As a developer,
I want pytest configuration with async support and test fixtures,
so that I can write and run backend tests.

## Acceptance Criteria

1. **Given** Backend structure is set up **When** I create testing infrastructure **Then** `backend/tests/conftest.py` contains pytest configuration with async support (pytest-asyncio)
2. **Given** Backend structure is set up **When** I create testing infrastructure **Then** Test fixtures exist for test client, test database, and mock services
3. **Given** Backend structure is set up **When** I create testing infrastructure **Then** Testcontainers setup is configured for integration tests
4. **Given** Backend structure is set up **When** I create testing infrastructure **Then** Test directory structure exists: `tests/unit/`, `tests/integration/`, `tests/e2e/` with `__init__.py` files
5. **Given** Backend structure is set up **When** I create testing infrastructure **Then** Running `uv run pytest` executes successfully (even with no tests)
6. **Given** Backend structure is set up **When** I create testing infrastructure **Then** Test discovery works correctly

## Tasks / Subtasks

- [ ] Task 1: Create pytest configuration (AC: 1, 6)
  - [ ] Create `backend/tests/conftest.py`
  - [ ] Configure pytest with pytest-asyncio plugin
  - [ ] Set up pytest.ini or pyproject.toml pytest configuration
  - [ ] Configure test discovery patterns
  - [ ] Configure async test support
- [ ] Task 2: Create test fixtures (AC: 2)
  - [ ] Create test client fixture (FastAPI TestClient)
  - [ ] Create test database fixture (in-memory or test database)
  - [ ] Create mock service fixtures (Redis, RabbitMQ, Supabase)
  - [ ] Create session fixture for database tests
  - [ ] Configure fixture scopes appropriately
- [ ] Task 3: Configure Testcontainers (AC: 3)
  - [ ] Import testcontainers library
  - [ ] Create Testcontainers fixtures for integration tests
  - [ ] Configure containers for PostgreSQL, Redis, RabbitMQ (if needed)
  - [ ] Set up container lifecycle management
- [ ] Task 4: Create test directory structure (AC: 4)
  - [ ] Ensure `backend/tests/unit/` exists with `__init__.py`
  - [ ] Ensure `backend/tests/integration/` exists with `__init__.py`
  - [ ] Ensure `backend/tests/e2e/` exists with `__init__.py`
  - [ ] Create `backend/tests/__init__.py` if needed
- [ ] Task 5: Verify pytest setup (AC: 5, 6)
  - [ ] Run `cd backend && uv run pytest`
  - [ ] Verify pytest executes without errors
  - [ ] Verify test discovery finds test directories
  - [ ] Create a simple test file to verify fixtures work

## Dev Notes

- **Architecture Patterns**: pytest with async support for FastAPI testing. Testcontainers for integration testing with real services.
- **Source Tree Components**: 
  - `backend/tests/conftest.py` - Pytest configuration and fixtures
  - `backend/tests/unit/` - Unit test directory
  - `backend/tests/integration/` - Integration test directory
  - `backend/tests/e2e/` - End-to-end test directory
  - `backend/pytest.ini` or `backend/pyproject.toml` - Pytest configuration
- **Testing Standards**: Follow pytest best practices. Use fixtures for test setup/teardown. Async tests for FastAPI endpoints.
- **Dependencies**: Story 1.4 must be complete (pytest dependencies installed), Story 1.7 must be complete (FastAPI app exists)
- **Test Structure**: Separate unit, integration, and e2e tests. Use fixtures for common test setup.

### Project Structure Notes

- **Alignment**: Test structure follows pytest conventions and architecture.md testing patterns
- **Fixtures**: Reusable fixtures for common test scenarios (client, database, mocks)
- **Testcontainers**: Use for integration tests requiring real services (database, Redis, etc.)
- **No Conflicts**: Greenfield setup, no existing tests

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Testing] - Testing patterns and strategies
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 10] - Task 10: Configure backend testing infrastructure
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.11] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

