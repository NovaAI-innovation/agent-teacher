# Story 1.18: Set Up Docker Compose Development Environment

Status: ready-for-dev

## Story

As a developer,
I want Docker Compose configuration for all services,
so that I can run the entire stack locally with one command.

## Acceptance Criteria

1. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** `docker-compose.yml` exists with services: backend, frontend, redis, rabbitmq
2. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** Backend service is configured with volumes for hot reloading and environment variables
3. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** Frontend service is configured with volumes for hot reloading
4. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** Services have proper networking, health checks, and restart policies
5. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** Port mappings are configured: backend:8000, frontend:3000, redis:6379, rabbitmq:5672,15672
6. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** Running `docker-compose up -d` starts all services successfully
7. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** All containers are running and healthy
8. **Given** Backend and frontend are set up **When** I create Docker Compose configuration **Then** Backend health check passes, frontend is accessible, Redis and RabbitMQ are reachable

## Tasks / Subtasks

- [ ] Task 1: Create docker-compose.yml (AC: 1, 2, 3, 4, 5)
  - [ ] Create `docker-compose.yml` in project root
  - [ ] Define backend service:
    - Use Python 3.12 base image or uv image
    - Mount backend directory as volume for hot reloading
    - Set working directory
    - Configure environment variables (use env_file or environment section)
    - Expose port 8000
    - Add health check endpoint
    - Set restart policy
  - [ ] Define frontend service:
    - Use Node.js base image
    - Mount frontend directory as volume for hot reloading
    - Set working directory
    - Configure environment variables
    - Expose port 3000
    - Add health check
    - Set restart policy
  - [ ] Define redis service:
    - Use official Redis image
    - Expose port 6379
    - Add health check
    - Set restart policy
  - [ ] Define rabbitmq service:
    - Use official RabbitMQ image
    - Expose ports 5672 (AMQP) and 15672 (Management UI)
    - Add health check
    - Set restart policy
  - [ ] Configure networking (default bridge network or custom network)
  - [ ] Set up service dependencies (backend depends on redis, rabbitmq)
- [ ] Task 2: Create Dockerfiles (if needed)
  - [ ] Create `backend/Dockerfile` for backend service (if not using base image directly)
  - [ ] Create `frontend/Dockerfile` for frontend service (if not using base image directly)
  - [ ] Configure for development (hot reloading, etc.)
- [ ] Task 3: Test Docker Compose setup (AC: 6, 7, 8)
  - [ ] Run `docker-compose up -d`
  - [ ] Verify all containers start successfully
  - [ ] Check container status: `docker-compose ps`
  - [ ] Verify backend health check: `curl http://localhost:8000/health`
  - [ ] Verify frontend is accessible: `curl http://localhost:3000`
  - [ ] Verify Redis is reachable: `docker-compose exec redis redis-cli ping`
  - [ ] Verify RabbitMQ is reachable: `docker-compose exec rabbitmq rabbitmq-diagnostics ping`
  - [ ] Test hot reloading by making a code change

## Dev Notes

- **Architecture Patterns**: Docker Compose for local development orchestration. Hot reloading for fast development iteration.
- **Source Tree Components**:
  - `docker-compose.yml` - Docker Compose configuration
  - `backend/Dockerfile` - Backend Docker image (if needed)
  - `frontend/Dockerfile` - Frontend Docker image (if needed)
- **Testing Standards**: No automated tests required, but Docker Compose should be tested manually
- **Dependencies**: Story 1.7 must be complete (backend health check), Story 1.13 must be complete (frontend initialized)
- **Development Focus**: Configured for development (hot reloading, volumes), not production

### Project Structure Notes

- **Alignment**: Docker Compose setup follows architecture.md development environment patterns
- **Hot Reloading**: Volumes mounted for live code changes without rebuilding
- **Service Dependencies**: Backend depends on Redis and RabbitMQ, should wait for them to be healthy
- **Port Mappings**: Match architecture.md port specifications
- **No Conflicts**: Greenfield setup, no existing Docker Compose configuration

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Development Environment] - Docker Compose setup patterns
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 17] - Task 17: Set up Docker Compose development environment
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.18] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
