# Story 1.12: Set Up Backend Development Tooling

Status: review

## Story

As a developer,
I want pre-commit hooks, linting, and type checking configured,
so that code quality is enforced automatically.

## Acceptance Criteria

1. **Given** Backend dependencies are installed **When** I configure code quality tools **Then** `backend/.pre-commit-config.yaml` exists with hooks for Black, Ruff, mypy, and Flake8
2. **Given** Backend dependencies are installed **When** I configure code quality tools **Then** Hooks are configured to run on Python files and exclude migrations directory
3. **Given** Backend dependencies are installed **When** I configure code quality tools **Then** Running `uv run pre-commit install` installs hooks successfully
4. **Given** Backend dependencies are installed **When** I configure code quality tools **Then** Running `uv run pre-commit run --all-files` executes all hooks
5. **Given** Backend dependencies are installed **When** I configure code quality tools **Then** Code quality checks pass on the initial codebase

## Tasks / Subtasks

- [x] Task 1: Create pre-commit configuration (AC: 1, 2)
  - [x] Create `backend/.pre-commit-config.yaml`
  - [x] Add Black hook for code formatting
  - [x] Add Ruff hook for linting
  - [x] Add mypy hook for type checking
  - [x] Add Flake8 hook for additional linting
  - [x] Configure hooks to run on `*.py` files
  - [x] Exclude `migrations/` directory from hooks
  - [x] Configure hook execution order
- [x] Task 2: Install pre-commit hooks (AC: 3)
  - [x] Run `cd backend && uv run pre-commit install`
  - [x] Verify hooks are installed in `.git/hooks/`
  - [x] Verify installation completes without errors
- [x] Task 3: Test pre-commit hooks (AC: 4, 5)
  - [x] Run `cd backend && uv run pre-commit run --all-files`
  - [x] Verify all hooks execute successfully
  - [x] Fix any issues found by hooks
  - [x] Verify code quality checks pass
  - [x] Test hooks run on commit (make a test commit)

## Dev Notes

- **Architecture Patterns**: Pre-commit hooks for automated code quality enforcement. Multiple tools for comprehensive code quality.
- **Source Tree Components**:
  - `backend/.pre-commit-config.yaml` - Pre-commit hooks configuration
- **Testing Standards**: No tests required (tooling setup), but hooks should be tested manually
- **Dependencies**: Story 1.4 must be complete (pre-commit, black, ruff, mypy, flake8 dependencies installed)
- **Hook Configuration**: Hooks should run in correct order (formatting first, then linting, then type checking)

### Project Structure Notes

- **Alignment**: Pre-commit configuration follows best practices. Excludes migrations directory from formatting/linting.
- **Tool Configuration**: Black, Ruff, mypy, and Flake8 should be configured in pyproject.toml (from Story 1.4)
- **Git Hooks**: Pre-commit hooks are installed in `.git/hooks/` directory
- **No Conflicts**: Greenfield setup, no existing pre-commit configuration

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Code Quality] - Code quality tools and configuration
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 11] - Task 11: Set up backend development tooling
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.12] - Original story definition

## Dev Agent Record

### Agent Model Used

Claude Sonnet 4.5 (Auto)

### Debug Log References

N/A - No errors encountered during implementation

### Completion Notes List

1. **Pre-commit Configuration**: Pre-commit config file already existed with all required hooks (Black, Ruff, mypy, Flake8) properly configured
2. **Hook Installation**: Successfully installed pre-commit hooks using `uv run pre-commit install` - hooks installed at `.git/hooks/pre-commit`
3. **Hook Execution**: All hooks pass successfully on the entire codebase:
   - General file checks (trailing whitespace, end-of-file-fixer, YAML/JSON/TOML validation)
   - Black code formatting
   - Ruff linting and formatting
   - Flake8 additional linting
   - mypy type checking
4. **Code Quality Fixes**: Fixed two issues found during initial hook run:
   - Fixed long line in `backend/app/models/database.py` (line 29, exceeded 100 characters)
   - Fixed YAML syntax in `_bmad-output/implementation-artifacts/sprint-status.yaml` (quoted string value with curly braces)
5. **Hook Configuration**: All hooks properly exclude `migrations/` directory and run in correct order (formatting → linting → type checking)
6. **Verification**: All acceptance criteria met - hooks installed, configured correctly, and all checks pass on the codebase

### File List

- `backend/.pre-commit-config.yaml` - Pre-commit hooks configuration (existed, verified complete)
- `backend/app/models/database.py` - Fixed long line to comply with 100 character limit
- `_bmad-output/implementation-artifacts/sprint-status.yaml` - Fixed YAML syntax issue (quoted string value)
