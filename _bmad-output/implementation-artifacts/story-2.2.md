# Story 2.2: User Login with Email and Password

Status: ready-for-dev

## Story

As a learner,
I want to log in with my email and password,
so that I can access my account and enrolled courses.

## Acceptance Criteria

1. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** I am authenticated successfully
2. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** I receive a JWT access token and refresh token
3. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** Tokens are stored securely (httpOnly cookies or secure storage)
4. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** I am redirected to my dashboard or the page I was trying to access
5. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** Invalid credentials show an appropriate error message without revealing whether the email exists
6. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** Failed login attempts are logged for security monitoring
7. **Given** I have a registered account **When** I submit login credentials with correct email and password **Then** Session expires after 24 hours of inactivity

## Tasks / Subtasks

- [ ] Task 1: Create JWT utility functions (AC: 2, 7)
  - [ ] Create `backend/app/utils/jwt.py`
  - [ ] Implement JWT token generation (access token, refresh token)
  - [ ] Implement JWT token verification
  - [ ] Configure token expiration (access: 15 minutes, refresh: 7 days)
  - [ ] Add token refresh logic
- [ ] Task 2: Create login API endpoint (AC: 1, 2, 5, 6)
  - [ ] Update `backend/app/api/v1/auth.py` with login endpoint
  - [ ] Define login request schema (email, password)
  - [ ] Verify user credentials
  - [ ] Generate JWT tokens on successful login
  - [ ] Log failed login attempts
  - [ ] Return generic error for invalid credentials (don't reveal if email exists)
  - [ ] Return tokens in response
- [ ] Task 3: Create login service (AC: 1, 2, 6)
  - [ ] Update `backend/app/services/auth_service.py` with login logic
  - [ ] Implement credential verification
  - [ ] Handle password verification
  - [ ] Generate JWT tokens
  - [ ] Log authentication events
- [ ] Task 4: Create login frontend page (AC: 3, 4, 5)
  - [ ] Create `frontend/app/(auth)/login/page.tsx`
  - [ ] Create login form component
  - [ ] Add email and password inputs
  - [ ] Handle form submission
  - [ ] Store tokens securely (httpOnly cookies or secure storage)
  - [ ] Handle redirect after login (dashboard or intended page)
  - [ ] Display error messages for invalid credentials
- [ ] Task 5: Update API client (AC: 2, 3)
  - [ ] Update `frontend/lib/api/auth.ts` with login function
  - [ ] Update API client interceptors to handle token storage
  - [ ] Configure token refresh logic
- [ ] Task 6: Create authentication middleware (AC: 4, 7)
  - [ ] Create `backend/app/middleware/authentication.py`
  - [ ] Implement JWT token verification middleware
  - [ ] Handle token expiration
  - [ ] Protect routes requiring authentication

## Dev Notes

- **Architecture Patterns**: JWT-based authentication with access and refresh tokens. Secure token storage on client side.
- **Source Tree Components**:
  - `backend/app/utils/jwt.py` - JWT token utilities
  - `backend/app/api/v1/auth.py` - Login endpoint
  - `backend/app/services/auth_service.py` - Login service
  - `backend/app/middleware/authentication.py` - Auth middleware
  - `frontend/app/(auth)/login/page.tsx` - Login page
  - `frontend/lib/api/auth.ts` - Login API client
- **Testing Standards**: Unit tests for JWT utilities, service tests for login logic, integration tests for API endpoint, E2E tests for login flow
- **Dependencies**: Story 2.1 must be complete (User model, registration)
- **Security**: Use secure token storage (httpOnly cookies preferred). Don't reveal if email exists in error messages. Log failed attempts.

### Project Structure Notes

- **Alignment**: JWT authentication follows architecture.md authentication patterns
- **Token Storage**: Use httpOnly cookies for security, or secure localStorage with XSS protection
- **Token Expiration**: Access tokens short-lived (15 min), refresh tokens longer (7 days)
- **Error Handling**: Generic error messages to prevent email enumeration attacks

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Authentication] - JWT authentication patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR2] - FR2: User Login requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 2.2] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
