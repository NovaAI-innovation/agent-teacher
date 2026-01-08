# Story 2.1: User Registration with Email and Password

Status: ready-for-dev

## Story

As a learner,
I want to create an account with my email and password,
so that I can access the learning platform.

## Acceptance Criteria

1. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** My account is created in the database
2. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** My password is hashed using bcrypt/Argon2 before storage
3. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** I receive a success message confirming account creation
4. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** I am redirected to the login page
5. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** Email validation ensures the email format is correct
6. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** Password validation enforces minimum strength requirements
7. **Given** I am a new user on the registration page **When** I submit a registration form with valid email, password, and confirmation password **Then** Duplicate email addresses are rejected with an appropriate error message

## Tasks / Subtasks

- [ ] Task 1: Create User model (AC: 1, 2)
  - [ ] Create `backend/app/models/user.py`
  - [ ] Define User model with SQLModel (id, email, hashed_password, created_at, updated_at)
  - [ ] Add email uniqueness constraint
  - [ ] Add password hashing utility using passlib with bcrypt/Argon2
  - [ ] Create password hashing method
  - [ ] Create password verification method
- [ ] Task 2: Create registration API endpoint (AC: 1, 2, 5, 6, 7)
  - [ ] Create `backend/app/api/v1/auth.py` registration endpoint
  - [ ] Define registration request schema (email, password, password_confirm)
  - [ ] Add email validation (format check)
  - [ ] Add password validation (minimum length, strength requirements)
  - [ ] Check for duplicate email addresses
  - [ ] Hash password before storing
  - [ ] Create user in database
  - [ ] Return success response
- [ ] Task 3: Create registration service (AC: 1, 2, 7)
  - [ ] Create `backend/app/services/auth_service.py`
  - [ ] Implement user registration logic
  - [ ] Handle duplicate email validation
  - [ ] Hash passwords securely
  - [ ] Create user records
- [ ] Task 4: Create registration frontend page (AC: 3, 4, 5, 6, 7)
  - [ ] Create `frontend/app/(auth)/register/page.tsx`
  - [ ] Create registration form component
  - [ ] Add email input with validation
  - [ ] Add password input with strength indicator
  - [ ] Add password confirmation input
  - [ ] Add form validation (client-side)
  - [ ] Handle form submission
  - [ ] Display success message on successful registration
  - [ ] Redirect to login page after success
  - [ ] Display error messages for validation failures
- [ ] Task 5: Create API client function (AC: 1)
  - [ ] Update `frontend/lib/api/auth.ts`
  - [ ] Create register function
  - [ ] Handle API errors
- [ ] Task 6: Create database migration (AC: 1)
  - [ ] Create Alembic migration for User table
  - [ ] Run migration: `alembic upgrade head`
  - [ ] Verify User table is created

## Dev Notes

- **Architecture Patterns**: REST API for registration. Password hashing with bcrypt/Argon2. Email uniqueness validation.
- **Source Tree Components**:
  - `backend/app/models/user.py` - User model
  - `backend/app/api/v1/auth.py` - Registration endpoint
  - `backend/app/services/auth_service.py` - Registration service logic
  - `frontend/app/(auth)/register/page.tsx` - Registration page
  - `frontend/lib/api/auth.ts` - Registration API client
  - `backend/migrations/versions/` - User table migration
- **Testing Standards**: Unit tests for password hashing, service tests for registration logic, integration tests for API endpoint, E2E tests for registration flow
- **Dependencies**: Epic 1 must be complete (database, API structure, frontend structure)
- **Security**: Passwords must be hashed, never stored in plain text. Use secure password hashing algorithm (bcrypt or Argon2).

### Project Structure Notes

- **Alignment**: User model follows architecture.md data model patterns. Registration follows REST API patterns.
- **Password Security**: Use passlib with bcrypt or Argon2. Minimum password requirements (length, complexity).
- **Email Validation**: Validate email format on both client and server side.
- **Error Handling**: Provide clear error messages for validation failures.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#User Account Management] - User model and authentication patterns (lines 2565-2571)
- [Source: _bmad-output/planning-artifacts/prd.md#FR1] - FR1: User Registration requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 2.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
