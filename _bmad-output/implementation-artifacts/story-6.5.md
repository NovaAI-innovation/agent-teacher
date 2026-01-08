# Story 6.5: Access Tutoring During Module Learning

Status: ready-for-dev

## Story

As a learner,
I want to access tutoring while learning a module,
so that I can get help without leaving my learning context.

## Acceptance Criteria

1. **Given** I am viewing a module **When** I need help **Then** I can access tutoring during module learning (FR34)
2. **Given** I am viewing a module **When** I need help **Then** Tutoring is accessible from the module page
3. **Given** I am viewing a module **When** I need help **Then** Tutoring session is automatically linked to the current module
4. **Given** I am viewing a module **When** I need help **Then** I can continue learning while tutoring is active
5. **Given** I am viewing a module **When** I need help **Then** Tutoring interface is accessible and doesn't block learning

## Tasks / Subtasks

- [ ] Task 1: Add tutoring button to module page (AC: 1, 2)
  - [ ] Update `frontend/app/learning/[courseId]/modules/[moduleId]/page.tsx`
  - [ ] Add "Get Help" or tutoring button
  - [ ] Make easily accessible
- [ ] Task 2: Create tutoring overlay/modal (AC: 1, 4, 5)
  - [ ] Create `frontend/components/tutoring/TutoringOverlay.tsx`
  - [ ] Display tutoring chat in overlay/modal
  - [ ] Allow learning content to remain visible
  - [ ] Make accessible and responsive
- [ ] Task 3: Auto-link module context (AC: 3)
  - [ ] Pass module context when initiating tutoring
  - [ ] Set module context in tutoring session
  - [ ] Use context in tutor responses
- [ ] Task 4: Integrate tutoring into learning flow (AC: 1, 2, 4)
  - [ ] Open tutoring from module page
  - [ ] Maintain learning context
  - [ ] Allow simultaneous learning and tutoring

## Dev Notes

- **Architecture Patterns**: In-context tutoring. Overlay/modal interface. Seamless integration.
- **Source Tree Components**:
  - `frontend/app/learning/[courseId]/modules/[moduleId]/page.tsx` - Updated module page
  - `frontend/components/tutoring/TutoringOverlay.tsx` - Tutoring overlay component
  - `frontend/components/tutoring/TutoringChat.tsx` - Tutoring chat component
- **Testing Standards**: Unit tests for components, E2E tests for tutoring access, accessibility tests
- **Dependencies**: Story 6.1 must be complete (Tutoring sessions), Story 5.3 must be complete (Module access)
- **User Experience**: Easy access to tutoring. Don't block learning. Seamless integration.

### Project Structure Notes

- **Alignment**: In-context tutoring follows architecture.md UX patterns. Accessible and non-intrusive.
- **Access**: Make tutoring easily accessible from module page. Clear button/link.
- **Interface**: Use overlay/modal so learning content remains visible. Non-blocking.
- **Context**: Automatically link to current module for relevant help

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Interactive Tutoring] - In-context tutoring patterns (lines 2599-2602)
- [Source: _bmad-output/planning-artifacts/prd.md#FR34] - FR34: Access Tutoring requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 6.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
