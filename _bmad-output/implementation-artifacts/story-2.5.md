# Story 2.5: Manage Account Settings

Status: ready-for-dev

## Story

As a learner,
I want to view and update my account settings,
so that I can manage my profile information and preferences.

## Acceptance Criteria

1. **Given** I am logged into my account **When** I navigate to account settings **Then** I can view my current account information (email, name, preferences)
2. **Given** I am logged into my account **When** I navigate to account settings **Then** I can update my display name
3. **Given** I am logged into my account **When** I navigate to account settings **Then** I can update my email address (with email verification)
4. **Given** I am logged into my account **When** I navigate to account settings **Then** I can update my password (with current password verification)
5. **Given** I am logged into my account **When** I navigate to account settings **Then** I can update my preferences (notifications, privacy settings)
6. **Given** I am logged into my account **When** I navigate to account settings **Then** Changes are saved to the database
7. **Given** I am logged into my account **When** I navigate to account settings **Then** I receive confirmation when settings are updated
8. **Given** I am logged into my account **When** I navigate to account settings **Then** Email changes require verification before taking effect
9. **Given** I am logged into my account **When** I navigate to account settings **Then** Password changes require current password confirmation

## Tasks / Subtasks

- [ ] Task 1: Update User model (AC: 1, 2, 5)
  - [ ] Update `backend/app/models/user.py`
  - [ ] Add display_name field
  - [ ] Add preferences field (JSON or separate table)
  - [ ] Add email_verified field
  - [ ] Create database migration
- [ ] Task 2: Create account settings API endpoints (AC: 1, 2, 3, 4, 5, 6, 8, 9)
  - [ ] Create `backend/app/api/v1/profile.py` or update auth.py
  - [ ] Create GET endpoint to retrieve user settings
  - [ ] Create PATCH/PUT endpoint to update display name
  - [ ] Create PATCH endpoint to update email (with verification flow)
  - [ ] Create PATCH endpoint to update password (require current password)
  - [ ] Create PATCH endpoint to update preferences
  - [ ] Add validation and authorization checks
- [ ] Task 3: Create user service (AC: 2, 3, 4, 5, 6, 8, 9)
  - [ ] Create `backend/app/services/user_service.py`
  - [ ] Implement get user settings
  - [ ] Implement update display name
  - [ ] Implement update email (with verification token)
  - [ ] Implement update password (verify current password first)
  - [ ] Implement update preferences
- [ ] Task 4: Create email verification flow (AC: 3, 8)
  - [ ] Create email verification token model
  - [ ] Create email verification endpoint
  - [ ] Send verification email on email change
  - [ ] Verify email token
- [ ] Task 5: Create account settings frontend page (AC: 1, 2, 3, 4, 5, 7, 8, 9)
  - [ ] Create `frontend/app/settings/page.tsx` or `frontend/app/profile/settings/page.tsx`
  - [ ] Create settings form component
  - [ ] Display current user information
  - [ ] Add form fields for display name
  - [ ] Add form fields for email (with verification status)
  - [ ] Add form fields for password change (current + new)
  - [ ] Add form fields for preferences
  - [ ] Handle form submission
  - [ ] Display success/error messages
  - [ ] Handle email verification flow
- [ ] Task 6: Update API client (AC: 1, 2, 3, 4, 5)
  - [ ] Update `frontend/lib/api/auth.ts` or create `frontend/lib/api/profile.ts`
  - [ ] Add getSettings function
  - [ ] Add updateDisplayName function
  - [ ] Add updateEmail function
  - [ ] Add updatePassword function
  - [ ] Add updatePreferences function

## Dev Notes

- **Architecture Patterns**: REST API for account management. Email verification for security. Password verification for sensitive changes.
- **Source Tree Components**: 
  - `backend/app/models/user.py` - Updated User model
  - `backend/app/api/v1/profile.py` - Account settings endpoints
  - `backend/app/services/user_service.py` - User settings service
  - `frontend/app/settings/page.tsx` - Account settings page
  - `frontend/lib/api/profile.ts` - Settings API client
- **Testing Standards**: Unit tests for user service, integration tests for API endpoints, E2E tests for settings update flow
- **Dependencies**: Story 2.1 must be complete (User model), Story 2.2 must be complete (authentication)
- **Security**: Require current password for password changes. Email verification for email changes. Authorization checks.

### Project Structure Notes

- **Alignment**: Account settings follow architecture.md user management patterns. Email verification for security.
- **Preferences**: Store as JSON field or separate preferences table. Flexible for future expansion.
- **Email Verification**: Send verification email when email is changed. Email remains unverified until verified.
- **Password Changes**: Always require current password verification for security.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#User Account Management] - Account settings patterns (lines 2565-2571)
- [Source: _bmad-output/planning-artifacts/prd.md#FR4] - FR4: Account Management requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 2.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

