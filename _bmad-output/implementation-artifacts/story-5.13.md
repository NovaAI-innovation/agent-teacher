# Story 5.13: Display Appropriate Empty States

Status: ready-for-dev

## Story

As a learner,
I want to see appropriate empty states,
so that I understand when there is no content or data to display.

## Acceptance Criteria

1. **Given** I navigate to a page with no content **When** The page loads **Then** I see an appropriate empty state message
2. **Given** I navigate to a page with no content **When** The page loads **Then** Empty state explains why there is no content
3. **Given** I navigate to a page with no content **When** The page loads **Then** Empty state suggests what I can do next
4. **Given** I navigate to a page with no content **When** The page loads **Then** Empty states are accessible and visually clear
5. **Given** I navigate to a page with no content **When** The page loads **Then** Empty states follow consistent design patterns

## Tasks / Subtasks

- [ ] Task 1: Create empty state component (AC: 1, 2, 3, 4, 5)
  - [ ] Create `frontend/components/ui/EmptyState.tsx`
  - [ ] Display appropriate empty state messages
  - [ ] Explain why content is empty
  - [ ] Suggest next actions
  - [ ] Make accessible
  - [ ] Follow consistent design
- [ ] Task 2: Create empty state variants (AC: 1, 2, 3)
  - [ ] Create empty state for no courses
  - [ ] Create empty state for no enrolled courses
  - [ ] Create empty state for no assessments
  - [ ] Create empty state for no progress
  - [ ] Each with appropriate message and suggestions
- [ ] Task 3: Integrate empty states (AC: 1)
  - [ ] Add to courses page (no courses)
  - [ ] Add to enrolled courses page (no enrollments)
  - [ ] Add to assessment results (no attempts)
  - [ ] Add to progress page (no progress)
- [ ] Task 4: Create empty state catalog (AC: 2, 3, 5)
  - [ ] Document empty state messages
  - [ ] Define consistent patterns
  - [ ] Include action suggestions

## Dev Notes

- **Architecture Patterns**: Empty state components. Consistent messaging. Actionable suggestions.
- **Source Tree Components**: 
  - `frontend/components/ui/EmptyState.tsx` - Empty state component
  - Various pages updated with empty states
- **Testing Standards**: Unit tests for components, E2E tests for empty states, accessibility tests
- **Dependencies**: Epic 1 must be complete (Frontend structure)
- **Empty States**: Helpful, not just "no data". Explain why empty. Suggest actions.

### Project Structure Notes

- **Alignment**: Empty states follow architecture.md UX patterns. Helpful and consistent.
- **Messaging**: Explain why content is empty. Provide context. Suggest actions.
- **Consistency**: Use consistent design patterns across all empty states
- **Accessibility**: Make empty states accessible. Screen reader support. Clear visual indicators.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#UX Patterns] - Empty state patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR80] - FR80: Empty States requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.13] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

