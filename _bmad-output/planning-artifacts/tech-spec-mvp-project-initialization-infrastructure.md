---
title: 'MVP Project Initialization and Infrastructure Setup'
slug: 'mvp-project-initialization-infrastructure'
created: '2026-01-07T21:31:15.924Z'
status: 'ready-for-dev'
stepsCompleted: [1, 2, 3, 4]
tech_stack: ['FastAPI', 'Next.js', 'TypeScript', 'Python 3.12+', 'PostgreSQL (Supabase)', 'Redis', 'RabbitMQ', 'Docker', 'uv', 'npm', 'pytest', 'Playwright', 'Alembic', 'SQLModel', 'pydantic-ai', 'Prefect', 'Tailwind CSS', 'React Query']
files_to_modify: []
code_patterns: ['FastAPI router pattern', 'Next.js App Router', 'SQLModel ORM', 'pydantic-ai agents', 'Prefect workflows', 'Server/Client Components', 'API versioning (/api/v1/)', 'Environment-based configuration']
test_patterns: ['pytest with async support', 'Testcontainers for integration tests', 'Playwright for E2E', 'Co-located unit tests', 'Separate integration/E2E directories']
---

# Tech-Spec: MVP Project Initialization and Infrastructure Setup

**Created:** 2026-01-07T21:31:15.924Z

## Overview

### Problem Statement

The agent-teacher project (MENTOR-web) requires a complete project scaffold and infrastructure setup for MVP development. Currently, the project exists only as planning artifacts (PRD, Architecture, UX Design) with no codebase. We need to establish the foundational structure, development environment, and tooling to enable implementation of the multi-agent learning platform with FastAPI backend and Next.js frontend.

### Solution

Create a complete project initialization that includes:
1. Full directory structure matching the architecture specification
2. Backend initialization with FastAPI, all dependencies via `uv`, and project configuration
3. Frontend initialization with Next.js (TypeScript, Tailwind CSS) via `npm`
4. Docker Compose setup for local development (backend, frontend, Redis, RabbitMQ)
5. Database migration structure with Alembic
6. Testing infrastructure setup (pytest for backend, Playwright for E2E)
7. Development tooling (pre-commit hooks, linting, type checking)
8. Environment configuration management
9. Basic CI/CD pipeline structure (GitHub Actions)
10. Git repository initialization with proper .gitignore

### Scope

**In Scope:**
- Complete directory structure creation (backend, frontend, infrastructure, scripts)
- Backend FastAPI application initialization with all core dependencies
- Frontend Next.js application initialization with TypeScript and Tailwind CSS
- Docker Compose configuration for local development environment
- Database migration structure (Alembic) with initial setup
- Testing framework setup (pytest, Playwright, testcontainers)
- Development tooling configuration (pre-commit, Black, Ruff, mypy, ESLint, Prettier)
- Environment variable templates (.env.example files)
- Basic CI/CD pipeline structure (GitHub Actions workflows)
- Git repository initialization
- Project documentation (README files)
- Package manager configuration (uv for backend, npm for frontend)

**Out of Scope:**
- Actual feature implementation (agents, workflows, business logic)
- Production deployment configuration (focus on local development)
- Advanced monitoring setup (basic logging only)
- mem0 integration (deferred to post-MVP per architecture)
- API gateway setup (Kong/Apache APISIX - deferred)
- Production secrets management (environment variables sufficient for MVP)

## Context for Development

### Codebase Patterns

**Confirmed Clean Slate:** No existing codebase - this is a greenfield project. All patterns will be established during initialization based on the architecture document.

**Backend Patterns:**
- **FastAPI Router Pattern**: Versioned API routes (`/api/v1/`) with separate router files per domain (auth, courses, learning, etc.)
- **Service Layer**: Business logic in `app/services/` with clear separation from API routes
- **SQLModel ORM**: Database models in `app/models/` using SQLModel (extends Pydantic)
- **Agent Architecture**: pydantic-ai agents in `app/services/agents/` and standalone `agents/` directory
- **Orchestration**: Prefect workflows in `orchestration/workflows/` with tasks in `orchestration/tasks/`
- **Configuration**: pydantic-settings for environment-based configuration
- **Naming Conventions**: snake_case for Python files and functions, PascalCase for classes

**Frontend Patterns:**
- **Next.js App Router**: File-based routing with Server Components (default) and Client Components (when needed)
- **Component Organization**: Feature-based component organization (`components/course/`, `components/learning/`, etc.)
- **API Client**: Centralized API client in `lib/api/` with Axios and React Query for data fetching
- **Type Safety**: TypeScript throughout with shared types between frontend and backend
- **Styling**: Tailwind CSS utility-first approach
- **Naming Conventions**: camelCase for variables/functions, PascalCase for components/types

**Project Structure:**
- **Separation**: Clear separation between `backend/` and `frontend/` folders
- **API Communication**: Frontend makes HTTP requests to backend API (no direct database access)
- **WebSocket**: Real-time tutoring via WebSocket (FastAPI native support)
- **Testing**: Co-located unit tests, separate `tests/integration/` and `tests/e2e/` directories
- **Migrations**: Alembic for database schema versioning in `backend/migrations/`

