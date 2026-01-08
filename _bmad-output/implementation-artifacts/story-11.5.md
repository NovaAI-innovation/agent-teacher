# Story 11.5: Adjust Text Size and Contrast Settings

Status: ready-for-dev

## Story

As a learner with visual impairments,
I want to adjust text size and contrast settings,
so that I can read content comfortably.

## Acceptance Criteria

1. **Given** I am viewing course content **When** I adjust accessibility settings **Then** I can adjust text size (FR84)
2. **Given** I am viewing course content **When** I adjust accessibility settings **Then** I can adjust contrast settings (FR84)
3. **Given** I am viewing course content **When** I adjust accessibility settings **Then** Settings are saved and persist across sessions
4. **Given** I am viewing course content **When** I adjust accessibility settings **Then** Text size adjustments maintain content readability and layout
5. **Given** I am viewing course content **When** I adjust accessibility settings **Then** Contrast adjustments meet or exceed WCAG AA standards
6. **Given** I am viewing course content **When** I adjust accessibility settings **Then** Settings are easily accessible
7. **Given** I am viewing course content **When** I adjust accessibility settings **Then** Settings apply consistently across the platform

## Tasks / Subtasks

- [ ] Task 1: Create accessibility settings model (AC: 3)
  - [ ] Create `backend/app/models/user_accessibility_settings.py`
  - [ ] Store text size preference
  - [ ] Store contrast preference
  - [ ] Link to user account
  - [ ] Create database migration
- [ ] Task 2: Create accessibility settings API (AC: 1, 2, 3)
  - [ ] Create `backend/app/api/v1/profile/accessibility_settings.py`
  - [ ] Create get settings endpoint
  - [ ] Create update settings endpoint
  - [ ] Persist settings
- [ ] Task 3: Implement text size adjustment (AC: 1, 4)
  - [ ] Create text size controls
  - [ ] Apply text size changes
  - [ ] Maintain layout and readability
  - [ ] Use CSS custom properties for text size
- [ ] Task 4: Implement contrast adjustment (AC: 2, 5)
  - [ ] Create contrast controls
  - [ ] Apply contrast themes
  - [ ] Ensure WCAG AA compliance
  - [ ] Use CSS custom properties for contrast
- [ ] Task 5: Create accessibility settings UI (AC: 1, 2, 6, 7)
  - [ ] Create `frontend/app/settings/accessibility/page.tsx`
  - [ ] Add text size controls
  - [ ] Add contrast controls
  - [ ] Make easily accessible
  - [ ] Apply settings consistently
- [ ] Task 6: Apply settings globally (AC: 7)
  - [ ] Apply settings across all pages
  - [ ] Use CSS custom properties
  - [ ] Ensure consistent application

## Dev Notes

- **Architecture Patterns**: User preferences. Accessibility settings. CSS custom properties. Persistent settings.
- **Source Tree Components**: 
  - `backend/app/models/user_accessibility_settings.py` - Accessibility settings model
  - `backend/app/api/v1/profile/accessibility_settings.py` - Settings API
  - `frontend/app/settings/accessibility/page.tsx` - Accessibility settings page
  - `frontend/app/globals.css` - Updated with CSS custom properties
- **Testing Standards**: Accessibility tests, settings persistence tests, E2E tests
- **Dependencies**: Story 2.2 must be complete (User authentication)
- **Settings**: Text size and contrast adjustments. Persistent across sessions. WCAG AA compliant.

### Project Structure Notes

- **Alignment**: Accessibility settings follow architecture.md UX patterns. User-friendly and persistent.
- **Text Size**: Allow text size adjustment. Maintain readability and layout.
- **Contrast**: Allow contrast adjustment. Ensure WCAG AA compliance.
- **Persistence**: Save settings to database. Apply across sessions. Consistent application.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Accessibility] - Accessibility settings patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR84] - FR84: Text Size and Contrast requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 11.5] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
