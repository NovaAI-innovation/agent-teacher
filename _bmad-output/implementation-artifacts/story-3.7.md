# Story 3.7: SEO-Optimized Course Pages

Status: ready-for-dev

## Story

As the system,
I want course pages to be SEO-optimized,
so that courses are discoverable via search engines.

## Acceptance Criteria

1. **Given** A course exists in the catalog **When** The course page is rendered **Then** Unique title tags and meta descriptions are generated for each course
2. **Given** A course exists in the catalog **When** The course page is rendered **Then** Schema.org structured data (Course, EducationalContent) is included
3. **Given** A course exists in the catalog **When** The course page is rendered **Then** Proper heading hierarchy (H1-H6) is used for content organization
4. **Given** A course exists in the catalog **When** The course page is rendered **Then** Clean, descriptive URLs are used for course pages
5. **Given** A course exists in the catalog **When** The course page is rendered **Then** XML sitemap includes all course pages
6. **Given** A course exists in the catalog **When** The course page is rendered **Then** robots.txt is configured appropriately
7. **Given** A course exists in the catalog **When** The course page is rendered **Then** Canonical URLs prevent duplicate content issues
8. **Given** A course exists in the catalog **When** The course page is rendered **Then** Course pages are indexable by search engines

## Tasks / Subtasks

- [ ] Task 1: Generate dynamic metadata (AC: 1, 4, 7)
  - [ ] Update `frontend/app/courses/[slug]/page.tsx`
  - [ ] Generate dynamic metadata function (Next.js generateMetadata)
  - [ ] Create unique title tags per course
  - [ ] Create unique meta descriptions per course
  - [ ] Add Open Graph tags
  - [ ] Add Twitter Card tags
  - [ ] Add canonical URLs
- [ ] Task 2: Add Schema.org structured data (AC: 2)
  - [ ] Create structured data component
  - [ ] Add Course schema
  - [ ] Add EducationalContent schema
  - [ ] Include in course detail page
- [ ] Task 3: Ensure proper heading hierarchy (AC: 3)
  - [ ] Review course detail page structure
  - [ ] Ensure H1 for course title
  - [ ] Use H2-H6 for sections appropriately
  - [ ] Maintain semantic HTML structure
- [ ] Task 4: Create XML sitemap (AC: 5)
  - [ ] Create `frontend/app/sitemap.ts` (Next.js sitemap)
  - [ ] Generate sitemap with all published courses
  - [ ] Include course URLs with slugs
  - [ ] Set update frequency and priority
- [ ] Task 5: Configure robots.txt (AC: 6)
  - [ ] Create `frontend/app/robots.ts` (Next.js robots.txt)
  - [ ] Allow indexing of course pages
  - [ ] Disallow admin and API routes
  - [ ] Reference sitemap
- [ ] Task 6: Verify SEO implementation (AC: 8)
  - [ ] Test metadata generation
  - [ ] Validate structured data (Google Rich Results Test)
  - [ ] Verify sitemap is accessible
  - [ ] Verify robots.txt is accessible
  - [ ] Test page indexability

## Dev Notes

- **Architecture Patterns**: Dynamic metadata generation. Schema.org structured data. SEO best practices.
- **Source Tree Components**: 
  - `frontend/app/courses/[slug]/page.tsx` - Updated with metadata
  - `frontend/app/sitemap.ts` - XML sitemap generation
  - `frontend/app/robots.ts` - Robots.txt configuration
  - `frontend/components/course/CourseStructuredData.tsx` - Schema.org data component
- **Testing Standards**: SEO validation tests, structured data validation, sitemap validation
- **Dependencies**: Story 3.4 must be complete (Course detail page)
- **SEO Best Practices**: Unique titles/descriptions, structured data, clean URLs, proper heading hierarchy, sitemap, robots.txt

### Project Structure Notes

- **Alignment**: SEO follows architecture.md SEO patterns. Next.js metadata API for dynamic metadata.
- **Structured Data**: Use Schema.org Course and EducationalContent schemas for rich snippets
- **Sitemap**: Generate dynamically from published courses. Update when courses are published/updated.
- **URLs**: Use clean, descriptive slugs. Canonical URLs prevent duplicate content.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#SEO] - SEO optimization patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR59] - FR59: SEO-Optimized Course Pages requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 3.7] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