### Files to Reference

| File | Purpose |
| ---- | ------- |
| `_bmad-output/planning-artifacts/architecture.md` | Complete project structure (lines 2033-2486), technology stack, initialization commands (lines 469-518), dependency lists |
| `_bmad-output/planning-artifacts/prd.md` | MVP scope and requirements, functional requirements mapping |
| `_bmad-output/planning-artifacts/ux-design-specification.md` | Frontend structure, component organization, routing patterns |

**Key Architecture Sections:**
- **Project Structure**: Lines 2033-2486 (complete directory tree)
- **Initialization Commands**: Lines 469-518 (exact dependency installation commands)
- **Technology Stack**: Lines 390-449 (confirmed technology decisions)
- **Testing Strategy**: Lines 269-291 (testing framework and patterns)

### Technical Decisions

**Package Managers:**
- Backend: `uv` for Python dependency management (faster than pip, better lock files)
- Frontend: `npm` for Node.js dependencies (standard, widely supported)

**Project Structure:**
- Separate `backend/` and `frontend/` folders for clear separation
- Backend uses FastAPI router pattern with versioned API (`/api/v1/`)
- Frontend uses Next.js App Router with file-based routing

**Local Development:**
- Docker Compose for orchestrating all services (backend, frontend, Redis, RabbitMQ)
- Hot reloading enabled for both backend (Uvicorn) and frontend (Next.js)
- Environment variables via `.env` files (gitignored, `.env.example` as template)

**Testing:**
- pytest for backend unit and integration tests
- Playwright for end-to-end testing
- Testcontainers for integration testing with real dependencies

**Code Quality:**
- Pre-commit hooks for automated quality checks (`.pre-commit-config.yaml` in backend)
- Backend: Black (formatting), Ruff (linting), mypy (type checking), Flake8 (additional linting)
- Frontend: ESLint (linting), Prettier (formatting), TypeScript (type checking)

**Files to Create (Summary):**
- **Root Level**: `.gitignore`, `.env.example`, `docker-compose.yml`, `README.md`, `.github/workflows/` (3 CI/CD files)
- **Backend**: Complete `backend/` structure with ~100+ files including:
  - `pyproject.toml`, `uv.lock`, `.env.example`, `.pre-commit-config.yaml`, `Dockerfile`
  - `app/` package with API routes, services, models, middleware, utils
  - `agents/`, `orchestration/`, `migrations/`, `tests/`, `scripts/` directories
- **Frontend**: Complete `frontend/` structure with ~150+ files including:
  - `package.json`, `package-lock.json`, `tsconfig.json`, `next.config.js`, `tailwind.config.js`, `.eslintrc.json`, `.prettierrc`, `Dockerfile`
  - `app/` directory with Next.js App Router structure (routes, layouts, pages)
  - `components/`, `lib/`, `public/`, `styles/`, `tests/` directories
- **Infrastructure**: `infrastructure/docker/`, `infrastructure/kubernetes/`, `infrastructure/monitoring/`
- **Scripts**: Root-level utility scripts (`setup.sh`, `start-dev.sh`, etc.)

## Implementation Plan

### Tasks

- [ ] Task 1: Initialize Git repository and root-level configuration
  - File: `.gitignore`
  - Action: Create comprehensive .gitignore for Python, Node.js, Docker, IDE files, environment variables
  - Notes: Include patterns for `__pycache__/`, `*.pyc`, `node_modules/`, `.env`, `.env.local`, `.venv/`, `dist/`, `.next/`, `uv.lock`, `package-lock.json` (keep lock files but ignore local env files)

- [ ] Task 2: Create root-level README and environment template
  - File: `README.md`
  - Action: Create project overview with setup instructions, architecture summary, and development workflow
  - File: `.env.example`
  - Action: Create root-level environment variable template with all required variables (APP_NAME, ENVIRONMENT, DEBUG, SECRET_KEY, database URLs, API keys placeholders)
  - Notes: Reference architecture.md lines 766-809 for complete environment variable list

- [ ] Task 3: Create complete backend directory structure
  - Files: Create all directories as specified in architecture.md lines 2060-2218
  - Action: Create directory tree: `backend/app/{api/v1,services/{agents,orchestration,knowledge},models,middleware,utils}`, `backend/agents/`, `backend/orchestration/{workflows,tasks}`, `backend/migrations/versions/`, `backend/tests/{unit,integration,e2e}`, `backend/scripts/`
  - Notes: Create all `__init__.py` files for Python packages

