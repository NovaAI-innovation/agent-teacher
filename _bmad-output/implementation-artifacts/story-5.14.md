# Story 5.14: Provide Loading Indicators and Progress Feedback

Status: ready-for-dev

## Story

As a learner,
I want to see loading indicators and progress feedback,
so that I know the system is working and how long operations will take.

## Acceptance Criteria

1. **Given** An operation is in progress **When** I am waiting for a response **Then** I see a loading indicator
2. **Given** An operation is in progress **When** I am waiting for a response **Then** Loading indicators are appropriate for the operation type
3. **Given** An operation is in progress **When** I am waiting for a response **Then** Progress feedback shows estimated time when available
4. **Given** An operation is in progress **When** I am waiting for a response **Then** Loading states are accessible (screen reader announcements)
5. **Given** An operation is in progress **When** I am waiting for a response **Then** Loading indicators follow consistent design patterns

## Tasks / Subtasks

- [ ] Task 1: Create loading indicator component (AC: 1, 2, 5)
  - [ ] Create `frontend/components/ui/LoadingIndicator.tsx`
  - [ ] Support different loading types (spinner, skeleton, progress bar)
  - [ ] Make visually clear
  - [ ] Follow consistent design
- [ ] Task 2: Create progress feedback component (AC: 3)
  - [ ] Create `frontend/components/ui/ProgressFeedback.tsx`
  - [ ] Display progress percentage
  - [ ] Show estimated time when available
  - [ ] Update in real-time
- [ ] Task 3: Integrate loading states (AC: 1, 2)
  - [ ] Add loading to API calls
  - [ ] Add loading to page transitions
  - [ ] Add loading to form submissions
  - [ ] Use appropriate indicator type
- [ ] Task 4: Add accessibility (AC: 4)
  - [ ] Add ARIA live regions for screen readers
  - [ ] Announce loading states
  - [ ] Announce progress updates
- [ ] Task 5: Create loading state management (AC: 1)
  - [ ] Use React Query loading states
  - [ ] Manage loading state globally
  - [ ] Show loading during async operations

## Dev Notes

- **Architecture Patterns**: Loading indicators. Progress feedback. Accessible loading states.
- **Source Tree Components**:
  - `frontend/components/ui/LoadingIndicator.tsx` - Loading indicator component
  - `frontend/components/ui/ProgressFeedback.tsx` - Progress feedback component
  - Various pages/components updated with loading states
- **Testing Standards**: Unit tests for components, E2E tests for loading states, accessibility tests
- **Dependencies**: Epic 1 must be complete (Frontend structure)
- **Loading States**: Show appropriate indicators. Provide progress when available. Make accessible.

### Project Structure Notes

- **Alignment**: Loading indicators follow architecture.md UX patterns. Accessible and informative.
- **Indicator Types**: Use spinners for quick operations, progress bars for long operations, skeletons for content loading
- **Progress**: Show progress percentage and estimated time when available
- **Accessibility**: Announce loading states to screen readers. Use ARIA live regions.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#UX Patterns] - Loading indicator patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR81] - FR81: Loading Indicators requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.14] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
