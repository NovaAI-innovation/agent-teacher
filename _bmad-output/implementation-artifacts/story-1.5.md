# Story 1.5: Set Up Backend Environment Configuration

Status: ready-for-dev

## Story

As a developer,
I want backend environment configuration with pydantic-settings,
so that I can manage environment variables securely.

## Acceptance Criteria

1. **Given** The backend structure is initialized **When** I create `backend/.env.example` and `backend/app/config.py` **Then** `backend/.env.example` contains all backend-specific environment variables (database URLs, API keys, service URLs) with descriptions
2. **Given** The backend structure is initialized **When** I create `backend/.env.example` and `backend/app/config.py` **Then** `backend/app/config.py` contains a Settings class using BaseSettings from pydantic-settings
3. **Given** The backend structure is initialized **When** I create `backend/.env.example` and `backend/app/config.py` **Then** The Settings class includes all environment variables with validation and default values
4. **Given** The backend structure is initialized **When** I create `backend/.env.example` and `backend/app/config.py` **Then** The Settings class structure matches architecture.md lines 817-873
5. **Given** The backend structure is initialized **When** I create `backend/.env.example` and `backend/app/config.py` **Then** Running `from app.config import settings` loads configuration without errors

## Tasks / Subtasks

- [ ] Task 1: Create backend .env.example file (AC: 1)
  - [ ] Add database connection variables (Supabase URL, key)
  - [ ] Add Redis connection variables
  - [ ] Add RabbitMQ connection variables
  - [ ] Add API keys for external services (LLM providers)
  - [ ] Add Prefect configuration variables
  - [ ] Add application settings (APP_NAME, ENVIRONMENT, DEBUG, SECRET_KEY)
  - [ ] Add CORS origins configuration
  - [ ] Document each variable with clear description
  - [ ] Reference architecture.md lines 766-809 for complete list
- [ ] Task 2: Create Settings class with pydantic-settings (AC: 2, 3, 4)
  - [ ] Create `backend/app/config.py`
  - [ ] Import BaseSettings from pydantic-settings
  - [ ] Create Settings class inheriting from BaseSettings
  - [ ] Add all environment variables as class attributes
  - [ ] Add validation for required fields
  - [ ] Add default values where appropriate
  - [ ] Configure field types (str, int, bool, etc.)
  - [ ] Match structure from architecture.md lines 817-873
- [ ] Task 3: Verify configuration loading (AC: 5)
  - [ ] Test importing settings: `from app.config import settings`
  - [ ] Verify settings object is created successfully
  - [ ] Test accessing individual settings attributes
  - [ ] Verify validation works for invalid values

## Dev Notes

- **Architecture Patterns**: Use pydantic-settings for type-safe configuration management. Settings should be loaded from environment variables with validation.
- **Source Tree Components**: 
  - `backend/.env.example` - Environment variable template
  - `backend/app/config.py` - Settings class
- **Testing Standards**: No tests required (configuration only), but import should be tested manually
- **Dependencies**: Story 1.4 must be complete (dependencies installed, pydantic-settings available)
- **Configuration Pattern**: Follow pydantic-settings best practices for environment variable loading

### Project Structure Notes

- **Alignment**: Settings class structure must match architecture.md lines 817-873 exactly
- **Environment Variables**: All backend-specific variables should be in backend/.env.example (not root .env.example)
- **Validation**: Use pydantic validators for complex validation (URLs, email formats, etc.)
- **No Conflicts**: Greenfield setup, no existing configuration to conflict with

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Environment Configuration] - Settings class structure (lines 817-873) and environment variables (lines 766-809)
- [Source: _bmad-output/planning-artifacts/tech-spec-mvp-project-initialization-infrastructure.md#Task 5] - Task 5: Set up backend environment configuration
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

