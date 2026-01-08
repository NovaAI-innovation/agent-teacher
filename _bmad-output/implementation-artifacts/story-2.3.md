# Story 2.3: User Logout

Status: ready-for-dev

## Story

As a learner,
I want to log out of my account,
so that I can securely end my session.

## Acceptance Criteria

1. **Given** I am logged into my account **When** I click the logout button **Then** My session is invalidated
2. **Given** I am logged into my account **When** I click the logout button **Then** My access and refresh tokens are revoked
3. **Given** I am logged into my account **When** I click the logout button **Then** I am redirected to the login page or homepage
4. **Given** I am logged into my account **When** I click the logout button **Then** I cannot access protected routes after logout
5. **Given** I am logged into my account **When** I click the logout button **Then** All client-side authentication state is cleared

## Tasks / Subtasks

- [ ] Task 1: Create logout API endpoint (AC: 1, 2)
  - [ ] Update `backend/app/api/v1/auth.py` with logout endpoint
  - [ ] Verify authentication token
  - [ ] Invalidate/revoke tokens (add to blacklist or delete from storage)
  - [ ] Return success response
- [ ] Task 2: Create token blacklist/revocation system (AC: 2)
  - [ ] Create token blacklist in Redis (or database)
  - [ ] Store revoked tokens with expiration
  - [ ] Check blacklist in authentication middleware
- [ ] Task 3: Create logout service (AC: 1, 2)
  - [ ] Update `backend/app/services/auth_service.py` with logout logic
  - [ ] Implement token revocation
  - [ ] Clear session data
- [ ] Task 4: Create logout frontend functionality (AC: 3, 4, 5)
  - [ ] Create logout button/component
  - [ ] Call logout API endpoint
  - [ ] Clear tokens from storage (cookies/localStorage)
  - [ ] Clear authentication state (React context/store)
  - [ ] Redirect to login page or homepage
  - [ ] Update API client to handle logout
- [ ] Task 5: Update authentication middleware (AC: 4)
  - [ ] Update `backend/app/middleware/authentication.py`
  - [ ] Check token blacklist before verifying token
  - [ ] Reject blacklisted tokens

## Dev Notes

- **Architecture Patterns**: Token revocation via blacklist. Client-side state clearing. Protected route handling.
- **Source Tree Components**:
  - `backend/app/api/v1/auth.py` - Logout endpoint
  - `backend/app/services/auth_service.py` - Logout service
  - `backend/app/middleware/authentication.py` - Updated auth middleware
  - `frontend/components/auth/LogoutButton.tsx` - Logout component
  - `frontend/lib/api/auth.ts` - Logout API client
- **Testing Standards**: Unit tests for token revocation, integration tests for logout endpoint, E2E tests for logout flow
- **Dependencies**: Story 2.2 must be complete (JWT authentication, login)
- **Security**: Tokens should be properly revoked. Client-side state must be cleared to prevent reuse.

### Project Structure Notes

- **Alignment**: Logout follows architecture.md authentication patterns. Token blacklist for security.
- **Token Revocation**: Use Redis for token blacklist (fast, expires automatically) or database
- **State Management**: Clear all authentication state on client side (tokens, user data, etc.)
- **Redirect**: Redirect to login or homepage after logout

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Authentication] - Token revocation patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR3] - FR3: User Logout requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 2.3] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
