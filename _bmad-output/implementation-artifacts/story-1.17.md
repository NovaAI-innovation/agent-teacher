# Story 1.17: Configure Frontend Code Quality and Testing Tools

Status: completed

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

- [x] Task 1: Configure ESLint (AC: 1, 6)
  - [x] Verify `frontend/eslint.config.mjs` exists (Next.js 16 uses flat config, not .eslintrc.json)
  - [x] Configure Next.js ESLint rules
  - [x] Configure TypeScript ESLint rules
  - [x] Add any custom rules as needed
  - [x] Test running `npm run lint`
  - [x] Verify ESLint executes successfully
- [x] Task 2: Configure Prettier (AC: 2, 3)
  - [x] Create `frontend/.prettierrc`
  - [x] Configure Prettier formatting rules (printWidth, tabWidth, semi, singleQuote, etc.)
  - [x] Create `.prettierignore` if needed
  - [x] Install prettier if not already installed
  - [x] Configure ESLint to work with Prettier (eslint-config-prettier)
  - [x] Test Prettier formatting
- [x] Task 3: Install and configure Playwright (AC: 4, 7)
  - [x] Install Playwright: `npm install -D @playwright/test` (already installed)
  - [x] Run `npx playwright install` to install browsers
  - [x] Create `frontend/tests/e2e/playwright.config.ts`
  - [x] Configure Playwright with base URL, test directory, etc.
  - [x] Add Playwright scripts to package.json
- [x] Task 4: Create test directory structure (AC: 5)
  - [x] Create `frontend/tests/__mocks__/` directory
  - [x] Create `frontend/tests/components/` directory
  - [x] Create `frontend/tests/lib/` directory
  - [x] Create `frontend/tests/e2e/` directory (if not created by Playwright)
- [x] Task 5: Verify configuration (AC: 3, 6, 7)
  - [x] Test ESLint: `npm run lint`
  - [x] Test Prettier: `npm run format:check`
  - [x] Verify no conflicts between ESLint and Prettier
  - [x] Test Playwright: `npx playwright test --list` (works, no tests yet)

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

Auto (Cursor AI)

### Debug Log References

N/A - No errors encountered during configuration

### Completion Notes List

- Updated `frontend/eslint.config.mjs` to integrate with Prettier using eslint-config-prettier
- Created `frontend/.prettierrc` with consistent formatting rules
- Created `frontend/.prettierignore` to exclude build artifacts and dependencies
- Created `frontend/tests/e2e/playwright.config.ts` with full Playwright configuration
- Created all test directories: `tests/__mocks__/`, `tests/components/`, `tests/lib/`, `tests/e2e/`
- Updated `package.json` scripts: added `lint:fix`, `format`, `format:check`, `test:e2e`, `test:e2e:ui`, `test:e2e:headed`
- Installed Playwright browsers (chromium)
- ESLint runs successfully (detects some existing code issues that need separate fixes)
- Prettier runs successfully (detects formatting issues in existing files)
- Playwright configuration verified and ready for E2E tests
- Note: Next.js 16 uses `eslint.config.mjs` (flat config) instead of `.eslintrc.json`

### File List

- `frontend/eslint.config.mjs` - Updated with Prettier integration
- `frontend/.prettierrc` - Created Prettier configuration
- `frontend/.prettierignore` - Created Prettier ignore file
- `frontend/tests/e2e/playwright.config.ts` - Created Playwright configuration
- `frontend/package.json` - Updated with new scripts
- `frontend/tests/__mocks__/` - Created directory
- `frontend/tests/components/` - Created directory
- `frontend/tests/lib/` - Created directory
- `frontend/tests/e2e/` - Created directory (contains playwright.config.ts)
