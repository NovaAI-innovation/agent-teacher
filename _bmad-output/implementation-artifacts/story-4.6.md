# Story 4.6: Generate Units with Modules for Courses

Status: ready-for-dev

## Story

As the system,
I want to autonomously generate units with modules,
so that course content is structured and complete.

## Acceptance Criteria

1. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Curriculum Designer Agent creates unit structure
2. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Content Generator Agent generates module content for each unit
3. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Modules are organized sequentially within units
4. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Each module has associated learning content
5. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Generated content is stored in the knowledge base (FR19)
6. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Content hierarchy (Course → Unit → Module) is maintained (FR7)
7. **Given** A course introduction has been generated **When** Unit and module generation is triggered **Then** Generation workflow completes successfully

## Tasks / Subtasks

- [ ] Task 1: Extend Curriculum Designer Agent (AC: 1, 3, 6)
  - [ ] Update `backend/app/services/agents/curriculum_designer_agent.py`
  - [ ] Add unit structure generation
  - [ ] Create sequential module organization
  - [ ] Maintain Course → Unit → Module hierarchy
- [ ] Task 2: Implement Content Generator Agent (AC: 2, 4)
  - [ ] Create `backend/app/services/agents/content_generator_agent.py`
  - [ ] Generate module learning content
  - [ ] Use pydantic-ai for structured generation
  - [ ] Generate comprehensive educational content
- [ ] Task 3: Update course generation workflow (AC: 1, 2, 7)
  - [ ] Update `backend/orchestration/workflows/course_generation_workflow.py`
  - [ ] Add unit generation step
  - [ ] Add module content generation step
  - [ ] Sequence generation tasks correctly
  - [ ] Handle workflow completion
- [ ] Task 4: Store unit and module content (AC: 5)
  - [ ] Update knowledge base service
  - [ ] Store unit structures
  - [ ] Store module content
  - [ ] Link to course hierarchy

## Dev Notes

- **Architecture Patterns**: Sequential content generation. Hierarchical content structure. Agent coordination.
- **Source Tree Components**:
  - `backend/app/services/agents/curriculum_designer_agent.py` - Updated for unit generation
  - `backend/app/services/agents/content_generator_agent.py` - Content Generator Agent
  - `backend/orchestration/workflows/course_generation_workflow.py` - Updated workflow
  - `backend/app/services/knowledge/knowledge_base.py` - Knowledge base storage
- **Testing Standards**: Unit tests for agents, integration tests for workflow, E2E tests for generation
- **Dependencies**: Story 4.5 must be complete (Course introduction generation)
- **Sequencing**: Generate units first, then modules within each unit. Maintain proper order.

### Project Structure Notes

- **Alignment**: Unit/module generation follows architecture.md content generation patterns
- **Agent Coordination**: Curriculum Designer creates structure, Content Generator creates content
- **Hierarchy**: Maintain Course → Unit → Module relationships in database
- **Content Quality**: Ensure generated content is comprehensive and educational

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Content Generation] - Unit/module generation patterns (lines 2583-2588)
- [Source: _bmad-output/planning-artifacts/prd.md#FR7, FR16, FR17] - FR7: Course Structure, FR16-17: Content Generation requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 4.6] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
