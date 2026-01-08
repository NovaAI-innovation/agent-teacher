# Story 1.19: Create Development Utility Scripts

Status: ready-for-dev

## Story

As a developer,
I want setup and development scripts,
so that I can quickly initialize and start the development environment.

## Acceptance Criteria

1. **Given** Project structure is complete **When** I create utility scripts **Then** `scripts/setup.sh` exists and initializes project (installs dependencies, sets up environment)
2. **Given** Project structure is complete **When** I create utility scripts **Then** `scripts/start-dev.sh` exists and starts development environment (docker-compose up)
3. **Given** Project structure is complete **When** I create utility scripts **Then** `scripts/stop-dev.sh` exists and stops development environment
4. **Given** Project structure is complete **When** I create utility scripts **Then** Scripts are executable and include error handling
5. **Given** Project structure is complete **When** I create utility scripts **Then** Running `./scripts/setup.sh` executes without errors
6. **Given** Project structure is complete **When** I create utility scripts **Then** Scripts provide clear output and error messages

## Tasks / Subtasks

- [ ] Task 1: Create setup script (AC: 1, 4, 5, 6)
  - [ ] Create `scripts/setup.sh`
  - [ ] Add shebang: `#!/bin/bash`
  - [ ] Add error handling: `set -e` or proper error checking
  - [ ] Install backend dependencies: `cd backend && uv sync`
  - [ ] Install frontend dependencies: `cd frontend && npm install`
  - [ ] Copy environment files: `.env.example` to `.env` (with prompts or instructions)
  - [ ] Set up pre-commit hooks: `cd backend && uv run pre-commit install`
  - [ ] Provide clear output messages for each step
  - [ ] Make script executable: `chmod +x scripts/setup.sh`
- [ ] Task 2: Create start-dev script (AC: 2, 4, 6)
  - [ ] Create `scripts/start-dev.sh`
  - [ ] Add shebang: `#!/bin/bash`
  - [ ] Add error handling
  - [ ] Start Docker Compose: `docker-compose up -d`
  - [ ] Wait for services to be healthy
  - [ ] Display service URLs and status
  - [ ] Provide clear output messages
  - [ ] Make script executable: `chmod +x scripts/start-dev.sh`
- [ ] Task 3: Create stop-dev script (AC: 3, 4, 6)
  - [ ] Create `scripts/stop-dev.sh`
  - [ ] Add shebang: `#!/bin/bash`
  - [ ] Add error handling
  - [ ] Stop Docker Compose: `docker-compose down`
  - [ ] Provide clear output messages
  - [ ] Make script executable: `chmod +x scripts/stop-dev.sh`
- [ ] Task 4: Test scripts (AC: 5, 6)
  - [ ] Test `./scripts/setup.sh` (or `bash scripts/setup.sh` on Windows)
  - [ ] Verify script executes without errors
  - [ ] Verify clear output messages
  - [ ] Test `./scripts/start-dev.sh`
  - [ ] Test `./scripts/stop-dev.sh`

## Dev Notes

- **Architecture Patterns**: Utility scripts for common development tasks. Bash scripts for cross-platform compatibility (or PowerShell for Windows).
- **Source Tree Components**: 
  - `scripts/setup.sh` - Project setup script
  - `scripts/start-dev.sh` - Start development environment script
  - `scripts/stop-dev.sh` - Stop development environment script
- **Testing Standards**: No automated tests required, but scripts should be tested manually
- **Dependencies**: Story 1.18 must be complete (Docker Compose configured), Story 1.4 must be complete (dependencies configured)
- **Cross-Platform**: Consider Windows compatibility (PowerShell scripts or WSL for bash scripts)

### Project Structure Notes

- **Alignment**: Scripts follow architecture.md development workflow patterns
- **Error Handling**: Scripts should handle errors gracefully and provide helpful messages
- **Executable**: Scripts should be executable (chmod +x) or runnable via bash/powershell
- **Documentation**: Scripts should have clear output explaining what they're doing
- **No Conflicts**: Greenfield setup, no existing scripts

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Development Workflow] - Development scripts and workflow
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 18] - Task 18: Create development utility scripts
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.19] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

