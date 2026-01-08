# Story 4.1: Coordinate Multiple Specialized Agents for Content Generation

Status: ready-for-dev

## Story

As the system,
I want to coordinate multiple specialized agents,
so that content generation tasks are distributed efficiently.

## Acceptance Criteria

1. **Given** A course generation request is received **When** The orchestration system processes the request **Then** Tasks are routed to appropriate specialized agents (Curriculum Designer, Research, Content Generator, QA)
2. **Given** A course generation request is received **When** The orchestration system processes the request **Then** Agent coordination follows hierarchical orchestration pattern with Master Orchestrator
3. **Given** A course generation request is received **When** The orchestration system processes the request **Then** Agent tasks are queued and executed in the correct sequence
4. **Given** A course generation request is received **When** The orchestration system processes the request **Then** Agent communication uses JSON-RPC 2.0 protocol
5. **Given** A course generation request is received **When** The orchestration system processes the request **Then** Task dependencies are managed correctly
6. **Given** A course generation request is received **When** The orchestration system processes the request **Then** Agent coordination is logged for monitoring

## Tasks / Subtasks

- [ ] Task 1: Set up Prefect orchestration (AC: 2, 3, 5)
  - [ ] Configure Prefect in `backend/orchestration/`
  - [ ] Create Prefect flow for course generation
  - [ ] Define task dependencies
  - [ ] Configure task sequencing
- [ ] Task 2: Create Master Orchestrator (AC: 2)
  - [ ] Create `backend/app/services/orchestration/master_orchestrator.py`
  - [ ] Implement hierarchical orchestration pattern
  - [ ] Coordinate specialized agents
  - [ ] Manage workflow execution
- [ ] Task 3: Create agent interfaces (AC: 1, 4)
  - [ ] Create base agent interface/abstract class
  - [ ] Define JSON-RPC 2.0 communication protocol
  - [ ] Create agent communication utilities
  - [ ] Implement request/response handling
- [ ] Task 4: Create specialized agent placeholders (AC: 1)
  - [ ] Create `backend/app/services/agents/curriculum_designer_agent.py` placeholder
  - [ ] Create `backend/app/services/agents/research_agent.py` placeholder
  - [ ] Create `backend/app/services/agents/content_generator_agent.py` placeholder
  - [ ] Create `backend/app/services/agents/qa_agent.py` placeholder
  - [ ] Each agent implements base interface
- [ ] Task 5: Create task queue system (AC: 3)
  - [ ] Configure RabbitMQ for task queuing
  - [ ] Create task queue utilities
  - [ ] Implement task routing
  - [ ] Handle task execution order
- [ ] Task 6: Implement logging (AC: 6)
  - [ ] Add orchestration logging
  - [ ] Log agent coordination events
  - [ ] Log task execution
  - [ ] Use correlation IDs for tracking

## Dev Notes

- **Architecture Patterns**: Hierarchical orchestration with Prefect. JSON-RPC 2.0 for agent communication. Task queuing with RabbitMQ.
- **Source Tree Components**: 
  - `backend/orchestration/workflows/course_generation_workflow.py` - Prefect workflow
  - `backend/app/services/orchestration/master_orchestrator.py` - Master orchestrator
  - `backend/app/services/agents/*.py` - Specialized agents
  - `backend/app/utils/agent_communication.py` - JSON-RPC 2.0 utilities
  - `backend/app/utils/task_queue.py` - Task queue utilities
- **Testing Standards**: Unit tests for orchestrator, integration tests for agent coordination, workflow tests
- **Dependencies**: Epic 1 must be complete (Prefect, RabbitMQ, infrastructure)
- **Orchestration**: Use Prefect for workflow orchestration. Master Orchestrator coordinates specialized agents.

### Project Structure Notes

- **Alignment**: Agent orchestration follows architecture.md orchestration patterns. Hierarchical structure.
- **JSON-RPC 2.0**: Use for agent-to-agent communication. Standardized protocol for inter-agent messaging.
- **Task Dependencies**: Manage dependencies in Prefect workflow. Ensure correct execution order.
- **Logging**: Comprehensive logging for monitoring and debugging agent coordination.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Agent Orchestration] - Orchestration patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR6, FR41, FR42] - FR6: Agent Coordination, FR41-42: Orchestration requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 4.1] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

