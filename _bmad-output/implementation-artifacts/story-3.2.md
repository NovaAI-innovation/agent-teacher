# Story 3.2: Browse Available Courses

Status: ready-for-dev

## Story

As a learner,
I want to browse available courses,
so that I can discover courses I'm interested in learning.

## Acceptance Criteria

1. **Given** I am on the courses page **When** I view the course listing **Then** I see a paginated list of available courses
2. **Given** I am on the courses page **When** I view the course listing **Then** Each course card displays: title, description, topic, estimated duration, and enrollment count
3. **Given** I am on the courses page **When** I view the course listing **Then** Courses are displayed in a responsive grid layout
4. **Given** I am on the courses page **When** I view the course listing **Then** I can navigate through multiple pages of courses
5. **Given** I am on the courses page **When** I view the course listing **Then** Empty states are shown when no courses are available
6. **Given** I am on the courses page **When** I view the course listing **Then** Loading indicators are displayed while courses are being fetched
7. **Given** I am on the courses page **When** I view the course listing **Then** Course listings are cached for performance

## Tasks / Subtasks

- [ ] Task 1: Create courses list API endpoint (AC: 1, 4, 7)
  - [ ] Update `backend/app/api/v1/courses.py` with list endpoint
  - [ ] Support pagination (page, limit parameters)
  - [ ] Return only published courses
  - [ ] Include enrollment count in response
  - [ ] Cache response in Redis
- [ ] Task 2: Create CourseCard component (AC: 2, 3)
  - [ ] Create `frontend/components/course/CourseCard.tsx`
  - [ ] Display course title, description, topic
  - [ ] Display estimated duration
  - [ ] Display enrollment count
  - [ ] Make card clickable (link to course detail)
  - [ ] Style with responsive design
- [ ] Task 3: Create CourseList component (AC: 1, 3, 4)
  - [ ] Create `frontend/components/course/CourseList.tsx`
  - [ ] Display courses in responsive grid layout
  - [ ] Implement pagination controls
  - [ ] Handle page navigation
  - [ ] Use React Query for data fetching
- [ ] Task 4: Create courses page (AC: 1, 5, 6)
  - [ ] Create `frontend/app/courses/page.tsx`
  - [ ] Integrate CourseList component
  - [ ] Add loading state with loading indicator
  - [ ] Add empty state component
  - [ ] Handle error states
- [ ] Task 5: Update API client (AC: 1)
  - [ ] Update `frontend/lib/api/courses.ts` with getCourses function
  - [ ] Support pagination parameters
  - [ ] Handle API errors

## Dev Notes

- **Architecture Patterns**: Paginated API with caching. React Query for data fetching. Responsive grid layout.
- **Source Tree Components**:
  - `backend/app/api/v1/courses.py` - Courses list endpoint
  - `frontend/app/courses/page.tsx` - Courses browsing page
  - `frontend/components/course/CourseCard.tsx` - Course card component
  - `frontend/components/course/CourseList.tsx` - Course list component
  - `frontend/lib/api/courses.ts` - Courses API client
- **Testing Standards**: Unit tests for components, integration tests for API, E2E tests for browsing flow
- **Dependencies**: Story 3.1 must be complete (Course catalog, models)
- **Performance**: Use React Query caching. Cache API responses in Redis. Lazy load images.

### Project Structure Notes

- **Alignment**: Course browsing follows architecture.md frontend patterns. Responsive design for all devices.
- **Pagination**: Use cursor-based or offset-based pagination. Default page size (e.g., 12 courses per page).
- **Caching**: React Query for client-side caching, Redis for server-side caching
- **Empty States**: Show helpful message when no courses available

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Course Management] - Course browsing patterns (lines 2573-2581)
- [Source: _bmad-output/planning-artifacts/prd.md#FR9, FR10] - FR9: Browse Courses, FR10: Course Listing requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 3.2] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
