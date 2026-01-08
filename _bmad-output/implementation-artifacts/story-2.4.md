# Story 2.4: Password Reset via Email

Status: ready-for-dev

## Story

As a learner,
I want to reset my password via email,
so that I can regain access if I forget my password.

## Acceptance Criteria

1. **Given** I have a registered account **When** I request a password reset with my email address **Then** A password reset token is generated and stored securely
2. **Given** I have a registered account **When** I request a password reset with my email address **Then** An email with a reset link is sent to my email address
3. **Given** I have a registered account **When** I request a password reset with my email address **Then** The reset link contains a time-limited token (e.g., expires in 1 hour)
4. **Given** I have a registered account **When** I click the reset link and submit a new password **Then** My password is updated in the database
5. **Given** I have a registered account **When** I click the reset link and submit a new password **Then** The reset token is invalidated after use
6. **Given** I have a registered account **When** I click the reset link and submit a new password **Then** All existing sessions are invalidated for security
7. **Given** I have a registered account **When** I click the reset link and submit a new password **Then** I receive confirmation that my password has been reset
8. **Given** I have a registered account **When** I click the reset link and submit a new password **Then** Invalid or expired tokens show an appropriate error message

## Tasks / Subtasks

- [ ] Task 1: Create password reset token model (AC: 1, 3)
  - [ ] Create `backend/app/models/password_reset_token.py`
  - [ ] Define PasswordResetToken model (id, user_id, token, expires_at, used_at)
  - [ ] Create database migration
  - [ ] Add token generation utility
- [ ] Task 2: Create password reset request endpoint (AC: 1, 2, 3)
  - [ ] Update `backend/app/api/v1/auth.py` with password reset request endpoint
  - [ ] Define request schema (email)
  - [ ] Generate secure reset token
  - [ ] Store token in database with expiration (1 hour)
  - [ ] Send email with reset link
  - [ ] Return success response (don't reveal if email exists)
- [ ] Task 3: Create email service (AC: 2)
  - [ ] Create `backend/app/services/email_service.py`
  - [ ] Configure email sending (SMTP or email service)
  - [ ] Create password reset email template
  - [ ] Send email with reset link
- [ ] Task 4: Create password reset confirmation endpoint (AC: 4, 5, 6, 7, 8)
  - [ ] Update `backend/app/api/v1/auth.py` with password reset confirmation endpoint
  - [ ] Define request schema (token, new_password)
  - [ ] Verify token is valid and not expired
  - [ ] Verify token hasn't been used
  - [ ] Update user password (hash new password)
  - [ ] Mark token as used
  - [ ] Invalidate all user sessions (add tokens to blacklist)
  - [ ] Return success response
- [ ] Task 5: Create password reset frontend pages (AC: 2, 4, 7, 8)
  - [ ] Create `frontend/app/(auth)/forgot-password/page.tsx` - Request reset page
  - [ ] Create `frontend/app/(auth)/reset-password/[token]/page.tsx` - Reset password page
  - [ ] Add form for email input (request page)
  - [ ] Add form for new password input (reset page)
  - [ ] Handle form submission
  - [ ] Display success/error messages
  - [ ] Redirect after successful reset
- [ ] Task 6: Update API client (AC: 1, 4)
  - [ ] Update `frontend/lib/api/auth.ts` with password reset functions
  - [ ] Add requestPasswordReset function
  - [ ] Add resetPassword function

## Dev Notes

- **Architecture Patterns**: Secure token-based password reset. Email service integration. Token expiration and one-time use.
- **Source Tree Components**: 
  - `backend/app/models/password_reset_token.py` - Reset token model
  - `backend/app/api/v1/auth.py` - Password reset endpoints
  - `backend/app/services/email_service.py` - Email sending service
  - `backend/app/services/auth_service.py` - Password reset service logic
  - `frontend/app/(auth)/forgot-password/page.tsx` - Request reset page
  - `frontend/app/(auth)/reset-password/[token]/page.tsx` - Reset password page
  - `frontend/lib/api/auth.ts` - Password reset API client
- **Testing Standards**: Unit tests for token generation/validation, service tests for reset logic, integration tests for endpoints, E2E tests for reset flow
- **Dependencies**: Story 2.1 must be complete (User model), Story 2.2 must be complete (session invalidation)
- **Security**: Tokens must be secure, time-limited, and single-use. Don't reveal if email exists. Invalidate all sessions after reset.

### Project Structure Notes

- **Alignment**: Password reset follows architecture.md authentication patterns. Email service for notifications.
- **Token Security**: Use cryptographically secure random tokens. Store hashed tokens if possible.
- **Email Service**: Use SMTP or email service (SendGrid, AWS SES, etc.). Email templates for consistency.
- **Token Expiration**: 1 hour expiration for security. Tokens are single-use only.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Authentication] - Password reset patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR4] - FR4: Password Reset requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 2.4] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

