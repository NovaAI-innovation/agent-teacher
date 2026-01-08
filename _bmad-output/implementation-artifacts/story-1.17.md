# Story 1.17: Configure Frontend Code Quality and Testing Tools

Status: ready-for-dev

## Story

As a developer,
I want ESLint, Prettier, and Playwright configured,
so that frontend code quality and E2E testing are set up.

## Acceptance Criteria

1. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** `frontend/.eslintrc.json` exists with Next.js and TypeScript rules configured
2. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** `frontend/.prettierrc` exists with consistent formatting rules
3. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** ESLint and Prettier work together without conflicts
4. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** `frontend/tests/e2e/playwright.config.ts` exists with Playwright configuration
5. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** Test directory structure exists: `tests/__mocks__/`, `tests/components/`, `tests/lib/`, `tests/e2e/`
6. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** Running `npm run lint` executes ESLint successfully
7. **Given** Frontend structure is created **When** I configure code quality and testing tools **Then** Playwright configuration is ready for E2E tests

## Tasks / Subtasks

- [ ] Task 1: Configure ESLint (AC: 1, 6)
  - [ ] Verify `frontend/.eslintrc.json` exists (may be created by Next.js)
  - [ ] Configure Next.js ESLint rules
  - [ ] Configure TypeScript ESLint rules
  - [ ] Add any custom rules as needed
  - [ ] Test running `npm run lint`
  - [ ] Verify ESLint executes successfully
- [ ] Task 2: Configure Prettier (AC: 2, 3)
  - [ ] Create `frontend/.prettierrc` (or .prettierrc.json)
  - [ ] Configure Prettier formatting rules (printWidth, tabWidth, semi, singleQuote, etc.)
  - [ ] Create `.prettierignore` if needed
  - [ ] Install prettier if not already installed
  - [ ] Configure ESLint to work with Prettier (eslint-config-prettier)
  - [ ] Test Prettier formatting
- [ ] Task 3: Install and configure Playwright (AC: 4, 7)
  - [ ] Install Playwright: `npm install -D @playwright/test`
  - [ ] Run `npx playwright install` to install browsers
  - [ ] Create `frontend/tests/e2e/playwright.config.ts`
  - [ ] Configure Playwright with base URL, test directory, etc.
  - [ ] Add Playwright scripts to package.json
- [ ] Task 4: Create test directory structure (AC: 5)
  - [ ] Create `frontend/tests/__mocks__/` directory
  - [ ] Create `frontend/tests/components/` directory
  - [ ] Create `frontend/tests/lib/` directory
  - [ ] Create `frontend/tests/e2e/` directory (if not created by Playwright)
- [ ] Task 5: Verify configuration (AC: 3, 6, 7)
  - [ ] Test ESLint: `npm run lint`
  - [ ] Test Prettier: `npm run format` (if script exists)
  - [ ] Verify no conflicts between ESLint and Prettier
  - [ ] Test Playwright: `npx playwright test` (should pass with no tests)

## Dev Notes

- **Architecture Patterns**: ESLint for linting, Prettier for formatting, Playwright for E2E testing. Standard Next.js tooling setup.
- **Source Tree Components**:
  - `frontend/.eslintrc.json` - ESLint configuration
  - `frontend/.prettierrc` - Prettier configuration
  - `frontend/tests/e2e/playwright.config.ts` - Playwright configuration
  - `frontend/tests/` - Test directories
- **Testing Standards**: Playwright for E2E tests. Unit tests can use Jest/React Testing Library (configured later if needed).
- **Dependencies**: Story 1.13 must be complete (Next.js initialized)
- **Tool Integration**: ESLint and Prettier should work together without conflicts (use eslint-config-prettier)

### Project Structure Notes

- **Alignment**: Code quality tools follow Next.js and architecture.md best practices
- **ESLint**: Next.js comes with ESLint configured, may need to extend with TypeScript rules
- **Prettier**: Should be integrated with ESLint to avoid conflicts
- **Playwright**: Modern E2E testing tool, better than Cypress for Next.js
- **No Conflicts**: Greenfield setup, Next.js may create initial ESLint config

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Frontend Testing] - Testing tools and configuration
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 16] - Task 16: Configure frontend code quality and testing tools
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.17] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
