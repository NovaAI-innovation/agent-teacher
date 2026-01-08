# Story 1.20: Configure CI/CD Pipelines

Status: ready-for-dev

## Story

As a developer,
I want GitHub Actions workflows for backend and frontend CI,
so that code quality checks run automatically.

## Acceptance Criteria

1. **Given** Project structure is set up **When** I create CI/CD workflows **Then** `.github/workflows/ci-backend.yml` exists with backend CI pipeline (lint with Ruff/Black, type-check with mypy, test with pytest)
2. **Given** Project structure is set up **When** I create CI/CD workflows **Then** `.github/workflows/ci-frontend.yml` exists with frontend CI pipeline (lint with ESLint, type-check with TypeScript, test)
3. **Given** Project structure is set up **When** I create CI/CD workflows **Then** `.github/workflows/deploy.yml` exists as deployment pipeline placeholder
4. **Given** Project structure is set up **When** I create CI/CD workflows **Then** CI workflows run on push to main and pull requests
5. **Given** Project structure is set up **When** I create CI/CD workflows **Then** Workflows are syntactically valid and can be manually triggered
6. **Given** Project structure is set up **When** I create CI/CD workflows **Then** Workflow files follow GitHub Actions best practices

## Tasks / Subtasks

- [ ] Task 1: Create backend CI workflow (AC: 1, 4, 5, 6)
  - [ ] Create `.github/workflows/ci-backend.yml`
  - [ ] Configure workflow to run on push to main and pull requests
  - [ ] Set up Python environment (Python 3.12)
  - [ ] Install uv package manager
  - [ ] Install dependencies: `uv sync`
  - [ ] Add lint step: Run Ruff and Black
  - [ ] Add type-check step: Run mypy
  - [ ] Add test step: Run pytest
  - [ ] Configure job dependencies and caching
  - [ ] Add workflow name and description
- [ ] Task 2: Create frontend CI workflow (AC: 2, 4, 5, 6)
  - [ ] Create `.github/workflows/ci-frontend.yml`
  - [ ] Configure workflow to run on push to main and pull requests
  - [ ] Set up Node.js environment (Node.js 18+)
  - [ ] Install dependencies: `npm ci`
  - [ ] Add lint step: Run ESLint
  - [ ] Add type-check step: Run TypeScript compiler
  - [ ] Add test step: Run tests (if configured)
  - [ ] Configure job dependencies and caching
  - [ ] Add workflow name and description
- [ ] Task 3: Create deployment workflow placeholder (AC: 3, 5, 6)
  - [ ] Create `.github/workflows/deploy.yml`
  - [ ] Add basic workflow structure
  - [ ] Add placeholder jobs for deployment
  - [ ] Configure to run on push to main (or manual trigger)
  - [ ] Add workflow name and description
- [ ] Task 4: Verify workflows (AC: 5, 6)
  - [ ] Validate YAML syntax (can use online validator or GitHub)
  - [ ] Verify workflows follow GitHub Actions best practices
  - [ ] Test manual workflow trigger (if possible)
  - [ ] Verify workflow files are properly formatted

## Dev Notes

- **Architecture Patterns**: GitHub Actions for CI/CD. Separate workflows for backend and frontend. Caching for faster builds.
- **Source Tree Components**: 
  - `.github/workflows/ci-backend.yml` - Backend CI pipeline
  - `.github/workflows/ci-frontend.yml` - Frontend CI pipeline
  - `.github/workflows/deploy.yml` - Deployment pipeline placeholder
- **Testing Standards**: No tests required (workflow configuration), but workflows should be tested by pushing to GitHub
- **Dependencies**: Story 1.4 must be complete (backend dependencies), Story 1.13 must be complete (frontend dependencies)
- **CI Strategy**: Run linting, type-checking, and tests on every push and PR. Fast feedback for developers.

### Project Structure Notes

- **Alignment**: CI/CD workflows follow architecture.md CI/CD patterns and GitHub Actions best practices
- **Caching**: Use GitHub Actions caching for dependencies to speed up workflows
- **Parallel Jobs**: Backend and frontend CI can run in parallel
- **Deployment**: Deployment workflow is placeholder, full implementation in deployment stories
- **No Conflicts**: Greenfield setup, no existing workflows

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#CI/CD] - CI/CD pipeline patterns
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 19] - Task 19: Configure CI/CD pipelines
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.20] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

