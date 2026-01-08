# Story 1.6: Initialize Backend Database and Service Connections

Status: ready-for-dev

## Story

As a developer,
I want database connection setup and service client initializations (Supabase, Redis, RabbitMQ),
so that backend services can connect to external dependencies.

## Acceptance Criteria

1. **Given** Backend configuration is set up **When** I create database and service connection files **Then** `backend/app/models/database.py` contains SQLModel engine initialization with Supabase connection string from config
2. **Given** Backend configuration is set up **When** I create database and service connection files **Then** `backend/app/models/database.py` exports `get_session` dependency for FastAPI
3. **Given** Backend configuration is set up **When** I create database and service connection files **Then** `backend/app/services/knowledge/supabase_client.py` contains Supabase client wrapper with connection initialization
4. **Given** Backend configuration is set up **When** I create database and service connection files **Then** `backend/app/utils/redis_client.py` contains Redis client with connection pooling
5. **Given** Backend configuration is set up **When** I create database and service connection files **Then** `backend/app/utils/rabbitmq_client.py` contains RabbitMQ connection utility with channel management
6. **Given** Backend configuration is set up **When** I create database and service connection files **Then** All connection utilities can be imported without errors

## Tasks / Subtasks

- [ ] Task 1: Create SQLModel database connection (AC: 1, 2)
  - [ ] Create `backend/app/models/database.py`
  - [ ] Import SQLModel and create_engine
  - [ ] Initialize SQLModel engine with Supabase connection string from config
  - [ ] Create `get_session` async dependency function for FastAPI
  - [ ] Configure session lifecycle (yield pattern for cleanup)
  - [ ] Add error handling for connection failures
- [ ] Task 2: Create Supabase client wrapper (AC: 3)
  - [ ] Create `backend/app/services/knowledge/supabase_client.py`
  - [ ] Import supabase client library
  - [ ] Initialize Supabase client with URL and key from config
  - [ ] Create wrapper functions for common operations (if needed)
  - [ ] Add connection error handling
- [ ] Task 3: Create Redis client with connection pooling (AC: 4)
  - [ ] Create `backend/app/utils/redis_client.py`
  - [ ] Import redis library
  - [ ] Initialize Redis client with connection pool from config
  - [ ] Configure connection pool settings (max connections, timeout)
  - [ ] Add connection error handling and retry logic
  - [ ] Export Redis client instance
- [ ] Task 4: Create RabbitMQ connection utility (AC: 5)
  - [ ] Create `backend/app/utils/rabbitmq_client.py`
  - [ ] Import aio-pika for async RabbitMQ operations
  - [ ] Create connection management functions
  - [ ] Implement channel management
  - [ ] Add connection error handling and reconnection logic
  - [ ] Export connection utilities
- [ ] Task 5: Verify all connections can be imported (AC: 6)
  - [ ] Test importing database module
  - [ ] Test importing Supabase client
  - [ ] Test importing Redis client
  - [ ] Test importing RabbitMQ client
  - [ ] Verify no import errors

## Dev Notes

- **Architecture Patterns**: Use dependency injection pattern for database sessions. Connection pooling for Redis and RabbitMQ for performance.
- **Source Tree Components**: 
  - `backend/app/models/database.py` - SQLModel database engine and session
  - `backend/app/services/knowledge/supabase_client.py` - Supabase client wrapper
  - `backend/app/utils/redis_client.py` - Redis client with pooling
  - `backend/app/utils/rabbitmq_client.py` - RabbitMQ connection management
- **Testing Standards**: No tests required (connection setup only), but imports should be tested manually
- **Dependencies**: Story 1.5 must be complete (config.py with connection strings)
- **Connection Management**: Use async patterns for all connections. Implement proper cleanup and error handling.

### Project Structure Notes

- **Alignment**: Database connection follows SQLModel patterns. Service clients follow architecture.md specifications.
- **Connection Strings**: All connection strings come from config.py (environment variables)
- **Error Handling**: All connection utilities should handle connection failures gracefully
- **No Conflicts**: Greenfield setup, no existing connections to conflict with

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Database Connection] - SQLModel database setup patterns
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 5a] - Task 5a: Create database connection setup
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.6] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

