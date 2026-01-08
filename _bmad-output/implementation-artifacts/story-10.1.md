# Story 10.1: Request Data Deletion

Status: ready-for-dev

## Story

As a learner,
I want to request deletion of my data,
so that I can exercise my right to be forgotten under GDPR.

## Acceptance Criteria

1. **Given** I am a registered user **When** I request data deletion **Then** I can submit a data deletion request (FR71)
2. **Given** I am a registered user **When** I request data deletion **Then** Deletion request is processed within 30 days (GDPR requirement)
3. **Given** I am a registered user **When** I request data deletion **Then** All my personal data is deleted: account, progress, assessments, enrollment data
4. **Given** I am a registered user **When** I request data deletion **Then** Data retention policy is followed (90 days after deletion request)
5. **Given** I am a registered user **When** I request data deletion **Then** I receive confirmation when deletion is complete
6. **Given** I am a registered user **When** I request data deletion **Then** Deletion actions are logged for audit (FR73)
7. **Given** I am a registered user **When** I request data deletion **Then** Deletion process is secure and verified

## Tasks / Subtasks

- [ ] Task 1: Create data deletion request model (AC: 1)
  - [ ] Create `backend/app/models/data_deletion_request.py`
  - [ ] Store deletion requests (user_id, requested_at, status, processed_at)
  - [ ] Create database migration
- [ ] Task 2: Create data deletion API (AC: 1, 2, 3, 4, 6, 7)
  - [ ] Create `backend/app/api/v1/privacy/data_deletion.py`
  - [ ] Create request deletion endpoint
  - [ ] Process deletion requests
  - [ ] Delete all user data (account, progress, assessments, enrollments)
  - [ ] Follow retention policy (90 days)
  - [ ] Log deletion actions
  - [ ] Verify deletion completion
- [ ] Task 3: Create data deletion service (AC: 2, 3, 4, 6, 7)
  - [ ] Create `backend/app/services/privacy/data_deletion_service.py`
  - [ ] Implement comprehensive data deletion
  - [ ] Delete all user-related data
  - [ ] Follow retention policies
  - [ ] Log all deletion actions
  - [ ] Verify deletion
- [ ] Task 4: Create deletion request UI (AC: 1, 5)
  - [ ] Create `frontend/app/settings/privacy/data-deletion/page.tsx`
  - [ ] Create deletion request form
  - [ ] Show confirmation dialog
  - [ ] Display deletion status
  - [ ] Show completion confirmation
- [ ] Task 5: Create scheduled deletion processor (AC: 2, 4)
  - [ ] Create background task for processing deletions
  - [ ] Process deletions within 30 days
  - [ ] Handle retention period

## Dev Notes

- **Architecture Patterns**: GDPR compliance. Data deletion. Audit logging. Retention policies.
- **Source Tree Components**:
  - `backend/app/models/data_deletion_request.py` - Deletion request model
  - `backend/app/api/v1/privacy/data_deletion.py` - Data deletion API
  - `backend/app/services/privacy/data_deletion_service.py` - Data deletion service
  - `frontend/app/settings/privacy/data-deletion/page.tsx` - Deletion request UI
- **Testing Standards**: Unit tests for deletion service, integration tests, security tests, compliance tests
- **Dependencies**: Story 2.1 must be complete (User model), Story 7.1 must be complete (Progress tracking)
- **GDPR Compliance**: Process within 30 days. Delete all personal data. Follow retention policies. Audit logging.

### Project Structure Notes

- **Alignment**: Data deletion follows architecture.md privacy patterns. GDPR compliant.
- **Comprehensive Deletion**: Delete all user-related data (account, progress, assessments, enrollments, etc.)
- **Retention**: Follow 90-day retention policy after deletion request
- **Audit**: Log all deletion actions for compliance verification

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Privacy] - Data deletion patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR71, FR73] - FR71: Data Deletion, FR73: Audit Logging requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 10.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
