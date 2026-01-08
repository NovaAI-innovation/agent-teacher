# Story 5.12: Retry Failed Operations

Status: ready-for-dev

## Story

As a learner,
I want to retry failed operations,
so that I can complete actions that failed due to temporary issues.

## Acceptance Criteria

1. **Given** An operation fails **When** I see an error message **Then** I can retry the failed operation
2. **Given** An operation fails **When** I see an error message **Then** Retry functionality is clearly available
3. **Given** An operation fails **When** I see an error message **Then** Retry attempts are limited to prevent infinite loops
4. **Given** An operation fails **When** I see an error message **Then** Retry shows loading state during retry attempt
5. **Given** An operation fails **When** I see an error message **Then** Retry success or failure is clearly communicated

## Tasks / Subtasks

- [ ] Task 1: Create retry utility (AC: 1, 3)
  - [ ] Create `frontend/lib/utils/retry.ts`
  - [ ] Implement retry logic with max attempts
  - [ ] Handle retry failures
  - [ ] Support exponential backoff
- [ ] Task 2: Create retry button component (AC: 1, 2, 4, 5)
  - [ ] Create `frontend/components/ui/RetryButton.tsx`
  - [ ] Display retry button on errors
  - [ ] Show loading state during retry
  - [ ] Communicate retry success/failure
  - [ ] Make clearly visible
- [ ] Task 3: Integrate retry into error handling (AC: 1, 2)
  - [ ] Update error message component
  - [ ] Add retry button to error messages
  - [ ] Handle retry actions
- [ ] Task 4: Update API client with retry (AC: 1, 3)
  - [ ] Update `frontend/lib/api/client.ts`
  - [ ] Add retry logic for failed requests
  - [ ] Limit retry attempts
  - [ ] Handle retry in interceptors
- [ ] Task 5: Create retry state management (AC: 4, 5)
  - [ ] Track retry attempts
  - [ ] Show loading during retry
  - [ ] Update UI on retry success/failure

## Dev Notes

- **Architecture Patterns**: Retry logic with limits. Loading states. Clear feedback.
- **Source Tree Components**:
  - `frontend/lib/utils/retry.ts` - Retry utility
  - `frontend/components/ui/RetryButton.tsx` - Retry button component
  - `frontend/components/ui/ErrorMessage.tsx` - Updated with retry
  - `frontend/lib/api/client.ts` - Updated with retry logic
- **Testing Standards**: Unit tests for retry logic, integration tests for retry functionality, E2E tests for retry flow
- **Dependencies**: Story 5.11 must be complete (Error messages)
- **Retry Strategy**: Limit retry attempts. Use exponential backoff. Show clear feedback.

### Project Structure Notes

- **Alignment**: Retry functionality follows architecture.md UX patterns. User-friendly and safe.
- **Retry Limits**: Prevent infinite retry loops. Set reasonable max attempts (e.g., 3 attempts).
- **User Experience**: Make retry option clear. Show loading state. Communicate results.
- **Safety**: Only retry on transient errors. Don't retry on permanent failures (4xx errors).

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Error Handling] - Retry patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR69] - FR69: Retry Failed Operations requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.12] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
