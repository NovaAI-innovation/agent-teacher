# Story 1.4: Configure Backend Dependencies and Package Management

Status: review

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

- [x] Task 1: Create pyproject.toml with project metadata (AC: 1)
  - [x] Add project name: "agent-teacher-backend"
  - [x] Add version: "0.1.0"
  - [x] Add description
  - [x] Set Python version requirement: ">=3.12"
  - [x] Add authors and license information
- [x] Task 2: Add all required dependencies (AC: 2)
  - [x] Add FastAPI and uvicorn[standard]
  - [x] Add SQLModel and supabase
  - [x] Add pydantic-ai
  - [x] Add Prefect
  - [x] Add slowapi>=0.1.9
  - [x] Add pydantic-settings
  - [x] Add python-dotenv
  - [x] Add alembic
  - [x] Add python-jose[cryptography] for JWT
  - [x] Add passlib[bcrypt] for password hashing
  - [x] Add redis (redis-py)
  - [x] Add aio-pika for RabbitMQ
  - [x] Add all other dependencies from architecture.md lines 711-764
- [x] Task 3: Add dev dependencies (AC: 3)
  - [x] Add pytest and pytest-asyncio
  - [x] Add black
  - [x] Add ruff
  - [x] Add mypy
  - [x] Add flake8
  - [x] Add pre-commit
  - [x] Add testcontainers
- [x] Task 4: Configure tool settings (AC: 4)
  - [x] Configure Black settings (line length, target version)
  - [x] Configure Ruff settings (line length, select rules, ignore patterns)
  - [x] Configure mypy settings (strict mode, Python version, ignore patterns)
- [x] Task 5: Verify dependency installation (AC: 5)
  - [x] Run `cd backend && uv sync`
  - [x] Verify all dependencies install successfully
  - [x] Verify `uv.lock` file is generated
  - [x] Check for version conflicts

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

gpt-4o

### Debug Log References

- Initial build error: README.md not found - resolved by removing readme field from pyproject.toml
- Build error: Unable to determine which files to ship - resolved by adding `[tool.hatch.build.targets.wheel]` with `packages = ["app"]`

### Completion Notes List

✅ **Story 1.4 Implementation Complete**

**Summary:**
- Created comprehensive `backend/pyproject.toml` with all required dependencies
- Configured project metadata, dependencies, dev dependencies, and tool settings
- Successfully installed all dependencies using `uv sync`
- Generated `uv.lock` file with locked dependency versions

**Acceptance Criteria Verification:**
- ✅ AC1: `pyproject.toml` contains project metadata (name: "agent-teacher-backend", version: "0.1.0", description, Python >=3.12, authors, license)
- ✅ AC2: Includes all required dependencies: FastAPI, SQLModel, pydantic-ai, Prefect, slowapi>=0.1.9, pydantic-settings, and all other dependencies from architecture.md
- ✅ AC3: Includes dev dependencies: pytest, pytest-asyncio, black, ruff, mypy, flake8, pre-commit, testcontainers
- ✅ AC4: Includes tool configurations for Black (line-length: 100, target-version: py312), Ruff (line-length: 100, select rules, ignore patterns), and mypy (Python 3.12, strict settings)
- ✅ AC5: Running `uv sync` installed all dependencies successfully and generated `uv.lock` file

**Implementation Details:**
- **Project Metadata:**
  - Name: "agent-teacher-backend"
  - Version: "0.1.0"
  - Description: "Backend API for agent-teacher: Autonomous learning platform with multi-agent AI"
  - Python requirement: ">=3.12"
  - Authors and license configured

- **Required Dependencies:**
  - Web framework: fastapi>=0.104.0, uvicorn[standard]>=0.24.0, python-multipart>=0.0.6, aiofiles>=23.2.0
  - Database: sqlmodel>=0.0.14, supabase>=2.0.0, alembic>=1.12.0
  - Configuration: python-dotenv>=1.0.0, pydantic-settings>=2.0.0
  - Authentication: python-jose[cryptography]>=3.3.0, passlib[bcrypt]>=1.7.4
  - Agent framework: pydantic-ai>=0.0.1, prefect>=2.14.0
  - Message queue: pika>=1.3.0, aio-pika>=9.0.0, redis>=5.0.0
  - Rate limiting: slowapi>=0.1.9
  - HTTP client: httpx>=0.25.0

- **Dev Dependencies:**
  - Testing: pytest>=7.4.0, pytest-asyncio>=0.21.0, testcontainers>=4.0.0
  - Code quality: black>=23.11.0, ruff>=0.1.0, mypy>=1.7.0, flake8>=6.1.0, pre-commit>=3.5.0

- **Tool Configurations:**
  - **Black**: line-length=100, target-version=py312, exclude migrations
  - **Ruff**: line-length=100, target-version=py312, select rules (E, W, F, I, B, C4, UP), ignore patterns, exclude migrations
  - **mypy**: python_version=3.12, strict settings enabled, exclude migrations

- **Build Configuration:**
  - Build system: hatchling
  - Package location: `app` directory
  - Successfully built and installed as editable package

- **Dependency Installation:**
  - All 218 packages installed successfully
  - No version conflicts detected
  - `uv.lock` file generated successfully

**Testing:**
- No tests required for this configuration story (as per Dev Notes)
- Verified `uv sync` completes successfully
- Verified `uv.lock` file is generated
- Verified all dependencies are accessible

### File List

- `backend/pyproject.toml` (created)
- `backend/uv.lock` (generated by uv sync)