- [ ] Task 4: Create backend pyproject.toml with all dependencies
  - File: `backend/pyproject.toml`
  - Action: Create pyproject.toml with project metadata, dependencies (FastAPI, SQLModel, pydantic-ai, Prefect, slowapi, etc.), dev dependencies (pytest, black, ruff, mypy, etc.), and tool configurations (Black, Ruff, mypy)
  - Notes: Reference architecture.md lines 711-764 for exact dependency versions and tool configs. Add slowapi>=0.1.9 to dependencies list for rate limiting (architecture mentions it but it's not in the example pyproject.toml)

- [ ] Task 5: Create backend environment configuration
  - File: `backend/.env.example`
  - Action: Create backend-specific environment variable template with database, API keys, service URLs
  - File: `backend/app/config.py`
  - Action: Create pydantic-settings configuration class with all environment variables
  - Notes: Use BaseSettings from pydantic-settings, include validation and default values, reference architecture.md lines 817-873 for complete Settings class structure

- [ ] Task 5a: Create database connection setup
  - File: `backend/app/models/database.py`
  - Action: Create SQLModel database engine and session management (create_engine, get_session dependency)
  - Notes: Initialize SQLModel engine with Supabase connection string from config, create async session factory for FastAPI dependency injection

- [ ] Task 5b: Create service client initializations
  - File: `backend/app/services/knowledge/supabase_client.py`
  - Action: Create Supabase client wrapper with connection initialization
  - File: `backend/app/utils/redis_client.py`
  - Action: Create Redis client connection utility with connection pooling
  - File: `backend/app/utils/rabbitmq_client.py`
  - Action: Create RabbitMQ connection utility with channel management
  - Notes: These are connection utilities, full implementations deferred to feature work

- [ ] Task 6: Create FastAPI application entry point
  - File: `backend/app/main.py`
  - Action: Create FastAPI app instance with CORS middleware, API router registration, health check endpoint, OpenAPI documentation configuration
  - File: `backend/app/__init__.py`
  - Action: Create empty __init__.py for app package
  - Notes: Include middleware setup, router mounting at `/api/v1`, basic error handling, lifespan context manager for startup/shutdown, reference architecture.md lines 875-920 for main.py structure

- [ ] Task 6a: Create health check endpoint
  - File: `backend/app/api/v1/health.py`
  - Action: Create health check router with `/health` endpoint that checks database, Redis, RabbitMQ connectivity
  - Notes: Return 200 OK with service status (database: connected, redis: connected, rabbitmq: connected)

- [ ] Task 6b: Create WebSocket endpoint structure
  - File: `backend/app/api/v1/websocket.py`
  - Action: Create WebSocket router with placeholder endpoint for tutoring sessions
  - Notes: Basic WebSocket endpoint structure, full implementation deferred to tutoring feature

- [ ] Task 7: Create API router structure
  - Files: `backend/app/api/__init__.py`, `backend/app/api/v1/__init__.py`
  - Action: Create API package structure with versioned router placeholder files (auth.py, courses.py, learning.py, tutoring.py, assessments.py, progress.py, admin.py)
  - Notes: Each router file should have basic FastAPI router instance, full implementation deferred to feature work

- [ ] Task 8: Create service layer structure
  - Files: Create `backend/app/services/__init__.py` and subdirectories with `__init__.py` files
  - Action: Create service package structure: `services/agents/`, `services/orchestration/`, `services/knowledge/` with placeholder __init__.py files
  - Notes: Service implementations deferred to feature work

- [ ] Task 9: Create models structure
  - File: `backend/app/models/__init__.py`
  - Action: Create models package with base model class
  - File: `backend/app/models/base.py`
  - Action: Create BaseModel with common fields (id, created_at, updated_at) using SQLModel
  - Notes: Individual model files (user.py, course.py, etc.) deferred to feature work

- [ ] Task 10: Create middleware structure
  - Files: `backend/app/middleware/__init__.py` and placeholder files
  - Action: Create middleware package with placeholder files: cors.py, security.py, rate_limiting.py, authentication.py, logging.py, error_handler.py
  - File: `backend/app/middleware/cors.py`
  - Action: Create CORS middleware configuration with frontend URLs from config, allow credentials, specific methods/headers
  - File: `backend/app/middleware/error_handler.py`
  - Action: Create global exception handler with standardized error response format (error_code, message, request_id, details)
  - File: `backend/app/middleware/logging.py`
  - Action: Create structured logging middleware with request/response logging, correlation IDs
  - File: `backend/app/middleware/rate_limiting.py`
  - Action: Create rate limiting middleware with slowapi, configure endpoint-specific limits (placeholder implementation)
  - File: `backend/app/middleware/security.py`
  - Action: Create security headers middleware (Content-Security-Policy, X-Frame-Options, HSTS, etc.)
  - Notes: CORS, error handler, and security headers should be functional (not just placeholders), logging and rate limiting should have basic structure

- [ ] Task 11: Create utilities structure
  - Files: `backend/app/utils/__init__.py` and placeholder files
  - Action: Create utils package with placeholder files: jwt.py, password.py, validators.py, formatters.py, logger.py, exceptions.py
  - File: `backend/app/utils/logger.py`
  - Action: Create structured logging configuration with JSON formatter, log levels, file/console handlers
  - File: `backend/app/utils/exceptions.py`
  - Action: Create custom exception classes (APIException, ValidationError, NotFoundError, etc.) with error codes
  - Notes: Logger and exceptions should be functional for initialization, other utilities deferred to feature work

- [ ] Task 12: Create dependencies module
  - File: `backend/app/dependencies.py`
  - Action: Create FastAPI dependencies module with placeholder functions (get_current_user, get_db, etc.)
  - Notes: Full implementation deferred to authentication feature

- [ ] Task 13: Create agents directory structure
  - Files: `backend/agents/__init__.py` and placeholder agent files
  - Action: Create agents package with placeholder files: curriculum_agent.py, content_agent.py, tutor_agent.py, qa_agent.py, optimizer_agent.py, health_monitor_agent.py
  - Notes: Agent implementations deferred to feature work

- [ ] Task 14: Create orchestration structure
  - Files: `backend/orchestration/__init__.py`, `backend/orchestration/workflows/__init__.py`, `backend/orchestration/tasks/__init__.py`
  - Action: Create orchestration package structure with placeholder workflow and task files
  - File: `backend/orchestration/prefect_config.py`
  - Action: Create Prefect client configuration and initialization (Prefect API URL, API key from config)
  - Notes: Prefect client setup should be functional, workflow implementations deferred to feature work

- [ ] Task 15: Initialize Alembic for database migrations
  - File: `backend/migrations/env.py`
  - Action: Create Alembic environment configuration with SQLModel integration, import all models for autogenerate
  - File: `backend/migrations/script.py.mako`
  - Action: Create Alembic migration template
  - File: `backend/migrations/alembic.ini`
  - Action: Create Alembic configuration file with database URL from environment
  - Notes: Run `alembic init migrations` then customize env.py for SQLModel, ensure it imports BaseModel and all model classes for autogenerate to work

- [ ] Task 16: Create backend testing infrastructure
  - File: `backend/tests/__init__.py`
  - Action: Create tests package
  - File: `backend/tests/conftest.py`
  - Action: Create pytest configuration with async support, test fixtures (test client, test database, mock services)
  - Files: Create test directory structure with `__init__.py` files in unit/, integration/, e2e/
  - Notes: Include pytest-asyncio configuration, Testcontainers setup for integration tests

- [ ] Task 17: Create backend scripts
  - File: `backend/scripts/init_db.py`
  - Action: Create database initialization script (create tables, seed initial data)
  - File: `backend/scripts/seed_data.py`
  - Action: Create data seeding script placeholder
  - File: `backend/scripts/reset_test_users.py`
  - Action: Create test user reset script placeholder
  - File: `backend/scripts/migrate_db.py`
  - Action: Create database migration helper script
  - Notes: Script implementations can be minimal placeholders for MVP initialization

- [ ] Task 18: Create backend Dockerfile
  - File: `backend/Dockerfile`
  - Action: Create multi-stage Dockerfile for FastAPI application with uv, Python 3.12, production dependencies
  - Notes: Include development and production stages, optimize for caching

- [ ] Task 19: Create backend pre-commit configuration
  - File: `backend/.pre-commit-config.yaml`
  - Action: Create pre-commit hooks configuration with Black, Ruff, mypy, Flake8 checks
  - Notes: Configure hooks to run on Python files, exclude migrations directory

- [ ] Task 20: Create backend README
  - File: `backend/README.md`
  - Action: Create backend-specific documentation with setup instructions, dependency installation, running locally, testing commands
  - Notes: Include commands for `uv sync`, `uv run uvicorn app.main:app --reload`, `uv run pytest`

- [ ] Task 21: Install backend dependencies
  - Action: Run `cd backend && uv sync` to install all dependencies and generate uv.lock
  - Notes: Verify all dependencies install successfully, check for version conflicts

- [ ] Task 22: Initialize frontend Next.js project
  - Action: Run `cd frontend && npx create-next-app@latest . --typescript --tailwind --app --no-src-dir --import-alias "@/*"`
  - Notes: This creates the base Next.js structure with App Router, TypeScript, Tailwind CSS

- [ ] Task 23: Install frontend additional dependencies
  - File: `frontend/package.json`
  - Action: Add dependencies: axios, @tanstack/react-query, zustand (if needed)
  - Action: Run `npm install` to install all dependencies
  - Notes: Verify package-lock.json is generated

- [ ] Task 24: Create frontend environment configuration
  - File: `frontend/.env.local.example`
  - Action: Create frontend environment variable template with NEXT_PUBLIC_API_URL
  - File: `frontend/.env.local`
  - Action: Create .env.local with NEXT_PUBLIC_API_URL=http://localhost:8000 (gitignored)
  - Notes: Use NEXT_PUBLIC_ prefix for client-accessible environment variables

- [ ] Task 25: Create frontend API client structure
  - Files: Create `frontend/lib/api/` directory structure
  - File: `frontend/lib/api/client.ts`
  - Action: Create Axios client configuration with base URL from NEXT_PUBLIC_API_URL, request/response interceptors, error handling, token management
  - File: `frontend/lib/api/endpoints.ts`
  - Action: Create API endpoint constants matching backend routes (/api/v1/auth, /api/v1/courses, etc.)
  - Files: Create placeholder API modules: auth.ts, courses.ts, learning.ts, assessments.ts, tutoring.ts, progress.ts, admin.ts
  - Notes: API client should have functional base configuration, individual endpoint implementations deferred to feature work

- [ ] Task 25a: Create frontend WebSocket client structure
  - File: `frontend/lib/websocket/client.ts`
  - Action: Create WebSocket client with connection management, reconnection logic, message handlers
  - File: `frontend/lib/websocket/handlers.ts`
  - Action: Create WebSocket message handler utilities
  - File: `frontend/lib/websocket/reconnect.ts`
  - Action: Create WebSocket reconnection logic with exponential backoff
  - Notes: WebSocket client structure should be ready, full implementation deferred to tutoring feature

- [ ] Task 26: Create frontend component directory structure
  - Files: Create `frontend/components/` with subdirectories: ui/, layout/, auth/, course/, learning/, assessment/, tutoring/, profile/, admin/
  - Action: Create directory structure with placeholder index files
  - Notes: Component implementations deferred to feature work

- [ ] Task 27: Create frontend lib utilities structure
  - Files: Create `frontend/lib/utils/`, `frontend/lib/hooks/`, `frontend/lib/types/`, `frontend/lib/websocket/` directories
  - Action: Create utility directory structure with placeholder files
  - Notes: Implementations deferred to feature work

- [ ] Task 28: Create frontend app router structure
  - Files: Create Next.js App Router structure: `app/layout.tsx`, `app/page.tsx`, `app/globals.css`
  - Action: Create root layout with basic HTML structure, homepage placeholder, global styles
  - File: `frontend/app/api/health/route.ts`
  - Action: Create Next.js API route for health check (proxies to backend or returns frontend status)
  - Notes: Route implementations deferred to feature work, but structure should be in place

- [ ] Task 28a: Configure Next.js for project needs
  - File: `frontend/next.config.js`
  - Action: Configure Next.js with API rewrites (proxy /api/* to backend), image domains, environment variables, TypeScript strict mode
  - File: `frontend/tsconfig.json`
  - Action: Verify/update TypeScript configuration for strict mode, path aliases (@/*), Next.js types
  - Notes: Ensure Next.js can communicate with backend API, TypeScript is properly configured

- [ ] Task 29: Configure frontend code quality tools
  - File: `frontend/.eslintrc.json`
  - Action: Configure ESLint with Next.js and TypeScript rules
  - File: `frontend/.prettierrc`
  - Action: Configure Prettier with consistent formatting rules
  - Notes: Ensure ESLint and Prettier work together without conflicts

- [ ] Task 30: Create frontend testing structure
  - Files: Create `frontend/tests/` directory with `__mocks__/`, `components/`, `lib/`, `e2e/` subdirectories
  - File: `frontend/tests/e2e/playwright.config.ts`
  - Action: Create Playwright configuration for E2E testing
  - Notes: Test implementations deferred, but structure should be ready

- [ ] Task 31: Create frontend Dockerfile
  - File: `frontend/Dockerfile`
  - Action: Create multi-stage Dockerfile for Next.js application with Node.js, build and production stages
  - Notes: Optimize for Next.js production build, include .next cache optimization

- [ ] Task 32: Create frontend README
  - File: `frontend/README.md`
  - Action: Create frontend-specific documentation with setup instructions, development commands, build process
  - Notes: Include commands for `npm install`, `npm run dev`, `npm run build`

- [ ] Task 33: Create Docker Compose configuration
  - File: `docker-compose.yml`
  - Action: Create Docker Compose file with services: backend (FastAPI), frontend (Next.js), redis, rabbitmq
  - Notes: Configure volumes for hot reloading, environment variables, networking, health checks, service dependencies, restart policies, port mappings (backend:8000, frontend:3000, redis:6379, rabbitmq:5672,15672)

- [ ] Task 34: Create infrastructure directory structure
  - Files: Create `infrastructure/docker/`, `infrastructure/kubernetes/`, `infrastructure/monitoring/` directories
  - Action: Create infrastructure directory structure with placeholder files
  - Notes: Full infrastructure configurations deferred to production deployment

- [ ] Task 35: Create root-level utility scripts
  - File: `scripts/setup.sh`
  - Action: Create setup script that initializes project (installs dependencies, sets up environment)
  - File: `scripts/start-dev.sh`
  - Action: Create script to start development environment (docker-compose up)
  - File: `scripts/stop-dev.sh`
  - Action: Create script to stop development environment
  - Notes: Make scripts executable, include error handling

- [ ] Task 36: Create GitHub Actions CI/CD workflows
  - File: `.github/workflows/ci-backend.yml`
  - Action: Create backend CI pipeline (lint with Ruff/Black, type-check with mypy, test with pytest)
  - File: `.github/workflows/ci-frontend.yml`
  - Action: Create frontend CI pipeline (lint with ESLint, type-check with TypeScript, test)
  - File: `.github/workflows/deploy.yml`
  - Action: Create deployment pipeline placeholder (build and deploy steps)
  - Notes: CI workflows should run on push to main and pull requests

- [ ] Task 37: Initialize Git repository
  - Action: Run `git init` in project root
  - Action: Run `git add .` to stage all files
  - Action: Create initial commit with message "Initial project setup: FastAPI backend + Next.js frontend"
  - Notes: Ensure .gitignore is working correctly before committing

- [ ] Task 38: Verify complete setup
  - Action: Verify backend starts: `cd backend && uv run uvicorn app.main:app --reload`
  - Action: Verify frontend starts: `cd frontend && npm run dev`
  - Action: Verify Docker Compose works: `docker-compose up -d`
  - Action: Verify tests run: `cd backend && uv run pytest` (should pass with no tests initially)
  - Notes: Document any issues found and verify all services can start independently

### Acceptance Criteria

- [ ] AC 1: Given a fresh clone of the repository, when a developer runs the setup script, then all dependencies are installed and the project structure is complete
  - Verification: `scripts/setup.sh` executes without errors, `backend/uv.lock` and `frontend/package-lock.json` exist, all directories from architecture.md are present

- [ ] AC 2: Given the project is initialized, when a developer starts the backend service, then FastAPI application starts on port 8000 with health check endpoint accessible
  - Verification: `cd backend && uv run uvicorn app.main:app --reload` starts successfully, `curl http://localhost:8000/health` returns 200 OK with service status, `curl http://localhost:8000/docs` shows OpenAPI documentation

- [ ] AC 3: Given the project is initialized, when a developer starts the frontend service, then Next.js application starts on port 3000 with homepage accessible
  - Verification: `cd frontend && npm run dev` starts successfully, `curl http://localhost:3000` returns 200 OK, page renders

- [ ] AC 4: Given Docker and Docker Compose are installed, when a developer runs `docker-compose up`, then all services (backend, frontend, Redis, RabbitMQ) start successfully
  - Verification: All containers are running, backend health check passes, frontend is accessible, Redis and RabbitMQ are reachable

- [ ] AC 5: Given the backend is set up, when a developer runs `uv run pytest`, then pytest executes successfully (even with no tests)
  - Verification: Pytest runs without import errors, test discovery works, conftest.py is loaded correctly

- [ ] AC 6: Given the backend dependencies are installed, when a developer runs pre-commit hooks, then code quality checks (Black, Ruff, mypy) execute
  - Verification: `uv run pre-commit run --all-files` executes all hooks, hooks are installed via `uv run pre-commit install`

- [ ] AC 7: Given the frontend is set up, when a developer runs `npm run build`, then Next.js builds successfully without errors
  - Verification: Build completes, no TypeScript errors, production build artifacts are created in `.next/`

- [ ] AC 8: Given Alembic is configured, when a developer runs `alembic current`, then Alembic connects to database and shows current revision (or "empty" if no migrations)
  - Verification: Alembic configuration is valid, database connection works (using Supabase URL from environment), env.py correctly imports SQLModel Base and models

- [ ] AC 15: Given Redis and RabbitMQ are running in Docker, when the backend starts, then backend can connect to Redis and RabbitMQ without errors
  - Verification: Backend logs show successful Redis and RabbitMQ connections, health check endpoint reports both services as connected

- [ ] AC 16: Given Prefect is configured, when the backend starts, then Prefect client initializes successfully (even if Prefect server is not running)
  - Verification: Backend starts without Prefect connection errors, Prefect client configuration loads from environment variables

- [ ] AC 17: Given the database connection is configured, when the backend starts, then SQLModel engine initializes and can create a test connection
  - Verification: Backend starts without database connection errors, health check reports database as connected

- [ ] AC 9: Given the project structure is complete, when a developer navigates the codebase, then all directories and placeholder files from architecture.md are present
  - Verification: All directories in architecture.md lines 2033-2486 exist, key placeholder files (__init__.py, router files, service files) are present

- [ ] AC 10: Given environment variables are configured, when services start, then all required environment variables are loaded without errors
  - Verification: Backend config.py loads all variables, frontend .env.local is read, no missing variable errors in logs

- [ ] AC 11: Given the Git repository is initialized, when a developer checks `.gitignore`, then sensitive files (`.env`, `node_modules/`, `__pycache__/`, `.next/`) are excluded
  - Verification: `git status` shows no sensitive files, `.gitignore` includes all required patterns

- [ ] AC 12: Given CI/CD workflows are configured, when a pull request is created, then GitHub Actions workflows run (lint, type-check, test)
  - Verification: Workflows are syntactically valid, can be manually triggered, run on appropriate events

- [ ] AC 13: Given the project is set up, when a developer reads the root README.md, then setup instructions are clear and complete
  - Verification: README includes prerequisites, installation steps, running locally, development workflow

- [ ] AC 14: Given backend and frontend are running, when a developer makes a request from frontend to backend, then CORS is configured correctly and requests succeed
  - Verification: Frontend can make API calls to backend, no CORS errors in browser console, backend CORS middleware allows frontend origin

**Acceptance Criteria Mapping to Stories:**
- AC 1: Maps to Epic 1 stories (setup script, project structure)
- AC 2, AC 15, AC 16, AC 17: Maps to Epic 2 stories (backend infrastructure, service connections)
- AC 3, AC 7: Maps to Epic 3 stories (frontend infrastructure)
- AC 4: Maps to Epic 4 stories (Docker Compose)
- AC 5, AC 6: Maps to Epic 2 stories (testing, code quality)
- AC 8: Maps to Epic 2 stories (database migrations)
- AC 9, AC 10, AC 11: Maps to Epic 1 stories (project structure, environment)
- AC 12: Maps to Epic 4 stories (CI/CD)
- AC 13: Maps to Epic 1 stories (documentation)
- AC 14: Maps to Epic 2 + Epic 3 stories (CORS configuration)

## Epic Generation Guidance

**For Product Managers Creating Epics:**

This tech spec provides the foundational infrastructure that enables all future feature epics. When creating epics from this spec:

1. **Epic Organization**: Group tasks by logical value delivery (see "Epic Grouping Suggestions" in Dependencies section)
2. **Story Sizing**: Each task may map to 1-3 stories depending on complexity:
   - Simple tasks (e.g., Task 1, Task 2) = 1 story
   - Complex tasks (e.g., Task 3, Task 6) = 2-3 stories
   - Sub-tasks (5a, 5b, 6a, etc.) should be grouped with parent tasks
3. **User Value**: While this is infrastructure, frame stories as "enabling capabilities":
   - "As a developer, I want a complete project structure, so that I can start implementing features"
   - "As a developer, I want a working backend API, so that I can build authentication features"
4. **Dependencies**: All epics from this spec must complete before feature epics can begin
5. **Acceptance Criteria**: Each story should have 2-5 ACs from the master list, selected based on story scope

**What This Enables:**
- All user-facing feature epics (authentication, course management, learning, tutoring, etc.)
- Agent implementation epics (curriculum agent, content agent, tutor agent, etc.)
- Platform administration epics (admin dashboard, quality monitoring, etc.)

**Critical Path:**
Epic 1 → Epic 2 → Epic 3 → Epic 4 (sequential dependencies)
- Epic 1 must complete first (foundation)
- Epic 2 and Epic 3 can be done in parallel after Epic 1
- Epic 4 requires Epic 2 and Epic 3 to be complete

## Additional Context

### Dependencies

**Prerequisites:**
- Python 3.12+ installed and available in PATH
- Node.js 18+ and npm installed and available in PATH
- Docker and Docker Compose installed (Docker Desktop or standalone)
- Git installed and configured
- `uv` Python package manager installed (`pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)

**External Services (for local development):**
- Supabase account (free tier) for PostgreSQL database
  - Required: Create project, obtain SUPABASE_URL and SUPABASE_KEY
  - Database connection string will be used by Alembic and SQLModel
- Redis (via Docker Compose - no external account needed)
- RabbitMQ (via Docker Compose - no external account needed)

**Task Dependencies:**
- Tasks 1-2 (Git, README, .env.example) can be done in parallel
- Task 3 (directory structure) must complete before Tasks 4-20 (backend setup)
- Task 4 (pyproject.toml) must complete before Task 21 (install dependencies)
- Task 22 (Next.js init) must complete before Tasks 23-32 (frontend setup)
- Tasks 33-36 (Docker, infrastructure, CI/CD) can be done in parallel after core setup
- Task 37 (Git init) should be last to ensure .gitignore is correct

**Epic Grouping Suggestions (for Epic Creation):**
This tech spec can be organized into logical epics for project management:

**Epic 1: Project Foundation & Configuration**
- Tasks: 1, 2, 3, 37 (Git, README, directory structure, Git init)
- Value: Establishes project structure and documentation
- Enables: All future development work

**Epic 2: Backend Core Infrastructure**
- Tasks: 4, 5, 5a, 5b, 6, 6a, 6b, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
- Value: Complete backend application scaffold with all services, middleware, and tooling
- Enables: Backend feature development (authentication, courses, agents, etc.)

**Epic 3: Frontend Core Infrastructure**
- Tasks: 22, 23, 24, 25, 25a, 26, 27, 28, 28a, 29, 30, 31, 32
- Value: Complete frontend application scaffold with API client, WebSocket, and tooling
- Enables: Frontend feature development (UI components, pages, user flows)

**Epic 4: Development Environment & DevOps**
- Tasks: 33, 34, 35, 36, 38
- Value: Local development environment, CI/CD pipelines, and verification
- Enables: Team collaboration, automated testing, deployment readiness

**Story-Level Considerations:**
- Some tasks (e.g., Task 3, Task 6) may need to be split into multiple stories if they're too large
- Tasks 5a, 5b, 6a, 6b, 25a, 28a are sub-tasks that should be grouped with their parent tasks in stories
- Each story should be completable by a single developer in one session (2-8 hours)
- Stories should have clear "Definition of Done" criteria

### Testing Strategy

**Backend Testing:**
- **Unit Tests**: Test individual services, utilities, and models in isolation
  - Location: `backend/tests/unit/`
  - Framework: pytest with pytest-asyncio for async code
  - Mocking: Use unittest.mock or pytest-mock for external dependencies
  - Coverage: Aim for 80%+ coverage on business logic (services, utils)
  
- **Integration Tests**: Test API endpoints with test database
  - Location: `backend/tests/integration/`
  - Framework: pytest with httpx for async HTTP client
  - Database: Use Testcontainers with PostgreSQL for real database testing
  - Setup: Each test gets clean database state via fixtures
  
- **E2E Tests**: Test complete workflows (deferred to feature implementation)
  - Location: `backend/tests/e2e/`
  - Framework: Playwright for browser automation
  - Scope: Full user journeys, multi-service interactions

**Frontend Testing:**
- **Component Tests**: Test React components (setup structure, implementation deferred)
  - Location: `frontend/tests/components/`
  - Framework: React Testing Library (to be added when implementing components)
  - Scope: Component rendering, user interactions, props handling
  
- **E2E Tests**: Playwright tests for user journeys (setup structure, implementation deferred)
  - Location: `frontend/tests/e2e/`
  - Framework: Playwright
  - Scope: Complete user flows, API integration, routing

**Test Infrastructure Setup (This Spec):**
- **pytest Configuration**: `backend/tests/conftest.py` with async support, fixtures, Testcontainers setup
- **Playwright Configuration**: `frontend/tests/e2e/playwright.config.ts` with browser setup, base URL
- **Test Fixtures**: Database fixtures, API client fixtures, mock service fixtures
- **Test Utilities**: Helper functions for common test operations

**Testing Commands:**
- Backend unit tests: `cd backend && uv run pytest tests/unit/ -v`
- Backend integration tests: `cd backend && uv run pytest tests/integration/ -v`
- Frontend E2E tests: `cd frontend && npm run test:e2e` (when implemented)
- All backend tests: `cd backend && uv run pytest tests/ -v`

### Notes

**Implementation Notes:**
- This spec focuses on local development setup only - production deployment configuration is out of scope
- All dependencies should be pinned to specific versions in lock files (uv.lock, package-lock.json)
- Environment variables should be documented in .env.example files with clear descriptions
- README files should include setup instructions for new developers with troubleshooting section
- Placeholder files should have basic structure/comments indicating what will be implemented later

**High-Risk Items:**
- **Dependency Version Conflicts**: Some dependencies may have conflicting version requirements - test `uv sync` early
- **Docker Compose Networking**: Ensure services can communicate (backend → Redis, backend → RabbitMQ, frontend → backend)
- **Environment Variable Management**: Multiple .env files (root, backend, frontend) - ensure consistency
- **Alembic SQLModel Integration**: Custom env.py configuration required for SQLModel - verify connection works, ensure all models are imported for autogenerate
- **Next.js App Router**: Ensure TypeScript configuration is correct for App Router patterns
- **Database Connection String**: Supabase connection string format may differ from standard PostgreSQL - verify SQLModel engine works with Supabase
- **Service Initialization Order**: Backend services (Redis, RabbitMQ, Prefect) must initialize in correct order - handle connection failures gracefully
- **CORS Configuration**: Frontend and backend must have matching CORS configuration - verify all origins are allowed

**Known Limitations:**
- No actual business logic implementation - only structure and placeholders
- No database schema migrations - only Alembic setup (migrations created during feature work)
- No authentication implementation - only dependency structure
- No agent implementations - only directory structure
- No actual API endpoints - only router structure
- CI/CD workflows are basic - full deployment pipeline deferred

**Epic Creation Readiness:**
- ✅ All tasks are clearly defined with specific file paths and actions
- ✅ Task dependencies are documented and logical
- ✅ Acceptance criteria are testable and complete
- ✅ Epic groupings are suggested for PM reference
- ✅ Story-level considerations are documented
- ✅ Critical path is identified
- ✅ "What this enables" is clearly stated for epic prioritization
- ✅ All technical decisions are documented for story implementation
- ✅ AC mapping to stories is provided
- ✅ Story sizing guidance is included

**Definition of Done (for Epic Completion):**
An epic from this spec is considered "Done" when:
- All tasks in the epic are completed
- All acceptance criteria for the epic are verified
- Services can start independently without errors
- Documentation is complete and accurate
- Code quality checks pass (linting, type checking)
- No blocking issues remain for dependent epics

**Story Estimation Guidance:**
- Simple tasks (1 file, straightforward): 2-4 hours (1 story point)
- Medium tasks (2-3 files, some complexity): 4-8 hours (2-3 story points)
- Complex tasks (multiple files, integration): 8-16 hours (5-8 story points)
- Very complex tasks (Task 3, Task 6): May need to be split into 2-3 stories

**Epic Blocker Risks:**
- If Epic 1 fails, all other epics are blocked
- If Epic 2 fails, backend feature epics are blocked
- If Epic 3 fails, frontend feature epics are blocked
- If Epic 4 fails, team collaboration and deployment are impacted
- Mitigation: Complete Epic 1 first, then Epic 2 and Epic 3 can proceed in parallel

**Future Considerations:**
- Production Docker Compose configuration (`docker-compose.prod.yml`)
- Kubernetes manifests for production scaling
- Advanced monitoring setup (Prometheus, Grafana, Loki)
- mem0 integration for semantic memory (post-MVP)
- API gateway setup (Kong/Apache APISIX)
- Production secrets management (Vault, AWS Secrets Manager, etc.)
- Multi-region deployment configuration
- Advanced caching strategies
- CDN configuration for static assets

