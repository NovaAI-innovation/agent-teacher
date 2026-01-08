# Story 4.8: Generate Assessments Aligned to Module Content

Status: ready-for-dev

## Story

As the system,
I want to generate assessments aligned to module content,
so that learners can demonstrate their understanding.

## Acceptance Criteria

1. **Given** Module content has been generated **When** Assessment generation is triggered **Then** Assessment Creator Agent generates assessment questions aligned to module content
2. **Given** Module content has been generated **When** Assessment generation is triggered **Then** Assessments include appropriate question types (multiple choice, short answer, etc.)
3. **Given** Module content has been generated **When** Assessment generation is triggered **Then** Assessments test understanding of key concepts from the module
4. **Given** Module content has been generated **When** Assessment generation is triggered **Then** Generated assessments are stored in the knowledge base (FR19)
5. **Given** Module content has been generated **When** Assessment generation is triggered **Then** Assessment quality is evaluated against benchmarks (FR18)
6. **Given** Module content has been generated **When** Assessment generation is triggered **Then** Assessments are linked to their corresponding modules

## Tasks / Subtasks

- [ ] Task 1: Create Assessment Creator Agent (AC: 1, 2, 3)
  - [ ] Create `backend/app/services/agents/assessment_creator_agent.py`
  - [ ] Generate assessment questions aligned to module content
  - [ ] Support multiple question types (multiple choice, short answer, etc.)
  - [ ] Test key concepts from module
  - [ ] Use pydantic-ai for structured generation
- [ ] Task 2: Create Assessment model (AC: 4, 6)
  - [ ] Create `backend/app/models/assessment.py`
  - [ ] Define assessment structure (questions, answers, question types)
  - [ ] Link to module
  - [ ] Create database migration
- [ ] Task 3: Store assessments (AC: 4, 6)
  - [ ] Update knowledge base service
  - [ ] Store assessment questions and answers
  - [ ] Link assessments to modules
- [ ] Task 4: Integrate quality evaluation (AC: 5)
  - [ ] Trigger QA Agent for assessment quality
  - [ ] Evaluate against quality benchmarks
  - [ ] Handle quality failures
- [ ] Task 5: Update course generation workflow (AC: 1)
  - [ ] Update `backend/orchestration/workflows/course_generation_workflow.py`
  - [ ] Add assessment generation step after module content
  - [ ] Link assessments to modules

## Dev Notes

- **Architecture Patterns**: Agent-based assessment generation. Quality evaluation. Module alignment.
- **Source Tree Components**: 
  - `backend/app/services/agents/assessment_creator_agent.py` - Assessment Creator Agent
  - `backend/app/models/assessment.py` - Assessment model
  - `backend/app/services/knowledge/knowledge_base.py` - Knowledge base storage
  - `backend/orchestration/workflows/course_generation_workflow.py` - Updated workflow
- **Testing Standards**: Unit tests for assessment generation, quality tests, alignment tests
- **Dependencies**: Story 4.7 must be complete (Module content), Story 4.9 must be complete (Quality evaluation)
- **Alignment**: Assessments must test key concepts from module content. Questions aligned to learning objectives.

### Project Structure Notes

- **Alignment**: Assessment generation follows architecture.md assessment patterns. Module alignment critical.
- **Question Types**: Support multiple choice, short answer, and other types. Generate appropriate questions.
- **Quality**: Ensure assessments test understanding, not just recall. Quality checks required.
- **Linking**: Assessments must be properly linked to modules in database

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Assessments] - Assessment generation patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR22, FR23] - FR22-23: Assessment requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 4.8] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

