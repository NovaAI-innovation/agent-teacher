# Story 1.12: Set Up Backend Development Tooling

Status: ready-for-dev

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

- [ ] Task 1: Create pre-commit configuration (AC: 1, 2)
  - [ ] Create `backend/.pre-commit-config.yaml`
  - [ ] Add Black hook for code formatting
  - [ ] Add Ruff hook for linting
  - [ ] Add mypy hook for type checking
  - [ ] Add Flake8 hook for additional linting
  - [ ] Configure hooks to run on `*.py` files
  - [ ] Exclude `migrations/` directory from hooks
  - [ ] Configure hook execution order
- [ ] Task 2: Install pre-commit hooks (AC: 3)
  - [ ] Run `cd backend && uv run pre-commit install`
  - [ ] Verify hooks are installed in `.git/hooks/`
  - [ ] Verify installation completes without errors
- [ ] Task 3: Test pre-commit hooks (AC: 4, 5)
  - [ ] Run `cd backend && uv run pre-commit run --all-files`
  - [ ] Verify all hooks execute successfully
  - [ ] Fix any issues found by hooks
  - [ ] Verify code quality checks pass
  - [ ] Test hooks run on commit (make a test commit)

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

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

