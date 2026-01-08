# Story 5.1: Provide Onboarding Guidance for New Learners

Status: ready-for-dev

## Story

As a new learner,
I want onboarding guidance when I first access the platform,
so that I understand how to use the platform effectively.

## Acceptance Criteria

1. **Given** I am a new learner who has just registered **When** I first log in **Then** I see an onboarding flow or welcome guide
2. **Given** I am a new learner who has just registered **When** I first log in **Then** Onboarding explains: how to browse courses, how to enroll, how to access content, how to take assessments
3. **Given** I am a new learner who has just registered **When** I first log in **Then** I can skip or dismiss the onboarding if desired
4. **Given** I am a new learner who has just registered **When** I first log in **Then** Onboarding is only shown once (tracked per user)
5. **Given** I am a new learner who has just registered **When** I first log in **Then** Onboarding is accessible and responsive
6. **Given** I am a new learner who has just registered **When** I first log in **Then** Onboarding provides clear next steps

## Tasks / Subtasks

- [ ] Task 1: Create onboarding tracking (AC: 4)
  - [ ] Update User model with onboarding_completed field
  - [ ] Create database migration
  - [ ] Track onboarding completion per user
- [ ] Task 2: Create onboarding component (AC: 1, 2, 3, 5, 6)
  - [ ] Create `frontend/components/course/OnboardingGuide.tsx`
  - [ ] Create multi-step onboarding flow
  - [ ] Explain: browsing courses, enrollment, accessing content, taking assessments
  - [ ] Add skip/dismiss functionality
  - [ ] Make accessible and responsive
  - [ ] Provide clear next steps
- [ ] Task 3: Integrate onboarding into app (AC: 1, 4)
  - [ ] Update `frontend/app/layout.tsx` or dashboard
  - [ ] Show onboarding on first login
  - [ ] Check onboarding_completed status
  - [ ] Don't show if already completed
- [ ] Task 4: Create onboarding completion API (AC: 4)
  - [ ] Create endpoint to mark onboarding as completed
  - [ ] Update user onboarding_completed field
  - [ ] Return success response

## Dev Notes

- **Architecture Patterns**: Multi-step onboarding flow. User preference tracking. Accessible design.
- **Source Tree Components**:
  - `backend/app/models/user.py` - Updated with onboarding_completed
  - `frontend/components/course/OnboardingGuide.tsx` - Onboarding component
  - `frontend/app/layout.tsx` or dashboard - Onboarding integration
  - `backend/app/api/v1/profile.py` - Onboarding completion endpoint
- **Testing Standards**: Unit tests for component, integration tests for API, E2E tests for onboarding flow
- **Dependencies**: Story 2.2 must be complete (User login)
- **UX**: Clear, helpful onboarding. Skip option. One-time display. Accessible design.

### Project Structure Notes

- **Alignment**: Onboarding follows architecture.md UX patterns. Accessible and responsive.
- **Tracking**: Track onboarding completion per user. Don't show again after completion.
- **Content**: Cover key platform features: browsing, enrollment, content access, assessments
- **Accessibility**: WCAG 2.1 AA compliant. Keyboard navigation. Screen reader support.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Learning & Assessment] - Onboarding patterns (lines 2590-2597)
- [Source: _bmad-output/planning-artifacts/prd.md#FR22] - FR22: Onboarding requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 5.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
