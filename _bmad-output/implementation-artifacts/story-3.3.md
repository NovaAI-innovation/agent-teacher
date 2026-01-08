# Story 3.3: Search and Filter Courses

Status: ready-for-dev

## Story

As a learner,
I want to search and filter courses,
so that I can quickly find courses matching my interests.

## Acceptance Criteria

1. **Given** I am on the courses page **When** I enter a search query **Then** Courses matching the search term (in title, description, or topic) are displayed
2. **Given** I am on the courses page **When** I enter a search query **Then** Search results are highlighted with matching terms
3. **Given** I am on the courses page **When** I enter a search query **Then** I can filter courses by topic/category
4. **Given** I am on the courses page **When** I enter a search query **Then** I can filter courses by difficulty level (if available)
5. **Given** I am on the courses page **When** I enter a search query **Then** I can combine search and filters
6. **Given** I am on the courses page **When** I enter a search query **Then** Search results are paginated
7. **Given** I am on the courses page **When** I enter a search query **Then** Empty search results show appropriate messaging
8. **Given** I am on the courses page **When** I enter a search query **Then** Search is case-insensitive and handles partial matches

## Tasks / Subtasks

- [ ] Task 1: Create search API endpoint (AC: 1, 5, 6, 8)
  - [ ] Update `backend/app/api/v1/courses.py` with search endpoint
  - [ ] Implement full-text search (PostgreSQL full-text search or basic LIKE queries)
  - [ ] Search in title, description, topic fields
  - [ ] Support case-insensitive and partial matching
  - [ ] Support filtering by topic/category
  - [ ] Support filtering by difficulty (if available)
  - [ ] Combine search and filters
  - [ ] Support pagination
- [ ] Task 2: Create search service (AC: 1, 8)
  - [ ] Update `backend/app/services/course_service.py` with search logic
  - [ ] Implement search query building
  - [ ] Handle case-insensitive matching
  - [ ] Handle partial matches
- [ ] Task 3: Create CourseSearch component (AC: 1, 2, 3, 4, 5, 7, 8)
  - [ ] Create `frontend/components/course/CourseSearch.tsx`
  - [ ] Add search input field
  - [ ] Add topic/category filter dropdown
  - [ ] Add difficulty filter dropdown (if available)
  - [ ] Implement debounced search
  - [ ] Highlight matching terms in results
  - [ ] Display empty state for no results
- [ ] Task 4: Integrate search into courses page (AC: 1, 5, 6)
  - [ ] Update `frontend/app/courses/page.tsx`
  - [ ] Integrate CourseSearch component
  - [ ] Update CourseList to handle search results
  - [ ] Maintain pagination with search/filters
- [ ] Task 5: Update API client (AC: 1)
  - [ ] Update `frontend/lib/api/courses.ts` with searchCourses function
  - [ ] Support search query and filter parameters

## Dev Notes

- **Architecture Patterns**: Full-text search with filtering. Debounced search for performance. Client-side highlighting.
- **Source Tree Components**:
  - `backend/app/api/v1/courses.py` - Search endpoint
  - `backend/app/services/course_service.py` - Search service
  - `frontend/components/course/CourseSearch.tsx` - Search component
  - `frontend/app/courses/page.tsx` - Updated courses page
  - `frontend/lib/api/courses.ts` - Search API client
- **Testing Standards**: Unit tests for search logic, integration tests for search API, E2E tests for search flow
- **Dependencies**: Story 3.1 must be complete (Course catalog), Story 3.2 must be complete (Courses page)
- **Performance**: Use debouncing for search input. Cache search results. Optimize database queries with indexes.

### Project Structure Notes

- **Alignment**: Search follows architecture.md API patterns. Full-text search for better results.
- **Search Strategy**: Use PostgreSQL full-text search or basic LIKE queries. Can upgrade to Elasticsearch later if needed.
- **Filtering**: Combine search with filters. Support multiple filter combinations.
- **User Experience**: Debounced search, loading states, empty states, highlighted results

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Course Management] - Search patterns (lines 2573-2581)
- [Source: _bmad-output/planning-artifacts/prd.md#FR8] - FR8: Search Courses requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 3.3] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
