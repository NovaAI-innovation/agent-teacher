# Story 1.14: Configure Frontend Dependencies and Environment

Status: ready-for-dev

## Story

As a developer,
I want frontend dependencies installed and environment configuration set up,
so that the frontend can communicate with the backend.

## Acceptance Criteria

1. **Given** Next.js is initialized **When** I install additional dependencies and configure environment **Then** `frontend/package.json` includes axios, @tanstack/react-query, and zustand (if needed)
2. **Given** Next.js is initialized **When** I install additional dependencies and configure environment **Then** Running `npm install` installs all dependencies and generates `package-lock.json`
3. **Given** Next.js is initialized **When** I install additional dependencies and configure environment **Then** `frontend/.env.local.example` exists with NEXT_PUBLIC_API_URL documented
4. **Given** Next.js is initialized **When** I install additional dependencies and configure environment **Then** `frontend/.env.local` exists (gitignored) with NEXT_PUBLIC_API_URL=http://localhost:8000
5. **Given** Next.js is initialized **When** I install additional dependencies and configure environment **Then** Environment variables are accessible in the frontend application

## Tasks / Subtasks

- [ ] Task 1: Install additional dependencies (AC: 1, 2)
  - [ ] Run `npm install axios @tanstack/react-query zustand` (or add to package.json and run npm install)
  - [ ] Verify dependencies are added to `frontend/package.json`
  - [ ] Run `npm install` to install all dependencies
  - [ ] Verify `package-lock.json` is generated
  - [ ] Verify no installation errors
- [ ] Task 2: Create environment variable templates (AC: 3)
  - [ ] Create `frontend/.env.local.example`
  - [ ] Add NEXT_PUBLIC_API_URL with description: "Backend API URL (default: http://localhost:8000)"
  - [ ] Document other environment variables if needed
- [ ] Task 3: Create local environment file (AC: 4)
  - [ ] Create `frontend/.env.local` (should be in .gitignore)
  - [ ] Add NEXT_PUBLIC_API_URL=http://localhost:8000
  - [ ] Verify .env.local is in .gitignore
- [ ] Task 4: Verify environment variables are accessible (AC: 5)
  - [ ] Create a test component or page that reads NEXT_PUBLIC_API_URL
  - [ ] Verify environment variable is accessible: `process.env.NEXT_PUBLIC_API_URL`
  - [ ] Test in development mode

## Dev Notes

- **Architecture Patterns**: Axios for HTTP client, React Query for data fetching/caching, Zustand for state management (if needed).
- **Source Tree Components**:
  - `frontend/package.json` - Updated with additional dependencies
  - `frontend/.env.local.example` - Environment variable template
  - `frontend/.env.local` - Local environment variables (gitignored)
- **Testing Standards**: No tests required (configuration only), but environment variable access should be tested manually
- **Dependencies**: Story 1.13 must be complete (Next.js initialized)
- **Environment Variables**: Next.js requires NEXT_PUBLIC_ prefix for client-side accessible variables

### Project Structure Notes

- **Alignment**: Dependencies match architecture.md frontend stack. Environment configuration follows Next.js patterns.
- **State Management**: Zustand is optional - only add if needed for global state. React Query handles server state.
- **Environment Files**: .env.local is gitignored, .env.local.example is committed for documentation
- **No Conflicts**: Greenfield setup, no existing dependencies to conflict with

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Frontend Dependencies] - Frontend dependency list
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 13] - Task 13: Configure frontend dependencies and environment
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.14] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
