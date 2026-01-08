---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments:
  - _bmad-output/planning-artifacts/prd.md
  - _bmad-output/planning-artifacts/research/technical-agent-orchestration-patterns-research.md
  - _bmad-output/planning-artifacts/research/technical-autonomous-content-generation-research.md
  - _bmad-output/planning-artifacts/research/technical-free-integrations-research.md
  - _bmad-output/planning-artifacts/research/technical-multi-agent-architectures-research.md
  - _bmad-output/analysis/brainstorming-session.md
workflowType: 'architecture'
project_name: 'agent-teacher'
user_name: 'Casey'
date: '2026-01-07T14:30:00.000Z'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

## Project Context Analysis

### Requirements Overview

**Functional Requirements:**
- 88 functional requirements organized into 9 categories: User Account Management, Course Management, Content Generation & Quality, Learning & Assessment, Interactive Tutoring, Progress Tracking, Multi-Agent Orchestration, Self-Improvement & Optimization, and Platform Administration
- Core functionality centers on autonomous multi-agent content generation with real-time interactive tutoring and self-improving platform capabilities
- Autonomous system requirements: agents must coordinate, monitor health, handle failures, and optimize performance without human intervention

**Non-Functional Requirements:**
- **Performance**: 3-second tutoring responses (95th percentile), 30-minute course generation, 5-second assessment grading
- **Concurrency**: 5,000 concurrent users, 1,000 simultaneous WebSocket sessions, 5-20 concurrent long-running workflows
- **Security**: AES-256 encryption at rest, TLS 1.3+ in transit, GDPR compliance, EdTech considerations (COPPA/FERPA awareness)
- **Scalability**: Horizontal scaling to 50,000 users within 12 months, 10x growth with <10% performance degradation
- **Accessibility**: Full WCAG 2.1 AA compliance, keyboard navigation, screen reader support
- **Reliability**: 99.5% uptime target, 30-second agent failure detection, 2-minute automatic recovery

**Scale & Complexity:**
- **Primary domain**: Full-stack web application (MPA) with sophisticated multi-agent backend orchestration
- **Complexity level**: High/Enterprise — Complex orchestration with autonomous capabilities, real-time interactions, and self-improving systems
- **Estimated architectural components**: 
  - 17+ specialized agents requiring coordination
  - Two-layer knowledge architecture (Supabase + mem0)
  - Real-time WebSocket infrastructure
  - API gateway for external integrations
  - Self-improvement feedback systems
  - Quality assurance and monitoring infrastructure

### Technical Constraints & Dependencies

**Critical Architectural Decisions Required:**

**1. Agent Orchestration Pattern Selection:**
- **Hybrid Orchestration Required**: System needs both sequential (content generation pipeline) and concurrent (research + curriculum design) patterns
- **Recommended Pattern**: Hierarchical Orchestration with Master Orchestrator
  - Multi-level structure with Master Orchestrator coordinating specialized agents
  - Supports 20 concurrent long-running workflows without resource contention
  - Prevents deadlocks through clear task dependencies and resource allocation
- **Orchestration Framework Options**:
  - **Primary Recommendation**: Prefect (modern, Python-native, excellent observability, free tier)
  - **Alternative**: Apache Airflow (mature, extensive ecosystem, self-hosted free)
  - **Lightweight Option**: Celery (simple, good for basic task queues)
- **Workflow State Management**: Persistent state in database with in-memory caching for active workflows
- **Resource Contention Prevention**: Task queues with priority-based routing, resource pools per agent type

**2. Agent Communication Protocols & Data Contracts:**
- **Primary Protocol**: JSON-RPC 2.0 for agent-to-agent communication
  - Lightweight, method-based, supports batch operations
  - Clear request/response patterns with structured data
  - Standardized across all agent interfaces
- **Secondary Protocol**: REST APIs for orchestrator-to-agent task assignment
  - Resource-based URLs (`/agents/{agent_id}/tasks`, `/workflows/{workflow_id}/status`)
  - HTTP status codes for workflow states
  - JSON payloads for structured data exchange
- **Real-Time Communication**: WebSocket for interactive tutoring (1,000 simultaneous sessions)
  - FastAPI WebSocket support (Python, free)
  - Session persistence and graceful reconnection
- **Asynchronous Communication**: Message Queues for decoupled agent communication
  - **Primary**: RabbitMQ (AMQP protocol, reliable delivery, complex routing, self-hosted free)
  - **Alternative**: Redis Pub/Sub (low latency, simple pub/sub, free tier available)
- **Event-Driven Patterns**: Publish-Subscribe for agent event distribution
  - Event sourcing for workflow state reconstruction
  - Blackboard pattern via message streaming topics
  - Agents publish events, subscribing agents receive relevant events

**3. Technology Stack Decisions Required:**
- **Python**: Confirmed for all agent logic (dominant language for AI agents, LLM integration, workflow management)
- **Web Framework**: Need decision on:
  - **FastAPI** (recommended): Modern, async support, built-in WebSocket, excellent performance, auto-generated OpenAPI docs
  - **Django**: Full-featured, mature, higher overhead
  - **Flask**: Lightweight, flexible, requires more manual setup
- **Orchestration**: Prefect or Airflow (see orchestration pattern above)
- **Agent Framework**: pydantic-ai (type-safe, model-agnostic, built by Pydantic team, structured outputs with validation, dependency injection)
- **Database ORM**: SQLAlchemy (Python standard, works with Supabase PostgreSQL)
- **WebSocket Solution**: Native FastAPI WebSocket support (no additional library needed)

**4. State Management Patterns:**
- **Workflow State**: Persistent state in Supabase with in-memory Redis cache for active workflows
- **Agent State**: Stateless agent design with state stored externally (Supabase, mem0)
- **Event Sourcing**: Store all state changes as events for audit trail and state reconstruction
- **Consistency Strategy**: 
  - Strong consistency for Supabase (curriculum knowledge - ACID compliance)
  - Eventual consistency for mem0 (optimization learnings - acceptable for non-critical updates)

**5. Error Propagation & Handling:**
- **Circuit Breaker Pattern**: Prevent cascading failures when agents fail
  - Health checks every 30 seconds
  - Automatic recovery within 2 minutes
  - Fallback mechanisms for critical workflows
- **Retry Mechanisms**: Exponential backoff for transient failures
  - Configurable retry attempts per agent type
  - Dead letter queues for failed tasks
- **Error Propagation**: Structured error responses through JSON-RPC protocol
  - Error codes per error type
  - Error messages with context
  - Workflow-level error aggregation

**6. Cost Management for External LLM/API Services:**
- **API Gateway Pattern**: Centralized gateway (Kong or Apache APISIX) for all external API calls
  - Unified rate limiting per service
  - Request/response transformation
  - Cost monitoring and alerts
- **Rate Limiting Strategy**: 
  - Per-service rate limits to prevent overruns
  - Priority queues for critical operations
  - Automatic throttling when approaching limits
- **Cost Monitoring**: Real-time usage tracking with budget alerts
  - Monthly cost caps per service
  - Automatic suspension on budget breach (with admin override)
  - Usage reporting and optimization recommendations

### Compliance Complexity (Detailed)

**GDPR Requirements:**
- **Data Deletion**: Right to deletion within 30 days (FR71)
- **Data Retention**: 3 years for active user accounts, 90 days after deletion request
- **Right to Access**: Users can request all their data (account, progress, assessments)
- **Data Portability**: Users can export their data in machine-readable format
- **Consent Management**: Explicit consent for data processing, cookie consent
- **Audit Trail**: Comprehensive logging of all data access and modifications (FR73)

**EdTech Considerations (COPPA/FERPA Awareness):**
- **COPPA (Children's Online Privacy Protection Act)**:
  - If users under 13: Parental consent required, limited data collection, no behavioral advertising
  - Age verification mechanisms required
  - Simplified privacy policies for children
- **FERPA (Family Educational Rights and Privacy Act)**:
  - Student educational records protection (if applicable to institutional use)
  - Access controls for educational data
  - Disclosure limitations for student information
- **Data Isolation Requirements**:
  - Separate data storage for educational vs. user profile data
  - Encryption at rest for all student data
  - Access controls restricting agent access to only necessary student data
- **Consent Flow Management**: 
  - Age-appropriate consent mechanisms
  - Parent/guardian consent workflows (if applicable)
  - Clear privacy policies for educational context

**Audit Trail Requirements:**
- **User Actions**: Log all user actions for audit and debugging (FR73)
- **Agent Activities**: Comprehensive logging of all agent operations (FR45)
- **Data Access**: Log all data access for compliance verification
- **Security Events**: Monitor and log failed API calls, authentication failures, suspicious activity

### Performance Degradation Strategy

**Under Load Scenarios:**
1. **Tutoring Sessions Exceed 1,000**:
   - Automatic horizontal scaling of WebSocket server instances
   - Load balancing across WebSocket instances
   - Queue new sessions if all instances at capacity
   - Graceful degradation: Show "busy" message, queue position, estimated wait time
   - Fallback: Queue tutoring requests, process when capacity available

2. **Course Generation Requests Exceed 20 Concurrent**:
   - Priority queue for course generation requests
   - Admin/urgent requests processed first
   - User requests queued with estimated completion time
   - Rate limiting: Max 20 concurrent, additional requests queued
   - Graceful degradation: Notify users of queue position, provide estimated wait time

3. **System Under High Load (5,000+ Concurrent Users)**:
   - Automatic resource scaling (horizontal scaling of application servers)
   - Increase database connection pools
   - Enable aggressive caching (Redis)
   - Defer non-critical operations (analytics, background jobs)
   - Graceful degradation: Prioritize core features (course access, progress tracking), defer enhancements

4. **Agent Failure During High Load**:
   - Circuit breaker activates automatically
   - Fallback agents or cached responses
   - User notification of degraded service
   - Automatic recovery when agent restored

5. **Database/API Under Heavy Load**:
   - Read replicas for Supabase queries
   - Aggressive caching layer (Redis)
   - API rate limiting with queuing
   - Graceful degradation: Serve cached content with staleness indicators

### Cross-Cutting Concerns Identified

**1. Agent Orchestration & Coordination (RESOLVED):**
- **Pattern**: Hierarchical Orchestration with Master Orchestrator
- **Framework**: Prefect (primary) or Airflow (alternative)
- **Concurrency**: Supports 20 concurrent workflows through task queues and resource pooling
- **State Management**: Persistent workflow state in Supabase, in-memory cache for active workflows
- **Deadlock Prevention**: Clear task dependencies, resource allocation, priority queues

**2. Agent Communication & State Management (RESOLVED):**
- **Primary Protocol**: JSON-RPC 2.0 for agent-to-agent communication
- **Secondary Protocol**: REST APIs for orchestrator-to-agent task assignment
- **Real-Time**: WebSocket (FastAPI) for interactive tutoring
- **Asynchronous**: RabbitMQ message queues for decoupled communication
- **Event-Driven**: Pub/Sub pattern for agent event distribution
- **Data Contracts**: Standardized JSON-RPC request/response schemas per agent type (enforced by pydantic-ai Pydantic models)
- **State Management**: Stateless agents with external state storage (Supabase, mem0) - pydantic-ai dependency injection facilitates service access
- **Error Propagation**: Structured JSON-RPC error responses with codes and context (validated by Pydantic models)
- **pydantic-ai Alignment**: Framework's structured outputs with Pydantic validation ensure all JSON-RPC messages conform to schemas, providing type safety and preventing communication errors

**3. Self-Improvement Architecture & Safety (RESOLVED):**
- **Specific Metrics & Thresholds** (from PRD):
  - **Content Quality**: 20% quarter-over-quarter improvement (baseline established at launch)
  - **Error Rates**: 50% reduction within 6 months (baseline established at launch)
  - **Generation Speed**: 30% improvement within 6 months (baseline established at launch)
  - **Agent Autonomy**: 60% baseline → 85% target within 6 months (percentage of decisions without human feedback)
  - **Agent Performance Feedback**: 25% improvement in positive feedback scores within 6 months (baseline established at launch)
- **Oscillation Prevention**:
  - Metrics tracking with revision system to prevent contradictory optimization cycles
  - Impact statements required for all mem0 entries (e.g., "This instance prevented this step from being adequately completed")
  - Conflict resolution: Query mem0 before writing, revise or remove conflicting entries
  - Tracking optimization change impact to prevent negative feedback loops
- **Autonomous Optimization Boundaries**:
  - **Can Autonomously Optimize**: Content generation speed, content quality improvements, agent workflow efficiency, caching strategies, API usage optimization
  - **Requires Human Oversight**: Security changes, data retention policy changes, compliance modifications, major architectural changes, user data handling changes
- **Acceptable Failure Modes When Self-Improvement Triggers Conflicting Updates**:
  - Version conflict resolution: Maintain multiple content versions, in-progress learners continue with original version
  - State alignment: Track learner progress against content version, migrate progress when appropriate
  - Rollback mechanism: Automatic rollback if quality degrades (FR70)
  - User notification: Clear communication when content updates affect their learning experience

**4. External API Management (RESOLVED):**
- **Pattern**: Centralized API Gateway (Kong or Apache APISIX)
- **Functionality**: 
  - Unified rate limiting per service
  - Cost monitoring and budget alerts
  - Request/response transformation
  - Authentication and authorization
  - Retry logic with exponential backoff
- **Fallback Strategies**:
  - Queue requests when rate limits hit
  - Serve cached responses with staleness indicators
  - Graceful degradation: Notify users of service unavailability
  - Automatic retry with exponential backoff

**5. Knowledge Base Architecture (RESOLVED):**
- **Two-Layer Architecture**:
  - **Supabase (Static Knowledge)**: Topic-specific curriculum, Research Agent writes, all agents read, query at generation start (snapshot consistency)
  - **mem0 (Semantic Memory)**: Performance optimization, agent-specific improvements, real-time querying during operations
- **Query Patterns**:
  - **Content Generator**: Full research (vector search + Supabase) at generation start
  - **Interactive Tutor**: Concise summaries (vector search only) during live sessions
- **Access Control**:
  - **Supabase Write Access**: Research Agent only
  - **mem0 Write Access**: Agents with content review/improvement/feedback responsibilities + agents encountering efficiency improvements
  - **Read Access**: All agents can query both layers
- **Conflict Resolution**: Query mem0 before writing, revise/remove conflicting entries, all entries require metrics or impact statements

**6. Testing Strategy for Multi-Agent Systems (RESOLVED):**
- **Unit Testing**:
  - Test individual agent logic in isolation
  - Mock external dependencies (APIs, databases, other agents)
  - Validate agent decision-making and output generation
  - **Framework**: pytest (free, Python)
- **Integration Testing**:
  - Test agent-to-agent communication (JSON-RPC)
  - Validate workflow orchestration (Prefect/Airflow)
  - Test data flow between agents
  - Verify API gateway routing and rate limiting
  - **Framework**: pytest with fixtures, Testcontainers for real dependencies
- **End-to-End Testing**:
  - Test complete workflows from trigger to completion (content generation pipeline)
  - Validate multi-agent collaboration scenarios
  - Test failure recovery and retry mechanisms
  - Verify quality gates and workflow restarts
  - **Framework**: Playwright (free, browser automation)
- **Agent-Based Modeling & Simulation**:
  - Test system under various scenarios (high load, agent failures, network latency)
  - Understand emergent behaviors
  - Validate robustness before deployment
  - **Scenarios**: High load (many concurrent workflows), agent failures (single/multiple), network latency, resource contention, data inconsistency

**7. Developer Experience & Implementation Patterns (RESOLVED):**
- **Agent Interface Definitions**:
  - Standardized JSON-RPC interface per agent type
  - OpenAPI/Swagger documentation for all agent APIs
  - Type definitions using Pydantic BaseModel for all data contracts (pydantic-ai enforces type safety)
- **Agent Contracts**:
  - Input/output schemas defined as Pydantic models (automatically validated by pydantic-ai)
  - Error response formats standardized using Pydantic validation
  - Versioning strategy for agent interfaces (semantic versioning)
- **pydantic-ai Integration Benefits**:
  - **Structured Outputs**: Pydantic models ensure all JSON-RPC responses conform to schemas, eliminating type errors
  - **Type Safety**: Static type checking with mypy, runtime validation with Pydantic
  - **Dependency Injection**: Agents can inject Supabase, mem0, and other services through pydantic-ai's DI system
  - **Model-Agnostic**: Easy switching between LLM providers (OpenAI, Anthropic, Gemini, etc.) for cost optimization
  - **Observability**: Built-in integration with Pydantic Logfire for debugging, monitoring, and cost tracking
- **Developer Documentation**:
  - Agent creation guide with templates
  - Communication protocol documentation
  - Testing guidelines and examples
  - Deployment procedures
- **Code Quality Standards**:
  - Linting: Black, Ruff, Flake8 (Python)
  - Type checking: mypy (Python)
  - Pre-commit hooks for quality checks
  - Code review requirements

**8. Real-Time Communication Infrastructure (RESOLVED):**
- **WebSocket Solution**: FastAPI native WebSocket support
- **Capacity**: 1,000 simultaneous tutoring sessions
- **Scaling**: Horizontal scaling with load balancing across WebSocket instances
- **Session Management**: 
  - Session persistence in Supabase
  - Session restoration on reconnection
  - Session timeout handling (24-hour inactivity)
- **Reconnection Handling**:
  - Automatic reconnection with exponential backoff
  - State synchronization on reconnection
  - Graceful handling of connection loss
- **Performance Target**: Sub-3-second response time (95th percentile)

**9. Content Versioning & Consistency (RESOLVED):**
- **Version History**: Full content version history maintained (FR65)
- **Update Isolation**: 
  - In-progress learners continue with original version (FR64)
  - New learners receive latest version
  - Progress tracked against content version
- **State Alignment**: 
  - Maintain learner-content state alignment during updates (FR64)
  - Version migration strategy for progress tracking
- **Storage Lifecycle**: Hot/archive/cleanup management (FR67)
  - Active content: Hot storage (fast access)
  - Older versions: Archive storage
  - Cleanup policies: Retention periods defined

**10. Security & Access Control (RESOLVED):**
- **RBAC**: Learners, Administrators, System Agents with separate permissions
- **Credential Management**: Secure key storage (environment variables, secrets management)
- **API Authentication**: JWT tokens for API endpoints (except public course discovery)
- **Session Management**: 24-hour inactivity expiration (per NFR)
- **Agent Authentication**: mTLS for agent-to-agent communication (zero trust architecture)
- **Network Security**: Firewall, VPN, network isolation between agent network and user-facing network

### Architectural Risks & Validation Strategy

**High-Risk Areas Requiring Early Validation:**

**1. Multi-Agent Orchestration Complexity:**
- **Risk**: 17+ agents coordinating may create deadlocks, resource contention, or unpredictable behavior
- **Mitigation**: Start with simpler MVP orchestration (5-7 core agents), validate patterns, then scale to full agent set
- **Validation**: Integration tests for agent coordination, load testing with concurrent workflows, agent-based simulation
- **Success Criteria**: Zero deadlocks in 1000 workflow executions, 95% workflow completion rate, <2% resource contention

**2. Self-Improvement Safety:**
- **Risk**: Autonomous optimization may create negative feedback loops, degrade quality, or create security vulnerabilities
- **Mitigation**: Clear boundaries on autonomous optimization vs human oversight, metrics tracking with oscillation prevention
- **Validation**: Monitor metrics monthly, set intervention thresholds, human review for boundary-pushing changes
- **Success Criteria**: No negative feedback loops, quality improvements within 10% of targets, zero security incidents from autonomous changes

**3. Performance Under Load:**
- **Risk**: System may not meet performance targets (3-second tutoring, 30-minute course generation) under full load
- **Mitigation**: Performance degradation strategy defined above, horizontal scaling, caching, load testing
- **Validation**: Load testing with target concurrency (5,000 users, 1,000 WebSocket sessions, 20 concurrent workflows)
- **Success Criteria**: 95th percentile response times meet targets under load, <10% performance degradation at 2x load

**4. Agent Communication Reliability:**
- **Risk**: Agent-to-agent communication failures may disrupt workflows
- **Mitigation**: JSON-RPC protocol with retry logic, message queues for reliability, circuit breakers
- **Validation**: Chaos engineering (simulate agent failures), integration tests with network failures
- **Success Criteria**: 99.9% message delivery success, automatic recovery within 2 minutes, graceful degradation on failures

**MVP Strategy Considerations:**
- **Balance**: User value vs architectural complexity
- **Approach**: Start with validated MVP orchestration (5-7 core agents), then scale complexity as user value proven
- **Core MVP Agents**: Master Orchestrator, Curriculum Designer, Research Agent, Content Generator, QA/Review Agent, Interactive Tutor, Assessment Creator
- **Validation**: MVP demonstrates autonomous content generation with quality parity to traditional platforms
- **Scaling**: Add remaining agents incrementally after MVP validation

### Technology Stack Recommendations (Concrete)

**Orchestration Framework:**
- **Primary**: Prefect (modern, Python-native, excellent observability, free tier, built-in retry logic)
- **Alternative**: Apache Airflow (mature, extensive ecosystem, self-hosted free, requires more setup)

**Agent Framework:**
- **Primary**: pydantic-ai (type-safe agent framework by Pydantic team, model-agnostic support for OpenAI/Anthropic/Gemini/etc., structured outputs with Pydantic validation, dependency injection system, observability with Pydantic Logfire, durable execution and streaming support)
  - **Why pydantic-ai**: Aligns perfectly with JSON-RPC communication requirements (structured outputs ensure type-safe data contracts), model-agnostic approach supports cost optimization across providers, Pydantic validation ensures reliable agent outputs, dependency injection enables modular agent architecture, and built-in observability supports monitoring requirements

**Web Framework:**
- **Primary**: FastAPI (modern, async support, built-in WebSocket, excellent performance, auto-generated OpenAPI docs, Python-native)

**Message Queue:**
- **Primary**: RabbitMQ (AMQP protocol, reliable delivery, complex routing, self-hosted free, dead letter queues)
- **Alternative**: Redis Pub/Sub (low latency, simple, free tier available, less features)

**API Gateway:**
- **Primary**: Kong (open-source, extensive plugin ecosystem, rate limiting, authentication)
- **Alternative**: Apache APISIX (open-source, high performance, cloud-native)

**Database:**
- **Confirmed**: Supabase (PostgreSQL, free tier, real-time subscriptions, authentication built-in)

**Semantic Memory:**
- **Confirmed**: mem0 (semantic memory layer, vector search capabilities)

**Testing Frameworks:**
- **Unit/Integration**: pytest (Python standard, extensive ecosystem)
- **E2E**: Playwright (free, browser automation, WebSocket testing support)
- **Load Testing**: Locust (free, Python-based, easy agent workflow simulation)

**Monitoring & Observability:**
- **Metrics**: Prometheus (free, time-series database, agent metrics)
- **Logs**: Loki (free, log aggregation, integrates with Grafana)
- **Traces**: Jaeger (free, distributed tracing, track requests across agents)
- **Dashboards**: Grafana (free, visualization, integrates with Prometheus/Loki/Jaeger)

This comprehensive analysis addresses all critical gaps identified in the Party Mode discussion, providing concrete recommendations, specific patterns, and detailed strategies for architectural decision-making.

## Starter Template Evaluation

### Primary Technology Domain

**Full-Stack Web Application (MPA - Multi-Page Application)** based on project requirements analysis:
- FastAPI backend (Python) - confirmed from technology stack recommendations
- Server-side rendered pages for SEO optimization (PRD requirement)
- Client-side enhancements for interactive features
- Multi-agent orchestration backend

### Starter Options Considered

**Evaluated Starter Templates:**
1. **FastAPI-React Starters** - Most available FastAPI starters are React SPA-based, which conflicts with MPA architecture requirement
2. **FastAPI Cookiecutter Templates** - Limited options for MPA/server-side rendering
3. **Custom FastAPI Scaffold** - Recommended approach using FastAPI's built-in Jinja2 template support

**Key Finding:** Separating frontend and backend provides better scalability, independent deployment, and allows us to use the best tool for each job: FastAPI for backend API and Next.js for frontend SSR/SSG.

### Selected Starter: Custom FastAPI Backend + Next.js Frontend (Separate Folders)

**Rationale for Selection:**
- **Separate Frontend/Backend**: Clean separation of concerns, independent deployment, better scalability
- **MPA Architecture**: Next.js provides excellent server-side rendering for SEO requirements from PRD
- **FastAPI Backend**: API-only backend, clean separation, easy to scale independently
- **Next.js Frontend**: Best-in-class SSR/SSG capabilities, excellent developer experience, strong TypeScript support
- **WebSocket Support**: FastAPI backend has native WebSocket support for 1,000 simultaneous tutoring sessions
- **Flexibility**: Custom scaffold allows us to structure the project exactly as needed for multi-agent architecture
- **Best Practices**: Can incorporate FastAPI and Next.js best practices for production deployments

**Initialization Approach:**
We'll create a structured project scaffold with separate frontend and backend:
- **Backend**: FastAPI API-only structure (JSON responses, no templates)
- **Frontend**: Next.js application with App Router for SSR/SSG
- **Communication**: Frontend calls backend API via HTTP client
- **Multi-agent service architecture**: Organized in backend folder
- **Project organization patterns**: Clear separation between frontend and backend
- **Development tooling setup**: Separate tooling for each (uv for backend, npm/pnpm for frontend)

**Initialization Commands:**

**Backend Setup:**
```bash
cd backend

# Core FastAPI and web dependencies
uv add fastapi uvicorn[standard] python-multipart aiofiles

# Database and ORM
uv add sqlmodel supabase python-dotenv alembic

# Authentication and security
uv add python-jose[cryptography] passlib[bcrypt] pydantic-settings

# Agent framework and orchestration
uv add pydantic-ai prefect

# Message queue and async communication
uv add pika redis redis celery

# WebSocket support (built into FastAPI)
uv add websockets

# API client for testing
uv add httpx

# Development dependencies
uv add --dev pytest pytest-asyncio black ruff mypy flake8 pre-commit
uv add --dev testcontainers playwright

# Production dependencies
uv add gunicorn
```

**Frontend Setup:**
```bash
cd frontend

# Initialize Next.js project
npx create-next-app@latest . --typescript --tailwind --app --no-src-dir --import-alias "@/*"

# Install additional dependencies
npm install axios  # HTTP client for backend API
npm install @tanstack/react-query  # Data fetching and caching
npm install zustand  # State management (if needed)

# Development dependencies
npm install --save-dev @types/node @types/react @types/react-dom
```

### Architectural Decisions Provided by Starter

**Language & Runtime:**
- **Python 3.12+** (confirmed from project context)
- **FastAPI** web framework for async Python
- **Uvicorn** ASGI server for production deployment
- **TypeScript/JavaScript**: None - Python-only stack for backend, vanilla JavaScript for client-side enhancements

**Templating & Frontend (Separate Folders):**
- **Frontend/Backend Separation**: Frontend and backend in separate folders (`frontend/` and `backend/`)
- **Backend**: FastAPI API only (JSON responses, no templates)
- **Frontend**: Separate application serving MPA pages

**Frontend Decision: Next.js Frontend (Selected)**
- **Next.js** app with Server-Side Rendering (SSR) for SEO
- Calls backend FastAPI API via HTTP client
- **Pros**: Strong SSR/SSG capabilities, excellent SEO support, rich frontend ecosystem, modern tooling
- **Cons**: Requires Node.js in addition to Python, more complex deployment
- **Rationale**: Best-in-class SSR for MPA architecture, excellent developer experience, strong TypeScript support

**Build Tooling:**
- **Backend**: uv for Python dependencies
- **Frontend**: npm or pnpm for Node.js dependencies (Next.js)
- **Build Step**: Next.js build process for production (SSR/SSG optimization)
- **Asset Optimization**: Next.js handles minification, code splitting, image optimization automatically

**Testing Framework:**
- **pytest**: Unit and integration testing (confirmed from technology stack)
- **httpx**: Async HTTP client for testing FastAPI endpoints
- **Testcontainers**: For integration testing with real dependencies
- **Playwright**: End-to-end testing (confirmed from technology stack)

**Code Organization:**
- **Backend**: FastAPI router pattern, API endpoints only (JSON responses)
- **Frontend**: Separate FastAPI app (if Option A) serving Jinja2 templates, calls backend API
- **API Communication**: Frontend makes HTTP requests to backend API
- **Static Assets**: CSS/JavaScript organized by component/page in frontend folder
- **Configuration**: Separate configs for backend and frontend
- **Models**: SQLModel models in backend, API response models shared via Pydantic

**Development Experience:**
- **Hot Reloading**: Uvicorn automatic reload during development
- **Type Checking**: mypy for Python type checking
- **Linting**: Black, Ruff, Flake8 (confirmed from technology stack)
- **Pre-commit Hooks**: Quality checks before commits
- **API Documentation**: FastAPI auto-generates OpenAPI/Swagger docs

**Project Structure Pattern (Detailed) - Separate Frontend/Backend:**
```
agent-teacher/
├── backend/                         # FastAPI backend API only
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app initialization (API only)
│   │   ├── config.py                # Configuration management
│   │   ├── dependencies.py          # FastAPI dependencies
│   │   ├── middleware.py            # Custom middleware
│   │   │
│   │   ├── api/                     # API routes (JSON responses only)
│   │   │   ├── __init__.py
│   │   │   ├── v1/                  # API version 1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── courses.py       # Course API endpoints
│   │   │   │   ├── learning.py      # Learning API endpoints
│   │   │   │   ├── tutoring.py      # WebSocket tutoring endpoints
│   │   │   │   ├── assessments.py   # Assessment API endpoints
│   │   │   │   ├── admin.py         # Admin API endpoints
│   │   │   │   └── auth.py          # Authentication API endpoints
│   │   │   └── v2/                  # Future API version 2
│   │   │
│   │   ├── services/                # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── agents/              # Agent service integration
│   │   │   │   ├── __init__.py
│   │   │   │   ├── orchestrator.py
│   │   │   │   ├── curriculum.py
│   │   │   │   ├── research.py
│   │   │   │   ├── content.py
│   │   │   │   ├── tutor.py
│   │   │   │   └── ...
│   │   │   ├── orchestration/       # Prefect workflow integration
│   │   │   ├── knowledge/           # Supabase/mem0 integration
│   │   │   ├── course.py
│   │   │   ├── assessment.py
│   │   │   └── progress.py
│   │   │
│   │   ├── models/                  # Pydantic/SQLModel models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── course.py
│   │   │   ├── assessment.py
│   │   │   ├── progress.py
│   │   │   └── agent.py
│   │   │
│   │   └── utils/                   # Helper functions
│   │       ├── __init__.py
│   │       ├── security.py
│   │       ├── validation.py
│   │       ├── logging.py
│   │       └── errors.py
│   │
│   ├── agents/                      # Agent implementations
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── curriculum_designer/
│   │   ├── research/
│   │   ├── content_generator/
│   │   ├── tutor/
│   │   └── ...
│   │
│   ├── orchestration/               # Prefect workflows
│   │   ├── __init__.py
│   │   ├── workflows/
│   │   └── tasks/
│   │
│   ├── tests/                       # Backend test suite
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   │
│   ├── pyproject.toml               # Backend Python dependencies
│   ├── .env.example
│   ├── .env
│   ├── Dockerfile                   # Backend Docker image
│   ├── README.md
│   └── pytest.ini
│
├── frontend/                        # Next.js frontend application
│   ├── app/                         # Next.js App Router (app directory)
│   │   ├── layout.tsx               # Root layout
│   │   ├── page.tsx                 # Homepage
│   │   ├── courses/                 # Course pages
│   │   │   ├── page.tsx             # Course listing (SSR)
│   │   │   ├── [id]/page.tsx        # Course detail (SSR)
│   │   │   └── [id]/modules/[moduleId]/page.tsx  # Module content (SSR)
│   │   ├── learning/                # Learning pages
│   │   ├── assessments/            # Assessment pages
│   │   └── admin/                   # Admin pages
│   │
│   ├── components/                  # React components
│   │   ├── ui/                      # UI components
│   │   ├── course/                  # Course-related components
│   │   ├── learning/                # Learning components
│   │   └── layout/                  # Layout components (header, footer, nav)
│   │
│   ├── lib/                         # Utility libraries
│   │   ├── api/                     # Backend API client
│   │   │   ├── client.ts            # HTTP client for FastAPI backend
│   │   │   ├── websocket.ts         # WebSocket client for tutoring
│   │   │   └── endpoints.ts         # API endpoint definitions
│   │   ├── utils/                   # Utility functions
│   │   └── types/                   # TypeScript types (shared with backend)
│   │
│   ├── public/                      # Static assets
│   │   ├── images/
│   │   ├── fonts/
│   │   └── favicon.ico
│   │
│   ├── styles/                      # Global styles
│   │   └── globals.css
│   │
│   ├── package.json                 # Node.js dependencies
│   ├── tsconfig.json                # TypeScript configuration
│   ├── next.config.js               # Next.js configuration
│   ├── tailwind.config.js           # Tailwind CSS configuration (if used)
│   ├── Dockerfile                   # Frontend Docker image
│   ├── .env.local                   # Frontend environment variables
│   ├── .env.example
│   └── README.md
│
├── infrastructure/                  # Infrastructure setup
│   ├── docker/
│   │   ├── docker-compose.yml       # Local development stack (backend + frontend)
│   │   └── docker-compose.prod.yml  # Production stack
│   ├── kubernetes/                  # K8s manifests
│   └── nginx/                       # Nginx config (reverse proxy)
│
├── scripts/                         # Utility scripts
│   ├── setup_dev.sh
│   ├── migrate.py
│   └── seed_data.py
│
├── .gitignore
├── README.md                        # Root project README
└── ARCHITECTURE.md                  # Architecture documentation
```

**Configuration Files Setup:**

**pyproject.toml (uv package management):**
```toml
[project]
name = "agent-teacher"
version = "0.1.0"
description = "MENTOR-web: Autonomous learning platform with multi-agent AI"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "python-multipart>=0.0.6",
    "aiofiles>=23.2.0",
    "sqlmodel>=0.0.14",
    "supabase>=2.0.0",
    "python-dotenv>=1.0.0",
    "python-jose[cryptography]>=3.3.0",
    "passlib[bcrypt]>=1.7.4",
    "pydantic-ai>=0.0.1",
    "prefect>=2.14.0",
    "pika>=1.3.0",
    "redis>=5.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "httpx>=0.25.0",
    "black>=23.11.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
    "flake8>=6.1.0",
    "pre-commit>=3.5.0",
    "testcontainers>=4.0.0",
    "playwright>=1.40.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.black]
line-length = 100
target-version = ['py312']

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
```

**.env.example (Environment variables template):**
```bash
# Application
APP_NAME=agent-teacher
ENVIRONMENT=development
DEBUG=true
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database (Supabase)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
SUPABASE_SERVICE_KEY=your-supabase-service-key

# Semantic Memory (mem0)
MEM0_API_URL=http://localhost:8001
MEM0_API_KEY=your-mem0-api-key

# Agent Framework (pydantic-ai)
# pydantic-ai is model-agnostic - configure your LLM provider API keys:
OPENAI_API_KEY=your-openai-api-key
# ANTHROPIC_API_KEY=your-anthropic-api-key  # If using Anthropic
# GEMINI_API_KEY=your-gemini-api-key        # If using Google Gemini

# Orchestration (Prefect)
PREFECT_API_URL=http://localhost:4200/api
PREFECT_API_KEY=your-prefect-api-key

# Message Queue (RabbitMQ)
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
REDIS_URL=redis://localhost:6379/0

# API Gateway (Kong)
KONG_ADMIN_URL=http://localhost:8001
KONG_API_URL=http://localhost:8000

# External APIs
BRAVE_SEARCH_API_KEY=your-brave-api-key
YOUTUBE_API_KEY=your-youtube-api-key

# Frontend Configuration
FRONTEND_URL=http://localhost:3000  # Next.js dev server
FRONTEND_URLS=http://localhost:3000,http://localhost:3001  # CORS allowed origins

# Monitoring
PROMETHEUS_PORT=9090
LOKI_URL=http://localhost:3100
JAEGER_URL=http://localhost:16686
```

**app/config.py (Configuration management):**
```python
from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache

class Settings(BaseSettings):
    # Application
    app_name: str = "agent-teacher"
    environment: str = "development"
    debug: bool = False
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440
    
    # Database
    supabase_url: str
    supabase_key: str
    supabase_service_key: str
    
    # Semantic Memory
    mem0_api_url: str
    mem0_api_key: str
    
    # Agent Framework (pydantic-ai)
    # pydantic-ai is model-agnostic - configure your LLM provider API keys:
    openai_api_key: str  # Primary LLM provider
    anthropic_api_key: str | None = None  # Optional: if using Anthropic
    gemini_api_key: str | None = None  # Optional: if using Google Gemini
    
    # Orchestration
    prefect_api_url: str = "http://localhost:4200/api"
    prefect_api_key: str | None = None
    
    # Message Queue
    rabbitmq_url: str = "amqp://guest:guest@localhost:5672/"
    redis_url: str = "redis://localhost:6379/0"
    
    # API Gateway
    kong_admin_url: str = "http://localhost:8001"
    kong_api_url: str = "http://localhost:8000"
    
    # Frontend URLs (for CORS)
    frontend_urls: list[str] = ["http://localhost:3000", "http://localhost:3001"]  # Development + Production
    
    # External APIs
    brave_search_api_key: str | None = None
    youtube_api_key: str | None = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

**backend/app/main.py (FastAPI API structure - Updated for Next.js frontend):**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import get_settings
from app.api.v1 import courses, learning, tutoring, assessments, admin, auth
from app.middleware import setup_middleware

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize connections, start background tasks
    # Initialize Prefect client, RabbitMQ, Redis connections
    # Initialize agent services
    yield
    # Shutdown: Close connections, cleanup

app = FastAPI(
    title=settings.app_name,
    description="MENTOR-web: Autonomous learning platform API",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware - allow Next.js frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.frontend_urls,  # Frontend URLs from config
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware setup
setup_middleware(app)

# Include API routers (JSON responses only, no HTML templates)
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(courses.router, prefix="/api/v1/courses", tags=["courses"])
app.include_router(learning.router, prefix="/api/v1/learning", tags=["learning"])
app.include_router(tutoring.router, prefix="/api/v1/tutoring", tags=["tutoring"])
app.include_router(assessments.router, prefix="/api/v1/assessments", tags=["assessments"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "healthy", "service": "backend-api"}
```

**frontend/lib/api/client.ts (Backend API client for Next.js):**
```typescript
import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const apiClient = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true, // For JWT cookies
});

// Add auth token to requests
apiClient.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

// Handle token refresh on 401
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Handle token refresh or redirect to login
    }
    return Promise.reject(error);
  }
);
```

**Next.js Frontend Architecture:**
- **App Router**: Next.js 14+ App Router for file-based routing and SSR
- **Server Components**: Use React Server Components for SEO-optimized pages
- **Client Components**: Use Client Components for interactive features (tutoring chat, assessments)
- **API Routes**: Next.js API routes for server-side data fetching (calls backend API)
- **Static Generation**: Static generation for course listing pages (ISR - Incremental Static Regeneration)
- **Server-Side Rendering**: SSR for dynamic pages (user-specific content, learning progress)

**Next.js Features for MPA:**
- **SEO Optimization**: Automatic meta tags, structured data, sitemap generation
- **Image Optimization**: Built-in image optimization and lazy loading
- **Code Splitting**: Automatic code splitting for optimal performance
- **Font Optimization**: Built-in font optimization
- **Performance**: Automatic performance optimizations (compression, minification)

**Development Workflow Setup:**

**Development Server Command:**
```bash
# Development with hot reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# With specific environment
ENVIRONMENT=development uvicorn app.main:app --reload
```

**Pre-commit Configuration (.pre-commit-config.yaml):**
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-json
      - id: check-toml
  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
        language_version: python3.12
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

**Production Deployment Considerations:**

**Production ASGI Server:**
- **Uvicorn with Gunicorn**: Multiple worker processes for production
  ```bash
  gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
  ```
- **Alternative**: Uvicorn standalone with multiple workers
  ```bash
  uvicorn app.main:app --workers 4 --host 0.0.0.0 --port 8000
  ```

**Docker Support:**
- Dockerfile for containerization
- docker-compose.yml for local development (FastAPI + Supabase + RabbitMQ + Redis + mem0)
- docker-compose.prod.yml for production stack

**Static File Serving in Production:**
- FastAPI static file mounting for development
- Nginx reverse proxy for production (better performance, caching, compression)
- CDN integration (Cloudflare) for static assets

**Integration Points with Confirmed Technologies:**
- **Supabase**: SQLModel models, Supabase Python client for knowledge base queries
- **mem0**: mem0 Python SDK for semantic memory operations
- **Prefect**: Prefect Python SDK for workflow orchestration, task decorators
- **pydantic-ai**: pydantic-ai Agent framework with structured outputs, type safety, and dependency injection for agent implementations
- **RabbitMQ**: Pika client for message queue operations
- **Redis**: redis-py for caching and pub/sub
- **Kong**: HTTP client for API gateway communication (or direct integration)

**Initialization Steps (Complete):**

**1. Create Project Structure:**
```bash
# Create root directory
mkdir agent-teacher
cd agent-teacher

# Create backend structure
mkdir -p backend/{app/{api/v1,services/{agents,orchestration,knowledge},models,utils},agents,orchestration/{workflows,tasks},tests/{unit,integration,e2e}}

# Create frontend structure (Next.js will create most of this)
mkdir -p frontend

# Create shared infrastructure
mkdir -p infrastructure/{docker,kubernetes,nginx} scripts
```

**2. Backend Setup:**
```bash
cd backend
# Create pyproject.toml, .env.example, config.py, main.py (see above)
# Install dependencies
uv sync
# Set up pre-commit hooks
uv run pre-commit install
```

**3. Frontend Setup:**
```bash
cd frontend
# Initialize Next.js project
npx create-next-app@latest . --typescript --tailwind --app --no-src-dir --import-alias "@/*"
# Install additional dependencies (see above)
npm install
# Create API client structure
mkdir -p lib/api
# Create .env.local with NEXT_PUBLIC_API_URL=http://localhost:8000
```

**4. Initialize Git Repository:**
```bash
cd ..
git init
git add .
git commit -m "Initial project setup: FastAPI backend + Next.js frontend"
```

**Note:** Project initialization using this scaffold structure should be the first implementation story (Epic 1, Story 1).

## Core Architectural Decisions

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**
- ✅ Frontend/Backend Separation: Next.js frontend + FastAPI backend in separate folders
- ✅ Data Migration: Alembic for database schema migrations
- ✅ Data Validation: SQLModel with Pydantic validation (single source of truth)
- ✅ Caching: Multi-layer caching (application + agent + CDN)
- ✅ Authentication: JWT with refresh tokens
- ✅ Authorization: RBAC with permission-based checks
- ✅ API Versioning: URL path versioning (`/api/v1/`, `/api/v2/`)
- ✅ Error Handling: Standardized error response format
- ✅ Rate Limiting: Multi-level (gateway + application) with `slowapi`
- ✅ Hosting: Container-based deployment (Docker)
- ✅ CI/CD: GitHub Actions with Docker build & deploy
- ✅ Monitoring: Prometheus + Loki + Jaeger + Grafana stack

**Important Decisions (Shape Architecture):**
- ✅ Client-Side State: Alpine.js + WebSocket (Next.js handles most state via SSR)
- ✅ Component Architecture: Next.js App Router with React Server/Client Components
- ✅ Routing: Next.js file-based routing (App Router)
- ✅ Performance: Multi-level caching + Next.js automatic optimizations
- ✅ Secrets Management: Environment variables (dev) + secrets service (prod)
- ✅ Scaling: Horizontal scaling with load balancing + auto-scaling

**Deferred Decisions (Post-MVP):**
- Kubernetes orchestration (Docker Compose sufficient for MVP)
- Advanced caching strategies (basic Redis caching for MVP)
- Advanced monitoring dashboards (basic Prometheus/Grafana for MVP)
- Multi-region deployment (single region for MVP)

### Data Architecture

**Database:**
- **Technology**: Supabase (PostgreSQL) - Confirmed
- **ORM**: SQLModel - Confirmed
- **Migration Tool**: Alembic
  - **Version**: Latest stable (verify during implementation)
  - **Rationale**: Version-controlled migrations, works with SQLModel, CI/CD friendly
  - **Affects**: Database schema evolution, deployment process

**Data Validation:**
- **Approach**: SQLModel with Pydantic validation
  - **Rationale**: Single source of truth, SQLModel extends Pydantic, type safety throughout stack
  - **Affects**: All database models and API responses

**Caching Strategy:**
- **Application Cache**: Redis for frequently accessed data (course listings, user sessions)
- **Agent Cache**: Redis for agent coordination and workflow state
- **CDN Cache**: Cloudflare for static assets (images, CSS, JavaScript)
- **Cache Pattern**: Cache-aside pattern with TTL-based expiration
- **Affects**: Performance, scalability, data freshness

**Data Consistency:**
- **Supabase**: Strong consistency (ACID compliance) for curriculum knowledge
- **mem0**: Eventual consistency for optimization learnings (acceptable for non-critical updates)

### Authentication & Security

**Authentication Method:**
- **Technology**: JWT (JSON Web Tokens) with refresh tokens
  - **Access Token**: Short-lived (15-30 minutes), contains user_id, roles, permissions
  - **Refresh Token**: Long-lived (7-14 days), stored in httpOnly cookie or database
  - **Package**: `python-jose[cryptography]` - Already included
  - **Affects**: User authentication, session management, API security

**Authorization Patterns:**
- **Approach**: Role-Based Access Control (RBAC) with permission-based checks
- **Roles**: Learner, Administrator, System Agent
- **Permissions**: Fine-grained permissions (e.g., `courses:view`, `content:generate`, `admin:access`)
- **Implementation**: FastAPI dependencies for route protection
- **Affects**: All protected API endpoints, agent access control

**Security Middleware:**
- **CORS Middleware**: Configured for Next.js frontend origins
- **Security Headers**: Content-Security-Policy, X-Frame-Options, HSTS, etc.
- **Rate Limiting**: Application-level rate limiting with `slowapi`
- **Request Validation**: Pydantic models for all request/response validation
- **Affects**: All API endpoints, security posture

**API Security Strategy:**
- **API Gateway**: Kong for external API rate limiting and cost management
- **Application Level**: JWT authentication, RBAC authorization
- **Agent-to-Agent**: mTLS for agent authentication (zero trust architecture)
- **Public Endpoints**: Course discovery/browsing (GET only, no auth)
- **Protected Endpoints**: All user operations, admin operations, agent operations

**Secrets Management:**
- **Development**: `.env` files (gitignored)
- **Production**: Environment variables via deployment platform (MVP), secrets service for scale
- **Affects**: Configuration management, security

### API & Communication Patterns

**API Design:**
- **Pattern**: REST for user-facing APIs
- **Versioning**: URL path versioning (`/api/v1/`, `/api/v2/`)
- **Documentation**: FastAPI auto-generated OpenAPI/Swagger docs
- **Affects**: All API endpoints, client integration

**Error Handling:**
- **Format**: Standardized error response with error codes, messages, request IDs
- **HTTP Status Codes**: Proper status code mapping (400, 401, 403, 404, 422, 429, 500, 503)
- **Implementation**: FastAPI exception handlers
- **Affects**: All API error responses, client error handling

**Rate Limiting:**
- **Gateway Level**: Kong for external API rate limits
- **Application Level**: `slowapi` for per-user and per-IP rate limiting
- **Configuration**: Endpoint-specific limits (e.g., course generation: 5/hour)
- **Affects**: API abuse prevention, cost control

**Agent Communication:**
- **Protocol**: JSON-RPC 2.0 for agent-to-agent communication - Confirmed
- **Orchestrator Communication**: REST APIs for task assignment - Confirmed
- **Real-Time**: WebSocket (FastAPI) for interactive tutoring - Confirmed
- **Async**: RabbitMQ message queues for decoupled communication - Confirmed

### Frontend Architecture

**Frontend Framework:**
- **Technology**: Next.js (App Router) - Selected
- **Version**: Latest stable (verify during implementation with `create-next-app@latest`)
- **Rationale**: Best-in-class SSR/SSG for SEO, excellent developer experience, TypeScript support
- **Affects**: All frontend development, deployment process

**State Management:**
- **Server State**: Next.js Server Components + React Query for data fetching
- **Client State**: React hooks + Zustand (if needed for complex client state)
- **Real-Time State**: WebSocket client for tutoring session state
- **Affects**: Frontend component architecture, data flow

**Component Architecture:**
- **Pattern**: Next.js App Router with React Server Components and Client Components
- **Server Components**: Default for SEO-optimized pages (course listings, content pages)
- **Client Components**: For interactive features (tutoring chat, assessments, forms)
- **Affects**: Frontend performance, SEO, interactivity

**Routing Strategy:**
- **Approach**: Next.js file-based routing (App Router)
- **URL Structure**: `/courses`, `/courses/[id]`, `/courses/[id]/modules/[moduleId]`, etc.
- **SSR/SSG**: Server-side rendering for dynamic pages, static generation where possible
- **Affects**: SEO, page load performance, URL structure

**Performance Optimization:**
- **Next.js Automatic**: Code splitting, image optimization, font optimization, compression
- **Caching**: Next.js caching + Redis for API responses
- **CDN**: Cloudflare for static assets
- **Affects**: Page load times, user experience

**Backend API Integration:**
- **HTTP Client**: Axios for API calls
- **Data Fetching**: React Query for caching and state management
- **WebSocket**: Native WebSocket API for real-time tutoring
- **API Base URL**: Environment variable (`NEXT_PUBLIC_API_URL`)
- **Affects**: Frontend-backend communication, data flow

### Infrastructure & Deployment

**Hosting Strategy:**
- **MVP**: Railway or Render (simple container deployment)
- **Production**: AWS ECS or GCP Cloud Run (based on provider preference)
- **Approach**: Container-based deployment (Docker)
- **Affects**: Deployment process, scaling, costs

**CI/CD Pipeline:**
- **Platform**: GitHub Actions (free tier: 2,000 minutes/month)
- **Stages**: Lint → Test → Build → Deploy
- **Docker**: Build Docker images for backend and frontend
- **Deployment**: Automated deployment to staging, manual for production
- **Affects**: Development workflow, deployment process

**Environment Configuration:**
- **Development**: `.env` files (separate for backend and frontend)
- **Staging/Production**: Environment variables in deployment platform
- **Backend Config**: `pydantic-settings` reads from environment
- **Frontend Config**: Next.js environment variables (`NEXT_PUBLIC_*`)
- **Affects**: Configuration management, secrets handling

**Monitoring and Logging:**
- **Metrics**: Prometheus (time-series database)
- **Logs**: Loki (log aggregation)
- **Traces**: Jaeger (distributed tracing)
- **Dashboards**: Grafana (visualization)
- **Affects**: Observability, debugging, performance monitoring

**Scaling Strategy:**
- **Application**: Horizontal scaling with multiple FastAPI instances
- **WebSocket**: Sticky sessions (session affinity) for WebSocket connections
- **Database**: Supabase managed scaling (free tier → Pro tier)
- **Cache**: Redis clustering for horizontal scaling
- **Auto-Scaling**: Based on CPU, memory, request queue depth
- **Affects**: Capacity planning, cost management, performance

**Container Orchestration:**
- **MVP**: Docker Compose for local development and simple deployments
- **Production Scale**: Kubernetes (EKS, GKE) optional for 50,000+ users
- **Affects**: Deployment complexity, scalability

### Decision Impact Analysis

**Implementation Sequence:**
1. **Backend API Setup**: FastAPI backend with API endpoints (no templates)
2. **Frontend Setup**: Next.js frontend with App Router
3. **Database Setup**: Supabase + Alembic migrations
4. **Authentication**: JWT implementation in backend, auth flow in frontend
5. **Agent Integration**: pydantic-ai agents with Prefect orchestration
6. **WebSocket**: Real-time tutoring implementation
7. **Monitoring**: Prometheus + Loki + Jaeger + Grafana setup
8. **CI/CD**: GitHub Actions pipeline
9. **Deployment**: Docker containerization and deployment

**Cross-Component Dependencies:**
- **Frontend → Backend**: Frontend depends on backend API being available
- **Backend → Database**: Backend depends on Supabase connection
- **Backend → Agents**: Backend depends on agent services and Prefect
- **Agents → Knowledge Base**: Agents depend on Supabase and mem0
- **Agents → Message Queue**: Agents depend on RabbitMQ for communication
- **Monitoring → All Components**: Monitoring stack observes all components

**Technology Versions (To Verify During Implementation):**
- Next.js: Latest stable (verify with `create-next-app@latest`)
- FastAPI: Latest stable (verify during `uv add fastapi`)
- pydantic-ai: Latest stable (verify during `uv add pydantic-ai`)
- Prefect: Latest stable (verify during `uv add prefect`)
- Alembic: Latest stable (verify during `uv add alembic`)
- All other dependencies: Verify latest stable versions during installation

## Implementation Patterns & Consistency Rules

### Pattern Categories Defined

**Critical Conflict Points Identified:**
15 areas where AI agents could make different choices that would cause integration issues or inconsistent code patterns.

### Naming Patterns

#### Database Naming Conventions

**Standard: snake_case (PostgreSQL convention)**

**Rules:**
- **Tables**: Plural, lowercase, snake_case
  - ✅ `users`, `course_modules`, `learning_sessions`, `assessment_responses`
  - ❌ `Users`, `User`, `courseModules`, `CourseModules`

- **Columns**: Lowercase, snake_case
  - ✅ `user_id`, `created_at`, `is_active`, `course_id`
  - ❌ `userId`, `createdAt`, `isActive`, `courseId`

- **Foreign Keys**: Referenced table name + `_id`
  - ✅ `user_id` (references `users.id`), `course_id` (references `courses.id`)
  - ❌ `fk_user`, `userId`, `fkUser`

- **Indexes**: `idx_{table}_{column(s)}`
  - ✅ `idx_users_email`, `idx_courses_created_at`, `idx_learning_sessions_user_id`
  - ❌ `users_email_index`, `UsersEmailIndex`

- **Primary Keys**: Always named `id` (integer, auto-increment)
  - ✅ `id INTEGER PRIMARY KEY`
  - ❌ `userId`, `user_id`, `pk_id`

- **Timestamps**: Always include `created_at` and `updated_at` (UTC, ISO 8601)
  - ✅ `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`, `updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`
  - ❌ `created`, `dateCreated`, `modified_at`

**Enforcement**: All SQLModel models must follow these conventions. Alembic migrations should enforce naming.

#### API Naming Conventions

**Standard: REST conventions with URL path versioning**

**Rules:**
- **Base Path**: `/api/v1/` (versioned URLs)
  - ✅ `/api/v1/courses`, `/api/v1/users`, `/api/v1/learning/sessions`
  - ❌ `/api/courses`, `/courses`, `/v1/courses`

- **Endpoints**: Plural nouns, lowercase, kebab-case for multi-word
  - ✅ `/api/v1/courses`, `/api/v1/course-modules`, `/api/v1/learning-sessions`
  - ❌ `/api/v1/course`, `/api/v1/Courses`, `/api/v1/course_modules`

- **Route Parameters**: Single lowercase word in curly braces
  - ✅ `/api/v1/courses/{id}`, `/api/v1/courses/{course_id}/modules/{module_id}`
  - ❌ `/api/v1/courses/:id`, `/api/v1/courses/{courseId}`, `/api/v1/courses/[id]`

- **Query Parameters**: snake_case (matches database columns)
  - ✅ `/api/v1/courses?user_id=123&is_active=true&created_after=2024-01-01`
  - ❌ `/api/v1/courses?userId=123&isActive=true`, `/api/v1/courses?createdAfter=2024-01-01`

- **HTTP Methods**: Standard REST verbs
  - ✅ `GET /api/v1/courses` (list), `GET /api/v1/courses/{id}` (detail), `POST /api/v1/courses` (create), `PUT /api/v1/courses/{id}` (update), `DELETE /api/v1/courses/{id}` (delete)
  - ❌ `GET /api/v1/get_courses`, `POST /api/v1/courses/update/{id}`

**Enforcement**: FastAPI route decorators must follow these patterns. API client generators should verify compliance.

#### Code Naming Conventions

**Standard: Language-native conventions with API boundary conversion**

**Backend (Python):**
- **Files**: snake_case with descriptive names
  - ✅ `user_service.py`, `course_repository.py`, `auth_middleware.py`
  - ❌ `UserService.py`, `userService.py`, `user-service.py`

- **Classes**: PascalCase
  - ✅ `UserService`, `CourseRepository`, `JWTAuthMiddleware`
  - ❌ `user_service`, `User_Service`, `userService`

- **Functions/Methods**: snake_case
  - ✅ `get_user_by_id()`, `create_course()`, `validate_jwt_token()`
  - ❌ `getUserById()`, `GetUserById()`, `get_user-by-id()`

- **Variables**: snake_case
  - ✅ `user_id`, `course_data`, `is_authenticated`
  - ❌ `userId`, `CourseData`, `isAuthenticated`

- **Constants**: UPPER_SNAKE_CASE
  - ✅ `MAX_RETRY_ATTEMPTS`, `DEFAULT_PAGE_SIZE`, `JWT_SECRET_KEY`
  - ❌ `MAX_RETRY_ATTEMPTS`, `maxRetryAttempts`, `MaxRetryAttempts`

**Frontend (TypeScript/React):**
- **Files**: kebab-case for pages/routes, PascalCase for components
  - ✅ `courses/[id]/page.tsx`, `CourseCard.tsx`, `user-profile.tsx`, `api-client.ts`
  - ❌ `Courses/[id]/page.tsx`, `courseCard.tsx`, `user_profile.tsx`

- **Components**: PascalCase
  - ✅ `CourseCard`, `UserProfile`, `LearningSession`, `AssessmentForm`
  - ❌ `course-card`, `courseCard`, `Course_Card`

- **Functions/Methods**: camelCase
  - ✅ `getUserById()`, `createCourse()`, `handleSubmit()`
  - ❌ `get_user_by_id()`, `GetUserById()`, `handle-submit()`

- **Variables**: camelCase
  - ✅ `userId`, `courseData`, `isAuthenticated`
  - ❌ `user_id`, `UserId`, `is_authenticated`

- **Constants**: UPPER_SNAKE_CASE (same as backend)
  - ✅ `MAX_RETRY_ATTEMPTS`, `API_BASE_URL`, `DEFAULT_PAGE_SIZE`
  - ❌ `MAX_RETRY_ATTEMPTS`, `maxRetryAttempts`

**API Boundary Conversion:**
- **Backend → Frontend**: Convert snake_case to camelCase in frontend API client
  - Backend JSON: `{"user_id": 123, "created_at": "2024-01-01T00:00:00Z"}`
  - Frontend TypeScript: `{userId: number, createdAt: string}`
  - Use transformation layer in `lib/api/client.ts` or React Query transformers

- **Frontend → Backend**: Convert camelCase to snake_case in API requests
  - Frontend TypeScript: `{userId: 123, courseId: 456}`
  - Backend JSON: `{"user_id": 123, "course_id": 456}`
  - Use transformation in Axios interceptors or request body transformation

**Enforcement**: Linters (ruff for Python, ESLint for TypeScript) must enforce these conventions.

### Structure Patterns

#### Project Organization

**Backend Structure:**
```
backend/
├── app/
│   ├── api/
│   │   └── v1/           # API version routes
│   │       ├── courses.py
│   │       ├── users.py
│   │       └── learning.py
│   ├── services/         # Business logic
│   │   ├── agents/       # Agent services
│   │   ├── orchestration/ # Prefect workflows
│   │   └── knowledge/    # Knowledge base services
│   ├── models/           # SQLModel database models
│   ├── utils/            # Utility functions
│   └── middleware/       # FastAPI middleware
├── tests/
│   ├── unit/             # Unit tests (co-located with modules)
│   ├── integration/      # Integration tests
│   └── e2e/              # End-to-end tests
└── migrations/           # Alembic migrations
```

**Frontend Structure:**
```
frontend/
├── app/                  # Next.js App Router
│   ├── (auth)/           # Route groups
│   ├── courses/
│   │   ├── page.tsx      # Server Component (SSR)
│   │   └── [id]/
│   │       ├── page.tsx
│   │       └── modules/[moduleId]/page.tsx
│   └── layout.tsx
├── components/
│   ├── ui/               # Reusable UI components
│   ├── course/           # Feature-specific components
│   └── layout/           # Layout components
├── lib/
│   ├── api/              # API client (Axios)
│   ├── utils/            # Utility functions
│   └── types/            # TypeScript types (shared with backend)
└── public/               # Static assets
```

**Test Organization:**
- **Backend**: Co-located with source files (`test_user_service.py` next to `user_service.py`)
- **Frontend**: Co-located with components (`CourseCard.test.tsx` next to `CourseCard.tsx`)
- **Integration Tests**: Separate `tests/integration/` folder
- **E2E Tests**: Separate `tests/e2e/` folder

**Enforcement**: Project structure templates must be documented and enforced via linting/CI.

#### File Structure Patterns

**Backend Files:**
- **Models**: `models/{entity}.py` (e.g., `models/user.py`, `models/course.py`)
- **Services**: `services/{domain}/{service}.py` (e.g., `services/courses/course_service.py`)
- **Routers**: `api/v1/{resource}.py` (e.g., `api/v1/courses.py`)
- **Config**: `config.py` (single config file)
- **Main**: `main.py` (FastAPI app initialization)

**Frontend Files:**
- **Pages**: `app/{route}/page.tsx` (Next.js App Router)
- **Components**: `components/{feature}/{Component}.tsx`
- **Types**: `lib/types/{domain}.ts` (e.g., `lib/types/course.ts`)
- **Utils**: `lib/utils/{utility}.ts` (e.g., `lib/utils/format.ts`)

**Static Assets:**
- **Images**: `public/images/{category}/{filename}` (e.g., `public/images/courses/python-intro.jpg`)
- **Fonts**: `public/fonts/{font-family}.woff2`
- **Icons**: `public/icons/{icon-name}.svg` or use icon library (React Icons)

**Enforcement**: File naming must match these patterns. IDE/editor templates can enforce structure.

### Format Patterns

#### API Response Formats

**Standard: Direct responses with HTTP status codes (no wrapper)**

**Success Responses:**
- **200 OK**: Direct resource object or array
```json
GET /api/v1/courses/{id}
{
  "id": 1,
  "title": "Introduction to Python",
  "description": "...",
  "user_id": 123,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

- **201 Created**: Created resource with Location header
```json
POST /api/v1/courses
HTTP/1.1 201 Created
Location: /api/v1/courses/1
{
  "id": 1,
  "title": "New Course",
  ...
}
```

- **204 No Content**: Empty body for DELETE operations
```http
DELETE /api/v1/courses/{id}
HTTP/1.1 204 No Content
```

**Error Responses:**
- **Format**: Standardized error object with HTTP status code
```json
{
  "error": {
    "code": "COURSE_NOT_FOUND",
    "message": "Course with ID 123 not found",
    "details": null,
    "request_id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

- **Status Codes**:
  - `400 Bad Request`: Validation errors, malformed requests
  - `401 Unauthorized`: Missing or invalid authentication
  - `403 Forbidden`: Authenticated but insufficient permissions
  - `404 Not Found`: Resource doesn't exist
  - `422 Unprocessable Entity`: Validation errors (FastAPI default)
  - `429 Too Many Requests`: Rate limit exceeded
  - `500 Internal Server Error`: Server errors
  - `503 Service Unavailable`: Service temporarily unavailable

**Pagination:**
- **Format**: Metadata in response headers, data in body
```http
GET /api/v1/courses?page=1&limit=20
HTTP/1.1 200 OK
X-Total-Count: 100
X-Page: 1
X-Limit: 20
X-Has-Next: true
[
  {...},
  {...}
]
```

**Enforcement**: FastAPI response models must enforce these formats. Error handlers must return consistent structure.

#### Data Exchange Formats

**JSON Field Naming:**
- **API JSON**: snake_case (matches database)
  - ✅ `{"user_id": 123, "created_at": "2024-01-01T00:00:00Z"}`
  - ❌ `{"userId": 123, "createdAt": "2024-01-01T00:00:00Z"}` (in API responses)

**Date/Time Formats:**
- **Standard**: ISO 8601 with UTC timezone
  - ✅ `"2024-01-01T00:00:00Z"` or `"2024-01-01T00:00:00+00:00"`
  - ❌ `"2024-01-01"`, `1640995200` (Unix timestamp), `"01/01/2024"`

**Boolean Representations:**
- **JSON**: `true`/`false` (lowercase)
  - ✅ `{"is_active": true}`, `{"is_completed": false}`
  - ❌ `{"is_active": "true"}`, `{"is_active": 1}`, `{"isActive": True}`

**Null Handling:**
- **JSON**: Use `null` (not `undefined`, not omitted)
  - ✅ `{"optional_field": null}` or `{"optional_field": "value"}`
  - ❌ `{"optional_field": undefined}` or omit field entirely

**Arrays vs Objects:**
- **Single Resource**: Always return object `{...}`
- **Collection**: Always return array `[{...}, {...}]`
- **Empty Collection**: Return empty array `[]` (not `null`)

**Enforcement**: Pydantic models (backend) and TypeScript types (frontend) must enforce these formats.

### Communication Patterns

#### Event System Patterns (RabbitMQ)

**Event Naming Convention:**
- **Format**: `{domain}.{action}.{past_tense}` (snake_case)
  - ✅ `course.created`, `course.updated`, `course.deleted`
  - ✅ `user.registered`, `user.activated`, `user.deactivated`
  - ✅ `learning_session.started`, `learning_session.completed`
  - ❌ `CourseCreated`, `course_created`, `CourseCreated`, `courses/create`

**Event Payload Structure:**
```json
{
  "event_type": "course.created",
  "event_id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2024-01-01T00:00:00Z",
  "version": "1.0",
  "payload": {
    "course_id": 1,
    "title": "Introduction to Python",
    "user_id": 123
  }
}
```

**Routing Keys (RabbitMQ):**
- **Format**: Same as event naming (`{domain}.{action}`)
  - ✅ `course.created`, `user.registered`, `learning_session.completed`
  - ❌ `course/created`, `CourseCreated`, `course_created`

**Enforcement**: Event publishers must follow naming convention. Event handlers must validate event structure.

#### WebSocket Event Patterns (Real-Time Tutoring)

**Event Naming Convention:**
- **Format**: `{action}:{entity}` (colon separator, lowercase)
  - ✅ `user:joined`, `user:left`, `message:sent`, `typing:started`, `typing:stopped`
  - ❌ `user_joined`, `UserJoined`, `user/joined`, `USER_JOINED`

**Message Format:**
```json
{
  "type": "message:sent",
  "payload": {
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "user_id": 123,
    "message": "Hello, can you help me understand this concept?",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

**Enforcement**: WebSocket handlers must validate message structure and event naming.

#### State Management Patterns (Frontend)

**Server State (React Query):**
- **Query Keys**: Array format with domain prefix
  - ✅ `['courses']`, `['courses', courseId]`, `['users', userId, 'profile']`
  - ❌ `'courses'`, `'courses:' + courseId`, `courses/${courseId}`

- **Mutations**: Use optimistic updates where possible
```typescript
useMutation({
  mutationFn: createCourse,
  onMutate: async (newCourse) => {
    await queryClient.cancelQueries(['courses']);
    const previousCourses = queryClient.getQueryData(['courses']);
    queryClient.setQueryData(['courses'], (old) => [...old, newCourse]);
    return { previousCourses };
  },
  onError: (err, newCourse, context) => {
    queryClient.setQueryData(['courses'], context.previousCourses);
  },
});
```

**Client State (Zustand/React Hooks):**
- **Store Naming**: camelCase with domain prefix
  - ✅ `useCourseStore`, `useAuthStore`, `useUISettingsStore`
  - ❌ `use_course_store`, `useCourse-store`, `CourseStore`

- **State Updates**: Always immutable
  - ✅ `setState({...state, newValue})` or `setState(produce(draft => { draft.value = newValue }))`
  - ❌ `state.value = newValue` (direct mutation)

**Enforcement**: ESLint rules must enforce immutable state updates. TypeScript must enforce type safety.

### Process Patterns

#### Error Handling Patterns

**Backend Error Handling:**
- **FastAPI Exception Handlers**: Global exception handlers for standardized error responses
```python
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": str(exc),
                "details": None,
                "request_id": request.state.request_id
            }
        }
    )
```

- **Custom Exceptions**: Domain-specific exceptions with error codes
```python
class CourseNotFoundError(Exception):
    def __init__(self, course_id: int):
        self.course_id = course_id
        self.code = "COURSE_NOT_FOUND"
        self.message = f"Course with ID {course_id} not found"
```

- **Logging**: Structured logging with context (request_id, user_id, error_code)
```python
logger.error(
    "Course not found",
    extra={
        "course_id": course_id,
        "request_id": request.state.request_id,
        "user_id": current_user.id,
        "error_code": "COURSE_NOT_FOUND"
    }
)
```

**Frontend Error Handling:**
- **Error Boundaries**: React Error Boundaries for component-level errors
```typescript
<ErrorBoundary fallback={<ErrorFallback />}>
  <CourseList />
</ErrorBoundary>
```

- **API Errors**: React Query error handling with user-friendly messages
```typescript
const { data, error } = useQuery(['courses'], fetchCourses);
if (error) {
  return <ErrorMessage message={error.error.message} code={error.error.code} />;
}
```

- **Toast Notifications**: User-facing errors via toast notifications (react-hot-toast or similar)
```typescript
toast.error(error.error.message, { id: error.error.request_id });
```

**Enforcement**: All errors must include error codes and request IDs for tracing. User-facing errors must be sanitized (no stack traces).

#### Loading State Patterns

**Backend:**
- **Async Operations**: Use background tasks for long-running operations
```python
@app.post("/api/v1/courses/{id}/generate")
async def generate_course_content(course_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(generate_course_content_task, course_id)
    return {"status": "processing", "task_id": task_id}
```

**Frontend:**
- **Loading State Naming**: `isLoading`, `isFetching`, `isMutating` (React Query standard)
  - ✅ `const { data, isLoading } = useQuery(...)`
  - ❌ `const { data, loading } = useQuery(...)`, `const { data, is_loading } = useQuery(...)`

- **Loading UI**: Skeleton loaders or spinners
```typescript
if (isLoading) return <CourseCardSkeleton />;
if (error) return <ErrorMessage error={error} />;
return <CourseList courses={data} />;
```

- **Optimistic Updates**: Show immediate feedback for mutations
```typescript
const mutation = useMutation({
  mutationFn: updateCourse,
  onMutate: async (newCourse) => {
    // Optimistic update
    await queryClient.cancelQueries(['courses', newCourse.id]);
    const previousCourse = queryClient.getQueryData(['courses', newCourse.id]);
    queryClient.setQueryData(['courses', newCourse.id], newCourse);
    return { previousCourse };
  },
});
```

**Enforcement**: Loading states must be consistent across components. No synchronous blocking operations.

#### Authentication Flow Patterns

**Backend:**
- **JWT Validation**: FastAPI dependency for protected routes
```python
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(user_id)
    if user is None:
        raise credentials_exception
    return user

@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return current_user
```

**Frontend:**
- **Token Storage**: localStorage for access token, httpOnly cookie for refresh token (if supported)
- **Token Refresh**: Automatic refresh on 401 responses
```typescript
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      const newToken = await refreshToken();
      localStorage.setItem('access_token', newToken);
      return apiClient.request(error.config);
    }
    return Promise.reject(error);
  }
);
```

- **Route Protection**: Next.js middleware for protected routes
```typescript
// middleware.ts
export function middleware(request: NextRequest) {
  const token = request.cookies.get('access_token');
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
}
```

**Enforcement**: All protected routes must verify JWT. Frontend must handle token expiration gracefully.

### Enforcement Guidelines

**All AI Agents MUST:**

1. **Follow Naming Conventions**: Use snake_case for Python, camelCase for TypeScript, snake_case for database and API JSON
2. **Maintain API Contract**: All API responses must follow standardized format (direct responses, no wrapper)
3. **Use Error Codes**: All errors must include error codes and request IDs
4. **Validate Input**: All API endpoints must validate input with Pydantic models (backend) and TypeScript types (frontend)
5. **Handle Loading States**: All async operations must show appropriate loading states
6. **Log Consistently**: All logging must use structured logging with request_id and context
7. **Test Patterns**: All code must include tests following project test organization
8. **Document Types**: All API endpoints must have TypeScript types and Pydantic models
9. **Version APIs**: All API changes must increment version (v1 → v2) for breaking changes
10. **Enforce Immutability**: All state updates must be immutable (frontend)

**Pattern Verification:**

- **Linting**: ruff (Python) and ESLint (TypeScript) must enforce naming and formatting
- **Type Checking**: mypy (Python) and TypeScript compiler must catch type errors
- **CI/CD**: GitHub Actions must run linters and type checkers before deployment
- **Code Review**: All PRs must verify pattern compliance
- **Documentation**: Pattern violations must be documented in PR comments

**Pattern Updates:**

- **Process**: Pattern changes must be approved via PR and documented in architecture.md
- **Breaking Changes**: Pattern changes that affect existing code must be versioned (API versioning)
- **Communication**: All agents must be notified of pattern updates

### Pattern Examples

**Good Examples:**

**Backend API Route:**
```python
# backend/app/api/v1/courses.py
@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(
    course_id: int,
    current_user: User = Depends(get_current_user)
) -> CourseResponse:
    """Get course by ID."""
    course = await course_service.get_course_by_id(course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "COURSE_NOT_FOUND",
                    "message": f"Course with ID {course_id} not found",
                    "details": None,
                    "request_id": request.state.request_id
                }
            }
        )
    return course
```

**Frontend API Client:**
```typescript
// frontend/lib/api/client.ts
export const getCourse = async (courseId: number): Promise<Course> => {
  const response = await apiClient.get(`/courses/${courseId}`);
  // Transform snake_case to camelCase
  return transformToCamelCase(response.data);
};

// frontend/lib/utils/transform.ts
export const transformToCamelCase = <T>(obj: any): T => {
  // Convert snake_case keys to camelCase
  // ...
};
```

**Frontend Component:**
```typescript
// frontend/components/course/CourseCard.tsx
'use client';

import { useQuery } from '@tanstack/react-query';
import { getCourse } from '@/lib/api/courses';

export function CourseCard({ courseId }: { courseId: number }) {
  const { data: course, isLoading, error } = useQuery(
    ['courses', courseId],
    () => getCourse(courseId)
  );

  if (isLoading) return <CourseCardSkeleton />;
  if (error) return <ErrorMessage error={error} />;
  
  return (
    <div>
      <h2>{course.title}</h2>
      <p>{course.description}</p>
    </div>
  );
}
```

**Anti-Patterns:**

❌ **Database Table Naming:**
```python
# WRONG: Mixed case, singular
class Users(Base):  # Should be 'users'
    UserId = Column(Integer)  # Should be 'id' and 'user_id'
    CreatedAt = Column(DateTime)  # Should be 'created_at'
```

❌ **API Response Wrapper:**
```python
# WRONG: Unnecessary wrapper
return {"data": {"id": 1, "title": "..."}, "error": None}
# CORRECT: Direct response
return {"id": 1, "title": "..."}
```

❌ **Frontend State Mutation:**
```typescript
// WRONG: Direct mutation
course.title = "New Title";  // Mutates state directly
// CORRECT: Immutable update
setCourse({...course, title: "New Title"});
```

❌ **Inconsistent Naming:**
```python
# WRONG: camelCase in Python
def getUserById(userId: int):  # Should be snake_case
    pass

# WRONG: snake_case in TypeScript
function get_user_by_id(user_id: number) {  // Should be camelCase
  // ...
}
```

## Project Structure & Boundaries

### Complete Project Directory Structure

```
agent-teacher/
├── README.md                                    # Project overview and setup instructions
├── .gitignore                                   # Git ignore rules for both Python and Node.js
├── .env.example                                 # Environment variable template (root level)
├── docker-compose.yml                           # Docker Compose for local development (backend, frontend, Redis, RabbitMQ)
├── docker-compose.prod.yml                      # Production Docker Compose configuration
├── .github/
│   └── workflows/
│       ├── ci-backend.yml                       # Backend CI pipeline (lint, test, type-check)
│       ├── ci-frontend.yml                      # Frontend CI pipeline (lint, test, type-check)
│       └── deploy.yml                           # Deployment pipeline (build, deploy to staging/production)
│
├── backend/                                     # FastAPI Backend (API-only)
│   ├── README.md                                # Backend-specific documentation
│   ├── pyproject.toml                           # Python dependencies and project config (uv)
│   ├── uv.lock                                  # Dependency lock file
│   ├── .env.example                             # Backend environment variables template
│   ├── .env                                     # Backend environment variables (gitignored)
│   ├── .pre-commit-config.yaml                  # Pre-commit hooks configuration
│   ├── Dockerfile                               # Backend Docker image
│   ├── docker-compose.backend.yml               # Backend-only Docker Compose
│   │
│   ├── app/                                     # Main application package
│   │   ├── __init__.py
│   │   ├── main.py                              # FastAPI application entry point
│   │   ├── config.py                            # Configuration management (pydantic-settings)
│   │   │
│   │   ├── api/                                 # API routes (versioned)
│   │   │   └── v1/                              # API version 1
│   │   │       ├── __init__.py
│   │   │       ├── auth.py                      # Authentication routes (FR1-FR4: User Account Management)
│   │   │       ├── courses.py                   # Course management routes (FR5-FR15, FR66: Course Management)
│   │   │       ├── learning.py                  # Learning & assessment routes (FR22-FR29, FR68-FR86: Learning & Assessment)
│   │   │       ├── tutoring.py                  # Interactive tutoring routes (FR30-FR34, FR76-FR77: Interactive Tutoring)
│   │   │       ├── assessments.py               # Assessment-specific routes (FR24-FR28: Assessments)
│   │   │       ├── progress.py                  # Progress tracking routes (FR35-FR40: Progress Tracking)
│   │   │       └── admin.py                     # Admin routes (FR54-FR63, FR70-FR73, FR87-FR88: Platform Administration)
│   │   │
│   │   ├── services/                            # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py                  # Authentication logic (JWT, password hashing)
│   │   │   ├── user_service.py                  # User management logic (FR1-FR4)
│   │   │   ├── course_service.py                # Course management logic (FR5-FR15, FR66)
│   │   │   ├── content_service.py               # Content generation coordination (FR16-FR21, FR64-FR65, FR67: Content Generation)
│   │   │   ├── learning_service.py              # Learning session management (FR22-FR23, FR29)
│   │   │   ├── assessment_service.py            # Assessment logic (FR24-FR28, FR26: Auto-grading)
│   │   │   ├── tutoring_service.py              # Tutoring session management (FR30-FR34, FR76-FR77)
│   │   │   ├── progress_service.py              # Progress tracking logic (FR35-FR40)
│   │   │   └── admin_service.py                 # Admin operations (FR54-FR63, FR70-FR73)
│   │   │
│   │   ├── services/agents/                     # Agent service layer
│   │   │   ├── __init__.py
│   │   │   ├── curriculum_agent.py              # Curriculum design agent (pydantic-ai) (FR5-FR6: Course/Unit generation)
│   │   │   ├── content_agent.py                 # Content generation agent (pydantic-ai) (FR16-FR17: Module/Assessment generation)
│   │   │   ├── tutor_agent.py                   # Tutoring agent (pydantic-ai) (FR30-FR33: Interactive tutoring)
│   │   │   ├── qa_agent.py                      # Quality assurance agent (pydantic-ai) (FR18, FR20: Content quality)
│   │   │   ├── optimizer_agent.py               # Optimization agent (pydantic-ai) (FR47-FR53: Self-improvement)
│   │   │   └── health_monitor_agent.py          # Health monitoring agent (pydantic-ai) (FR42, FR74: Agent health monitoring)
│   │   │
│   │   ├── services/orchestration/              # Agent orchestration layer
│   │   │   ├── __init__.py
│   │   │   ├── orchestrator.py                  # Main orchestrator (Prefect) (FR41-FR46: Multi-agent orchestration)
│   │   │   ├── task_router.py                   # Task routing logic (FR43: Route tasks to agents)
│   │   │   ├── agent_coordinator.py             # Agent coordination (FR41: Coordinate agents)
│   │   │   ├── fallback_handler.py              # Agent failure handling (FR44: Fallback mechanisms)
│   │   │   └── agent_logger.py                  # Agent activity logging (FR45: Agent logging)
│   │   │
│   │   ├── services/knowledge/                  # Knowledge base services
│   │   │   ├── __init__.py
│   │   │   ├── supabase_client.py               # Supabase client wrapper
│   │   │   ├── knowledge_base.py                # Knowledge base operations (FR19: Store content)
│   │   │   ├── content_retrieval.py             # Content retrieval for tutor (FR31: Query knowledge base)
│   │   │   ├── mem0_client.py                   # mem0 client for optimization learnings
│   │   │   └── content_versioning.py            # Content version management (FR64-FR65: Version history)
│   │   │
│   │   ├── models/                              # SQLModel database models
│   │   │   ├── __init__.py
│   │   │   ├── base.py                          # Base model with common fields (id, created_at, updated_at)
│   │   │   ├── user.py                          # User model (FR1-FR4: User Account Management)
│   │   │   ├── course.py                        # Course model (FR7-FR8: Course hierarchy)
│   │   │   ├── unit.py                          # Unit model (FR7: Course hierarchy)
│   │   │   ├── module.py                        # Module model (FR7: Course hierarchy)
│   │   │   ├── enrollment.py                    # Enrollment model (FR12-FR14: Course enrollment)
│   │   │   ├── learning_session.py              # Learning session model (FR22-FR23: Learning sessions)
│   │   │   ├── assessment.py                    # Assessment model (FR24-FR28: Assessments)
│   │   │   ├── assessment_response.py           # Assessment response model (FR24-FR28)
│   │   │   ├── tutoring_session.py              # Tutoring session model (FR30-FR34, FR76-FR77: Tutoring)
│   │   │   ├── progress.py                      # Progress model (FR35-FR40: Progress tracking)
│   │   │   ├── content_version.py               # Content version model (FR64-FR65: Version history)
│   │   │   └── agent_log.py                     # Agent log model (FR45, FR58: Agent logging)
│   │   │
│   │   ├── middleware/                          # FastAPI middleware
│   │   │   ├── __init__.py
│   │   │   ├── cors.py                          # CORS middleware configuration
│   │   │   ├── security.py                      # Security headers middleware
│   │   │   ├── rate_limiting.py                 # Rate limiting middleware (FR78: Rate limiting)
│   │   │   ├── authentication.py                # JWT authentication middleware
│   │   │   ├── logging.py                       # Request logging middleware
│   │   │   └── error_handler.py                 # Global error handler (FR68: Error messages)
│   │   │
│   │   ├── utils/                               # Utility functions
│   │   │   ├── __init__.py
│   │   │   ├── jwt.py                           # JWT token generation and validation
│   │   │   ├── password.py                      # Password hashing utilities
│   │   │   ├── validators.py                    # Input validation utilities
│   │   │   ├── formatters.py                    # Response formatting utilities
│   │   │   ├── logger.py                        # Structured logging utilities
│   │   │   └── exceptions.py                    # Custom exception classes
│   │   │
│   │   └── dependencies.py                      # FastAPI dependencies (get_current_user, etc.)
│   │
│   ├── agents/                                  # Standalone agent definitions (pydantic-ai)
│   │   ├── __init__.py
│   │   ├── curriculum_agent.py                  # Curriculum agent implementation
│   │   ├── content_agent.py                     # Content agent implementation
│   │   ├── tutor_agent.py                       # Tutor agent implementation
│   │   ├── qa_agent.py                          # QA agent implementation
│   │   ├── optimizer_agent.py                   # Optimizer agent implementation
│   │   └── health_monitor_agent.py              # Health monitor agent implementation
│   │
│   ├── orchestration/                           # Prefect workflows and tasks
│   │   ├── __init__.py
│   │   ├── workflows/
│   │   │   ├── __init__.py
│   │   │   ├── course_generation_workflow.py    # Course generation workflow (Prefect) (FR5-FR6, FR66)
│   │   │   ├── content_generation_workflow.py   # Content generation workflow (Prefect) (FR16-FR17)
│   │   │   ├── quality_assurance_workflow.py    # QA workflow (Prefect) (FR18, FR20)
│   │   │   ├── optimization_workflow.py         # Optimization workflow (Prefect) (FR47-FR53)
│   │   │   └── health_check_workflow.py         # Health check workflow (Prefect) (FR42, FR74)
│   │   │
│   │   └── tasks/
│   │       ├── __init__.py
│   │       ├── agent_tasks.py                   # Agent task definitions (Prefect tasks)
│   │       ├── knowledge_tasks.py               # Knowledge base tasks (Prefect tasks)
│   │       └── notification_tasks.py            # Notification tasks (Prefect tasks) (FR63: Notifications)
│   │
│   ├── migrations/                              # Alembic database migrations
│   │   ├── versions/                            # Migration version files
│   │   ├── env.py                               # Alembic environment configuration
│   │   ├── script.py.mako                       # Alembic migration template
│   │   └── alembic.ini                          # Alembic configuration
│   │
│   ├── tests/                                   # Backend tests
│   │   ├── __init__.py
│   │   ├── conftest.py                          # Pytest configuration and fixtures
│   │   │
│   │   ├── unit/                                # Unit tests (co-located with source files)
│   │   │   ├── test_auth_service.py             # Auth service unit tests
│   │   │   ├── test_user_service.py             # User service unit tests
│   │   │   ├── test_course_service.py           # Course service unit tests
│   │   │   ├── test_content_service.py          # Content service unit tests
│   │   │   ├── test_assessment_service.py       # Assessment service unit tests
│   │   │   ├── test_tutoring_service.py         # Tutoring service unit tests
│   │   │   ├── test_progress_service.py         # Progress service unit tests
│   │   │   ├── test_curriculum_agent.py         # Curriculum agent unit tests
│   │   │   ├── test_content_agent.py            # Content agent unit tests
│   │   │   ├── test_tutor_agent.py              # Tutor agent unit tests
│   │   │   └── test_orchestrator.py             # Orchestrator unit tests
│   │   │
│   │   ├── integration/                         # Integration tests
│   │   │   ├── test_api_auth.py                 # Authentication API integration tests
│   │   │   ├── test_api_courses.py              # Courses API integration tests
│   │   │   ├── test_api_learning.py             # Learning API integration tests
│   │   │   ├── test_api_tutoring.py             # Tutoring API integration tests
│   │   │   ├── test_api_assessments.py          # Assessments API integration tests
│   │   │   ├── test_api_progress.py             # Progress API integration tests
│   │   │   ├── test_agent_integration.py        # Agent integration tests
│   │   │   ├── test_knowledge_base_integration.py  # Knowledge base integration tests
│   │   │   └── test_websocket_integration.py    # WebSocket integration tests
│   │   │
│   │   └── e2e/                                 # End-to-end tests
│   │       ├── test_user_journey.py             # Complete user journey tests
│   │       ├── test_course_generation_journey.py  # Course generation flow tests
│   │       ├── test_tutoring_session_journey.py   # Tutoring session flow tests
│   │       └── test_admin_journey.py            # Admin journey tests
│   │
│   └── scripts/                                 # Utility scripts
│       ├── init_db.py                           # Database initialization script
│       ├── seed_data.py                         # Seed test data (FR87: Test data seeding)
│       ├── reset_test_users.py                  # Reset test user accounts (FR88: Reset test accounts)
│       └── migrate_db.py                        # Database migration script
│
├── frontend/                                    # Next.js Frontend
│   ├── README.md                                # Frontend-specific documentation
│   ├── package.json                             # Node.js dependencies
│   ├── package-lock.json                        # Dependency lock file
│   ├── tsconfig.json                            # TypeScript configuration
│   ├── next.config.js                           # Next.js configuration
│   ├── tailwind.config.js                       # Tailwind CSS configuration
│   ├── postcss.config.js                        # PostCSS configuration
│   ├── .env.local.example                       # Frontend environment variables template
│   ├── .env.local                               # Frontend environment variables (gitignored)
│   ├── .eslintrc.json                           # ESLint configuration
│   ├── .prettierrc                              # Prettier configuration
│   ├── Dockerfile                               # Frontend Docker image
│   │
│   ├── app/                                     # Next.js App Router
│   │   ├── layout.tsx                           # Root layout (Server Component)
│   │   ├── page.tsx                             # Homepage (Server Component) (FR9: Browse courses)
│   │   ├── globals.css                          # Global styles
│   │   │
│   │   ├── (auth)/                              # Auth route group
│   │   │   ├── login/
│   │   │   │   └── page.tsx                     # Login page (FR2: Login)
│   │   │   ├── register/
│   │   │   │   └── page.tsx                     # Registration page (FR1: Create account)
│   │   │   ├── forgot-password/
│   │   │   │   └── page.tsx                     # Forgot password page (FR4: Reset password)
│   │   │   └── reset-password/
│   │   │       └── page.tsx                     # Reset password page (FR4: Reset password)
│   │   │
│   │   ├── courses/                             # Courses pages
│   │   │   ├── page.tsx                         # Course listing (Server Component) (FR9-FR10: Browse & search courses)
│   │   │   ├── [id]/
│   │   │   │   ├── page.tsx                     # Course detail (Server Component) (FR11: View course description)
│   │   │   │   ├── modules/
│   │   │   │   │   └── [moduleId]/
│   │   │   │   │       └── page.tsx             # Module content page (Server Component) (FR23: Access module content)
│   │   │   │   └── enroll/
│   │   │   │       └── page.tsx                 # Enrollment page (Client Component) (FR12: Enroll in course)
│   │   │   │
│   │   ├── learning/                            # Learning pages
│   │   │   ├── page.tsx                         # Learning dashboard (Server Component) (FR38: View progress across courses)
│   │   │   ├── [courseId]/
│   │   │   │   ├── page.tsx                     # Course learning page (Server Component) (FR14: Access enrolled course)
│   │   │   │   ├── modules/
│   │   │   │   │   └── [moduleId]/
│   │   │   │   │       ├── page.tsx             # Module learning page (Server Component) (FR23: Sequential module access)
│   │   │   │   │       └── assessment/
│   │   │   │   │           └── page.tsx         # Module assessment page (Client Component) (FR24-FR28: Take assessments)
│   │   │   │   └── reset-progress/
│   │   │   │       └── page.tsx                 # Reset progress page (Client Component) (FR15: Reset progress)
│   │   │   │
│   │   ├── tutoring/                            # Tutoring pages
│   │   │   ├── [sessionId]/
│   │   │   │   └── page.tsx                     # Tutoring session page (Client Component) (FR30-FR34: Interactive tutoring)
│   │   │   │
│   │   ├── profile/                             # User profile pages
│   │   │   ├── page.tsx                         # Profile page (Server Component) (FR3: Manage account settings)
│   │   │   ├── settings/
│   │   │   │   └── page.tsx                     # Settings page (Client Component) (FR3: Account settings, FR84: Text size/contrast)
│   │   │   └── progress/
│   │   │       └── page.tsx                     # Progress overview page (Server Component) (FR38-FR40: Progress tracking)
│   │   │
│   │   ├── admin/                               # Admin pages (protected route)
│   │   │   ├── layout.tsx                       # Admin layout (Server Component)
│   │   │   ├── page.tsx                         # Admin dashboard (Server Component) (FR54: Platform health metrics)
│   │   │   ├── courses/
│   │   │   │   ├── page.tsx                     # Course management (Server Component) (FR55: Monitor course generation)
│   │   │   │   ├── generate/
│   │   │   │   │   └── page.tsx                 # Course generation trigger (Client Component) (FR66: Trigger generation)
│   │   │   │   └── [id]/
│   │   │   │       └── page.tsx                 # Course admin detail (Server Component)
│   │   │   ├── quality/
│   │   │   │   ├── page.tsx                     # Quality reports (Server Component) (FR56: QA reports)
│   │   │   │   └── benchmarks/
│   │   │   │       └── page.tsx                 # Quality benchmarks (Client Component) (FR57: Configure benchmarks)
│   │   │   ├── agents/
│   │   │   │   ├── page.tsx                     # Agent monitoring (Server Component) (FR58: Agent logs)
│   │   │   │   └── logs/
│   │   │   │       └── page.tsx                 # Agent logs detail (Server Component) (FR45, FR58: Agent logs)
│   │   │   ├── optimization/
│   │   │   │   └── page.tsx                     # Self-improvement metrics (Server Component) (FR53: Self-improvement metrics)
│   │   │   ├── test-data/
│   │   │   │   ├── page.tsx                     # Test data management (Server Component) (FR87: Test data seeding)
│   │   │   │   └── users/
│   │   │   │       └── page.tsx                 # Test user management (Server Component) (FR88: Reset test users)
│   │   │   └── api-costs/
│   │   │       └── page.tsx                     # API cost monitoring (Server Component) (FR79: API cost management)
│   │   │
│   │   ├── help/                                # Help pages
│   │   │   └── page.tsx                         # Help/documentation page (Server Component) (FR85: Help resources)
│   │   │
│   │   └── api/                                 # Next.js API routes (server-side API handlers if needed)
│   │       └── health/
│   │           └── route.ts                     # Health check API route
│   │
│   ├── components/                              # React components
│   │   ├── ui/                                  # Reusable UI components
│   │   │   ├── Button.tsx                       # Button component
│   │   │   ├── Input.tsx                        # Input component
│   │   │   ├── Card.tsx                         # Card component
│   │   │   ├── Modal.tsx                        # Modal component
│   │   │   ├── Toast.tsx                        # Toast notification component (FR68: Error messages)
│   │   │   ├── LoadingSpinner.tsx               # Loading spinner (FR81: Loading indicators)
│   │   │   ├── Skeleton.tsx                     # Skeleton loader (FR81: Loading states)
│   │   │   ├── EmptyState.tsx                   # Empty state component (FR80: Empty states)
│   │   │   └── ErrorBoundary.tsx                # Error boundary component (FR68: Error handling)
│   │   │
│   │   ├── layout/                              # Layout components
│   │   │   ├── Header.tsx                       # Site header
│   │   │   ├── Footer.tsx                       # Site footer
│   │   │   ├── Navigation.tsx                   # Navigation menu (FR82: Keyboard navigation)
│   │   │   ├── Sidebar.tsx                      # Sidebar navigation
│   │   │   └── SkipToContent.tsx                # Skip to content link (WCAG AA compliance)
│   │   │
│   │   ├── auth/                                # Authentication components
│   │   │   ├── LoginForm.tsx                    # Login form (Client Component) (FR2: Login)
│   │   │   ├── RegisterForm.tsx                 # Registration form (Client Component) (FR1: Create account)
│   │   │   ├── PasswordResetForm.tsx            # Password reset form (Client Component) (FR4: Reset password)
│   │   │   └── AuthGuard.tsx                    # Auth guard component (route protection)
│   │   │
│   │   ├── course/                              # Course-related components
│   │   │   ├── CourseCard.tsx                   # Course card component (Server/Client Component) (FR9: Browse courses)
│   │   │   ├── CourseList.tsx                   # Course list component (Server Component) (FR9-FR10: Course listing)
│   │   │   ├── CourseSearch.tsx                 # Course search component (Client Component) (FR10: Search courses)
│   │   │   ├── CourseDetail.tsx                 # Course detail component (Server Component) (FR11: Course description)
│   │   │   ├── CourseEnrollButton.tsx           # Enrollment button (Client Component) (FR12: Enroll)
│   │   │   ├── ModuleContent.tsx                # Module content display (Server Component) (FR23: Module content)
│   │   │   ├── ModuleNavigation.tsx             # Module navigation (Client Component) (FR23: Sequential access)
│   │   │   └── OnboardingGuide.tsx              # Onboarding component (Client Component) (FR22: Onboarding)
│   │   │
│   │   ├── learning/                            # Learning components
│   │   │   ├── LearningDashboard.tsx            # Learning dashboard (Server Component) (FR38: Progress overview)
│   │   │   ├── CourseProgress.tsx               # Course progress display (Server Component) (FR39-FR40: Progress tracking)
│   │   │   ├── ModuleProgress.tsx               # Module progress display (Server Component) (FR35: Module progress)
│   │   │   ├── CompletionBadge.tsx              # Completion acknowledgment (Client Component) (FR29: Completion acknowledgments)
│   │   │   └── MilestoneTracker.tsx             # Milestone tracker (Server Component) (FR86: Milestones and achievements)
│   │   │
│   │   ├── assessment/                          # Assessment components
│   │   │   ├── AssessmentForm.tsx               # Assessment form (Client Component) (FR24-FR25: Take assessments)
│   │   │   ├── AssessmentResult.tsx             # Assessment results (Client Component) (FR27: View results)
│   │   │   ├── AssessmentFeedback.tsx           # Assessment feedback (Client Component) (FR26: Feedback)
│   │   │   ├── RetakeButton.tsx                 # Retake assessment button (Client Component) (FR28: Retake assessments)
│   │   │   └── AutoGradeIndicator.tsx           # Auto-grade indicator (Client Component) (FR25: Auto-grading)
│   │   │
│   │   ├── tutoring/                            # Tutoring components
│   │   │   ├── TutoringChat.tsx                 # Tutoring chat interface (Client Component) (FR30-FR33: Interactive tutoring)
│   │   │   ├── ChatMessage.tsx                  # Chat message component (Client Component) (FR33: Conversation history)
│   │   │   ├── TutorResponse.tsx                # Tutor response component (Client Component) (FR32: Context-aware responses)
│   │   │   ├── SessionIndicator.tsx             # Session status indicator (Client Component) (FR77: Session timeout handling)
│   │   │   └── ReconnectionHandler.tsx          # WebSocket reconnection handler (Client Component) (FR77: WebSocket reconnection)
│   │   │
│   │   ├── profile/                             # Profile components
│   │   │   ├── ProfileSettings.tsx              # Profile settings form (Client Component) (FR3: Account settings)
│   │   │   ├── AccessibilitySettings.tsx        # Accessibility settings (Client Component) (FR84: Text size/contrast)
│   │   │   └── DataDeletionRequest.tsx          # Data deletion request (Client Component) (FR71: Data deletion)
│   │   │
│   │   └── admin/                               # Admin components
│   │       ├── AdminDashboard.tsx               # Admin dashboard (Server Component) (FR54: Platform health)
│   │       ├── CourseGenerationPanel.tsx        # Course generation panel (Client Component) (FR55, FR66: Course generation)
│   │       ├── QualityReportViewer.tsx          # Quality report viewer (Server Component) (FR56: QA reports)
│   │       ├── BenchmarkConfig.tsx              # Benchmark configuration (Client Component) (FR57: Configure benchmarks)
│   │       ├── AgentMonitor.tsx                 # Agent monitoring dashboard (Server Component) (FR58: Agent logs)
│   │       ├── OptimizationMetrics.tsx          # Optimization metrics view (Server Component) (FR53: Self-improvement metrics)
│   │       ├── APICostMonitor.tsx               # API cost monitor (Server Component) (FR79: API cost management)
│   │       └── TestDataManager.tsx              # Test data manager (Client Component) (FR87-FR88: Test data management)
│   │
│   ├── lib/                                     # Utility libraries
│   │   ├── api/                                 # Backend API client
│   │   │   ├── client.ts                        # Axios HTTP client configuration
│   │   │   ├── endpoints.ts                     # API endpoint definitions
│   │   │   ├── auth.ts                          # Authentication API calls
│   │   │   ├── courses.ts                       # Courses API calls
│   │   │   ├── learning.ts                      # Learning API calls
│   │   │   ├── assessments.ts                   # Assessments API calls
│   │   │   ├── tutoring.ts                      # Tutoring API calls
│   │   │   ├── progress.ts                      # Progress API calls
│   │   │   └── admin.ts                         # Admin API calls
│   │   │
│   │   ├── websocket/                           # WebSocket client
│   │   │   ├── client.ts                        # WebSocket client for tutoring (FR30-FR34: Interactive tutoring)
│   │   │   ├── handlers.ts                      # WebSocket message handlers
│   │   │   └── reconnect.ts                     # Reconnection logic (FR77: WebSocket reconnection)
│   │   │
│   │   ├── utils/                               # Utility functions
│   │   │   ├── transform.ts                     # API response transformation (snake_case → camelCase)
│   │   │   ├── format.ts                        # Formatting utilities (dates, numbers, etc.)
│   │   │   ├── validation.ts                    # Client-side validation utilities
│   │   │   └── error.ts                         # Error handling utilities (FR68: Error messages)
│   │   │
│   │   ├── hooks/                               # Custom React hooks
│   │   │   ├── useAuth.ts                       # Authentication hook
│   │   │   ├── useWebSocket.ts                  # WebSocket hook (FR30-FR34: Tutoring)
│   │   │   ├── useCourseProgress.ts             # Course progress hook (FR35-FR40: Progress tracking)
│   │   │   └── useAccessibility.ts              # Accessibility settings hook (FR84: Accessibility)
│   │   │
│   │   └── types/                               # TypeScript types
│   │       ├── api.ts                           # API response types (shared with backend)
│   │       ├── course.ts                        # Course-related types
│   │       ├── user.ts                          # User-related types
│   │       ├── assessment.ts                    # Assessment-related types
│   │       ├── tutoring.ts                      # Tutoring-related types
│   │       ├── progress.ts                      # Progress-related types
│   │       └── admin.ts                         # Admin-related types
│   │
│   ├── public/                                  # Static assets
│   │   ├── images/                              # Images
│   │   │   ├── courses/                         # Course images
│   │   │   ├── avatars/                         # User avatars
│   │   │   └── icons/                           # Icon images
│   │   ├── fonts/                               # Custom fonts
│   │   ├── favicon.ico                          # Favicon
│   │   └── robots.txt                           # Robots.txt (FR59: SEO optimization)
│   │
│   ├── styles/                                  # Global styles
│   │   └── globals.css                          # Global CSS styles (WCAG AA compliance)
│   │
│   └── tests/                                   # Frontend tests
│       ├── __mocks__/                           # Mock files
│       ├── components/                          # Component tests (co-located with components)
│       │   ├── ui/
│       │   │   └── Button.test.tsx
│       │   ├── course/
│       │   │   └── CourseCard.test.tsx
│       │   ├── learning/
│       │   │   └── LearningDashboard.test.tsx
│       │   ├── assessment/
│       │   │   └── AssessmentForm.test.tsx
│       │   └── tutoring/
│       │       └── TutoringChat.test.tsx
│       ├── lib/
│       │   ├── api/
│       │   │   └── client.test.ts
│       │   └── utils/
│       │       └── transform.test.ts
│       └── e2e/                                 # End-to-end tests (Playwright)
│           ├── auth.spec.ts                     # Authentication E2E tests
│           ├── course-enrollment.spec.ts        # Course enrollment E2E tests
│           ├── learning-journey.spec.ts         # Learning journey E2E tests
│           ├── tutoring-session.spec.ts         # Tutoring session E2E tests
│           └── admin.spec.ts                    # Admin E2E tests
│
├── infrastructure/                              # Infrastructure as Code
│   ├── docker/                                  # Docker configurations
│   │   ├── backend.Dockerfile                   # Backend production Dockerfile
│   │   ├── frontend.Dockerfile                  # Frontend production Dockerfile
│   │   └── nginx.conf                           # Nginx configuration (if needed)
│   │
│   ├── kubernetes/                              # Kubernetes manifests (for production scale)
│   │   ├── backend-deployment.yaml
│   │   ├── frontend-deployment.yaml
│   │   ├── services.yaml
│   │   └── ingress.yaml
│   │
│   └── monitoring/                              # Monitoring configurations
│       ├── prometheus/
│       │   └── prometheus.yml                   # Prometheus configuration
│       ├── grafana/
│       │   └── dashboards/                      # Grafana dashboard definitions
│       └── loki/
│           └── loki-config.yml                  # Loki configuration
│
└── scripts/                                     # Root-level utility scripts
    ├── setup.sh                                 # Initial project setup script
    ├── start-dev.sh                             # Start development environment
    ├── stop-dev.sh                              # Stop development environment
    └── deploy.sh                                # Deployment script
```

### Architectural Boundaries

#### API Boundaries

**External API Endpoints (FastAPI Backend):**
- **Base URL**: `/api/v1/`
- **Public Endpoints**: `/api/v1/courses` (GET - browse/search courses) - No authentication required
- **Authenticated Endpoints**: All other endpoints require JWT authentication
  - `/api/v1/auth/*` - Authentication routes (FR1-FR4)
  - `/api/v1/courses/*` - Course management (FR5-FR15, FR66)
  - `/api/v1/learning/*` - Learning sessions (FR22-FR29)
  - `/api/v1/tutoring/*` - Tutoring sessions (FR30-FR34, FR76-FR77)
  - `/api/v1/assessments/*` - Assessments (FR24-FR28)
  - `/api/v1/progress/*` - Progress tracking (FR35-FR40)
  - `/api/v1/admin/*` - Admin operations (FR54-FR63, FR70-FR73, FR87-FR88)

**Internal Service Boundaries:**
- **Backend API → Agent Services**: HTTP/REST for task assignment, JSON-RPC 2.0 for agent-to-agent communication
- **Backend API → Knowledge Base**: Supabase client (synchronous queries, async for updates)
- **Backend API → Message Queue**: RabbitMQ for asynchronous agent communication
- **Agent Services → Orchestration**: Prefect workflows coordinate agent tasks (FR41-FR46)

**Authentication & Authorization Boundaries:**
- **Public**: Course discovery/browsing only (FR9-FR10)
- **Authenticated Users**: All learning, tutoring, assessment, and progress features (FR1-FR40)
- **Administrators**: Admin dashboard and configuration (FR54-FR88)
- **System Agents**: Internal agent-to-agent communication (mTLS authentication)

**Data Access Layer Boundaries:**
- **ORM Layer**: SQLModel models (`app/models/`)
- **Service Layer**: Business logic (`app/services/`)
- **Repository Pattern**: Direct SQLModel queries in services (no separate repository layer)
- **Caching Layer**: Redis for frequently accessed data (course listings, user sessions)

#### Component Boundaries

**Frontend Component Communication:**
- **Server Components → Client Components**: Props passed from Server Components to Client Components
- **Client Components → Backend API**: HTTP client (`lib/api/client.ts`) for data fetching
- **Client Components → WebSocket**: WebSocket client (`lib/websocket/client.ts`) for real-time tutoring (FR30-FR34)
- **State Management**: React Query for server state, React hooks/Zustand for client state

**Service Communication Patterns:**
- **Synchronous**: FastAPI services call agent services directly via function calls
- **Asynchronous**: Prefect workflows orchestrate agent tasks via RabbitMQ message queues
- **Real-Time**: WebSocket connections for tutoring sessions (FastAPI WebSocket endpoints)

**Event-Driven Integration Points:**
- **RabbitMQ Events**: Agent coordination events (`course.created`, `content.generated`, etc.)
- **WebSocket Events**: Real-time tutoring events (`message:sent`, `typing:started`, etc.)
- **Event Handlers**: Prefect workflows handle RabbitMQ events for agent orchestration

#### Data Boundaries

**Database Schema Boundaries:**
- **Supabase (PostgreSQL)**: Primary database for all persistent data
  - User accounts, courses, units, modules (FR1-FR15)
  - Learning sessions, progress tracking (FR22-FR40)
  - Assessments and responses (FR24-FR28)
  - Tutoring sessions and history (FR30-FR34, FR76-FR77)
  - Agent logs and optimization metrics (FR45, FR47-FR53)
- **mem0**: Semantic memory layer for agent optimization learnings (FR47-FR53)

**Data Access Patterns:**
- **Read Operations**: SQLModel queries via services, cached in Redis when appropriate
- **Write Operations**: SQLModel models with Alembic migrations
- **Caching Strategy**: Redis for course listings, user sessions, frequently accessed content

**External Data Integration Points:**
- **Brave Search API**: Content research for course generation (FR16-FR17)
- **YouTube API**: Video content integration for modules (FR16)
- **LLM APIs (OpenAI, Anthropic, etc.)**: Agent operations (FR46)

### Requirements to Structure Mapping

#### Feature/Epic Mapping

**User Account Management (FR1-FR4):**
- **Backend Routes**: `backend/app/api/v1/auth.py`
- **Backend Services**: `backend/app/services/auth_service.py`, `backend/app/services/user_service.py`
- **Backend Models**: `backend/app/models/user.py`
- **Frontend Pages**: `frontend/app/(auth)/login/page.tsx`, `frontend/app/(auth)/register/page.tsx`, `frontend/app/(auth)/forgot-password/page.tsx`
- **Frontend Components**: `frontend/components/auth/LoginForm.tsx`, `frontend/components/auth/RegisterForm.tsx`
- **Tests**: `backend/tests/unit/test_auth_service.py`, `backend/tests/integration/test_api_auth.py`

**Course Management (FR5-FR15, FR66):**
- **Backend Routes**: `backend/app/api/v1/courses.py`
- **Backend Services**: `backend/app/services/course_service.py`, `backend/app/services/content_service.py`
- **Backend Models**: `backend/app/models/course.py`, `backend/app/models/unit.py`, `backend/app/models/module.py`, `backend/app/models/enrollment.py`
- **Backend Agents**: `backend/app/services/agents/curriculum_agent.py` (FR5-FR6), `backend/app/services/agents/content_agent.py` (FR16-FR17)
- **Backend Orchestration**: `backend/orchestration/workflows/course_generation_workflow.py` (Prefect)
- **Frontend Pages**: `frontend/app/courses/page.tsx` (FR9-FR10), `frontend/app/courses/[id]/page.tsx` (FR11), `frontend/app/courses/[id]/enroll/page.tsx` (FR12)
- **Frontend Components**: `frontend/components/course/CourseCard.tsx`, `frontend/components/course/CourseList.tsx`, `frontend/components/course/CourseSearch.tsx`
- **Tests**: `backend/tests/unit/test_course_service.py`, `backend/tests/integration/test_api_courses.py`

**Content Generation & Quality (FR16-FR21, FR64-FR65, FR67):**
- **Backend Services**: `backend/app/services/content_service.py`, `backend/app/services/agents/content_agent.py` (FR16-FR17), `backend/app/services/agents/qa_agent.py` (FR18, FR20)
- **Backend Models**: `backend/app/models/content_version.py` (FR64-FR65)
- **Backend Knowledge Base**: `backend/app/services/knowledge/knowledge_base.py` (FR19)
- **Backend Orchestration**: `backend/orchestration/workflows/content_generation_workflow.py`, `backend/orchestration/workflows/quality_assurance_workflow.py`
- **Tests**: `backend/tests/unit/test_content_service.py`, `backend/tests/unit/test_content_agent.py`

**Learning & Assessment (FR22-FR29, FR68-FR86):**
- **Backend Routes**: `backend/app/api/v1/learning.py`, `backend/app/api/v1/assessments.py`
- **Backend Services**: `backend/app/services/learning_service.py`, `backend/app/services/assessment_service.py`
- **Backend Models**: `backend/app/models/learning_session.py`, `backend/app/models/assessment.py`, `backend/app/models/assessment_response.py`
- **Frontend Pages**: `frontend/app/learning/page.tsx` (FR38), `frontend/app/learning/[courseId]/page.tsx` (FR14), `frontend/app/learning/[courseId]/modules/[moduleId]/page.tsx` (FR23), `frontend/app/learning/[courseId]/modules/[moduleId]/assessment/page.tsx` (FR24-FR28)
- **Frontend Components**: `frontend/components/learning/LearningDashboard.tsx`, `frontend/components/assessment/AssessmentForm.tsx`, `frontend/components/course/OnboardingGuide.tsx` (FR22)
- **Frontend Error Handling**: `frontend/components/ui/ErrorBoundary.tsx`, `frontend/components/ui/Toast.tsx` (FR68)
- **Tests**: `backend/tests/unit/test_assessment_service.py`, `backend/tests/integration/test_api_learning.py`

**Interactive Tutoring (FR30-FR34, FR76-FR77):**
- **Backend Routes**: `backend/app/api/v1/tutoring.py` (WebSocket endpoints)
- **Backend Services**: `backend/app/services/tutoring_service.py`, `backend/app/services/agents/tutor_agent.py` (FR30-FR33)
- **Backend Models**: `backend/app/models/tutoring_session.py`
- **Backend Knowledge Base**: `backend/app/services/knowledge/content_retrieval.py` (FR31)
- **Frontend Pages**: `frontend/app/tutoring/[sessionId]/page.tsx`
- **Frontend Components**: `frontend/components/tutoring/TutoringChat.tsx`, `frontend/components/tutoring/ReconnectionHandler.tsx` (FR77)
- **Frontend WebSocket Client**: `frontend/lib/websocket/client.ts` (FR77: Reconnection handling)
- **Tests**: `backend/tests/unit/test_tutoring_service.py`, `backend/tests/integration/test_api_tutoring.py`, `backend/tests/integration/test_websocket_integration.py`

**Progress Tracking (FR35-FR40):**
- **Backend Routes**: `backend/app/api/v1/progress.py`
- **Backend Services**: `backend/app/services/progress_service.py`
- **Backend Models**: `backend/app/models/progress.py`
- **Frontend Pages**: `frontend/app/profile/progress/page.tsx` (FR38)
- **Frontend Components**: `frontend/components/learning/CourseProgress.tsx`, `frontend/components/learning/ModuleProgress.tsx`, `frontend/components/learning/MilestoneTracker.tsx` (FR86)
- **Tests**: `backend/tests/unit/test_progress_service.py`, `backend/tests/integration/test_api_progress.py`

**Multi-Agent Orchestration (FR41-FR46):**
- **Backend Services**: `backend/app/services/orchestration/orchestrator.py` (Prefect), `backend/app/services/orchestration/task_router.py` (FR43), `backend/app/services/orchestration/agent_coordinator.py` (FR41)
- **Backend Agents**: All agents in `backend/app/services/agents/` and `backend/agents/`
- **Backend Orchestration**: All Prefect workflows in `backend/orchestration/workflows/`
- **Backend Message Queue**: RabbitMQ integration in orchestration layer
- **Backend Logging**: `backend/app/services/orchestration/agent_logger.py` (FR45)
- **Tests**: `backend/tests/unit/test_orchestrator.py`, `backend/tests/integration/test_agent_integration.py`

**Self-Improvement & Optimization (FR47-FR53):**
- **Backend Services**: `backend/app/services/agents/optimizer_agent.py`
- **Backend Models**: `backend/app/models/agent_log.py` (FR51)
- **Backend Knowledge Base**: `backend/app/services/knowledge/mem0_client.py`
- **Backend Orchestration**: `backend/orchestration/workflows/optimization_workflow.py`
- **Frontend Pages**: `frontend/app/admin/optimization/page.tsx` (FR53)
- **Frontend Components**: `frontend/components/admin/OptimizationMetrics.tsx`
- **Tests**: `backend/tests/unit/test_optimizer_agent.py`

**Platform Administration (FR54-FR63, FR70-FR73, FR87-FR88):**
- **Backend Routes**: `backend/app/api/v1/admin.py`
- **Backend Services**: `backend/app/services/admin_service.py`
- **Frontend Pages**: All pages in `frontend/app/admin/`
- **Frontend Components**: All components in `frontend/components/admin/`
- **Backend Scripts**: `backend/scripts/seed_data.py` (FR87), `backend/scripts/reset_test_users.py` (FR88)
- **Tests**: `backend/tests/e2e/test_admin_journey.py`

#### Cross-Cutting Concerns

**Authentication System:**
- **Backend**: `backend/app/middleware/authentication.py`, `backend/app/dependencies.py`, `backend/app/utils/jwt.py`, `backend/app/utils/password.py`
- **Frontend**: `frontend/components/auth/AuthGuard.tsx`, `frontend/lib/hooks/useAuth.ts`, `frontend/lib/api/auth.ts`
- **Tests**: `backend/tests/unit/test_auth_service.py`, `backend/tests/integration/test_api_auth.py`

**Error Handling:**
- **Backend**: `backend/app/middleware/error_handler.py`, `backend/app/utils/exceptions.py`
- **Frontend**: `frontend/components/ui/ErrorBoundary.tsx`, `frontend/components/ui/Toast.tsx`, `frontend/lib/utils/error.ts`
- **Tests**: Error handling tests in integration test suites

**Logging & Monitoring:**
- **Backend**: `backend/app/utils/logger.py`, `backend/app/middleware/logging.py`, `backend/app/services/orchestration/agent_logger.py`
- **Frontend**: Console logging for client-side errors, structured error reporting
- **Infrastructure**: `infrastructure/monitoring/` (Prometheus, Loki, Grafana)

**Rate Limiting:**
- **Backend**: `backend/app/middleware/rate_limiting.py` (application-level), Kong API Gateway (external API rate limiting) (FR78)
- **Tests**: Rate limiting tests in integration test suites

**Caching:**
- **Backend**: Redis integration in services (course listings, user sessions)
- **Frontend**: React Query caching for API responses
- **Infrastructure**: Redis container in `docker-compose.yml`

**Accessibility (WCAG 2.1 AA Compliance):**
- **Frontend**: All components must meet WCAG AA standards (FR61, FR82-FR84)
- **Frontend Components**: `frontend/components/layout/SkipToContent.tsx`, `frontend/components/profile/AccessibilitySettings.tsx`
- **Frontend Hooks**: `frontend/lib/hooks/useAccessibility.ts`
- **Tests**: Accessibility tests in component test suites

### Integration Points

#### Internal Communication

**Backend → Frontend:**
- **API Communication**: HTTP/REST via `/api/v1/*` endpoints
- **Real-Time Communication**: WebSocket connections for tutoring sessions (`/api/v1/tutoring/ws/{session_id}`)
- **Data Format**: JSON with snake_case keys (converted to camelCase in frontend client)

**Backend → Agent Services:**
- **Direct Calls**: FastAPI services call agent services directly (synchronous)
- **Orchestrated Calls**: Prefect workflows coordinate agent tasks via RabbitMQ (asynchronous)
- **Protocol**: JSON-RPC 2.0 for agent-to-agent communication

**Agent Services → Knowledge Base:**
- **Supabase**: Direct queries via Supabase client (`backend/app/services/knowledge/supabase_client.py`)
- **mem0**: Semantic memory queries for optimization learnings (`backend/app/services/knowledge/mem0_client.py`)

**Agent Services → Message Queue:**
- **RabbitMQ**: Agent coordination events (`course.created`, `content.generated`, etc.)
- **Event Handlers**: Prefect workflows handle RabbitMQ events

#### External Integrations

**External AI/LLM APIs:**
- **Integration Point**: Agent services use pydantic-ai with LLM providers (OpenAI, Anthropic, etc.) (FR46)
- **Rate Limiting**: Kong API Gateway for external API rate limiting (FR78)
- **Cost Monitoring**: Admin dashboard for API cost tracking (FR79)
- **Failure Handling**: Queue requests and retry with exponential backoff (FR44)

**Supabase (Database):**
- **Integration Point**: `backend/app/services/knowledge/supabase_client.py`
- **Sync Strategy**: Real-time sync for knowledge base (<1 second latency)
- **Fallback**: Cached content served with staleness indicators if Supabase unavailable

**Brave Search API:**
- **Integration Point**: Agent services use Brave Search API for content research (FR16-FR17)
- **Rate Limiting**: Kong API Gateway manages rate limits
- **Fallback**: Queue requests if API unavailable

**YouTube API:**
- **Integration Point**: Agent services use YouTube API for video content (FR16)
- **Rate Limiting**: Kong API Gateway manages rate limits
- **Fallback**: Optional video content if API unavailable

#### Data Flow

**Course Generation Flow:**
1. **Trigger**: Admin triggers course generation (FR66) → `frontend/app/admin/courses/generate/page.tsx`
2. **API Request**: Frontend → `POST /api/v1/admin/courses/generate` → `backend/app/api/v1/admin.py`
3. **Orchestration**: Prefect workflow (`backend/orchestration/workflows/course_generation_workflow.py`) coordinates agents
4. **Agent Tasks**: Curriculum agent (FR5-FR6) → Content agent (FR16-FR17) → QA agent (FR18, FR20)
5. **Knowledge Base**: Generated content stored in Supabase (`backend/app/services/knowledge/knowledge_base.py`) (FR19)
6. **Response**: Course available for enrollment (FR12)

**Tutoring Session Flow:**
1. **Initiate**: Learner initiates tutoring session (FR30) → `frontend/app/learning/[courseId]/modules/[moduleId]/page.tsx`
2. **WebSocket Connection**: Frontend → `WS /api/v1/tutoring/ws/{session_id}` → `backend/app/api/v1/tutoring.py`
3. **Message**: Learner sends question → WebSocket message → `backend/app/services/tutoring_service.py`
4. **Tutor Agent**: Tutor agent queries knowledge base (FR31) → `backend/app/services/agents/tutor_agent.py`
5. **Response**: Context-aware response (FR32) → WebSocket message → Frontend
6. **History**: Conversation history persisted (FR33) → `backend/app/models/tutoring_session.py`

**Learning Progress Flow:**
1. **Module Completion**: Learner completes module (FR23) → `frontend/app/learning/[courseId]/modules/[moduleId]/page.tsx`
2. **Assessment**: Learner takes assessment (FR24) → `frontend/app/learning/[courseId]/modules/[moduleId]/assessment/page.tsx`
3. **Auto-Grading**: System grades assessment (FR25) → `backend/app/services/assessment_service.py`
4. **Progress Update**: Progress tracked (FR35-FR40) → `backend/app/services/progress_service.py`
5. **Display**: Progress displayed in dashboard (FR38) → `frontend/app/profile/progress/page.tsx`

### File Organization Patterns

#### Configuration Files

**Root Level:**
- `.env.example` - Environment variable templates (both backend and frontend)
- `docker-compose.yml` - Local development Docker Compose
- `.gitignore` - Git ignore rules (Python, Node.js, environment files)

**Backend Configuration:**
- `backend/pyproject.toml` - Python dependencies and project config (uv)
- `backend/.env` - Backend environment variables (gitignored)
- `backend/.pre-commit-config.yaml` - Pre-commit hooks
- `backend/migrations/alembic.ini` - Alembic configuration

**Frontend Configuration:**
- `frontend/package.json` - Node.js dependencies
- `frontend/tsconfig.json` - TypeScript configuration
- `frontend/next.config.js` - Next.js configuration
- `frontend/tailwind.config.js` - Tailwind CSS configuration
- `frontend/.env.local` - Frontend environment variables (gitignored)

#### Source Organization

**Backend Source Structure:**
- **API Routes**: Versioned routes in `backend/app/api/v1/`
- **Services**: Business logic in `backend/app/services/` (feature-based organization)
- **Models**: Database models in `backend/app/models/` (one model per file)
- **Middleware**: Shared middleware in `backend/app/middleware/`
- **Agents**: Agent implementations in `backend/app/services/agents/` and `backend/agents/`
- **Orchestration**: Prefect workflows in `backend/orchestration/workflows/`

**Frontend Source Structure:**
- **Pages**: Next.js App Router pages in `frontend/app/` (file-based routing)
- **Components**: React components in `frontend/components/` (feature-based organization)
- **Libraries**: Utility libraries in `frontend/lib/` (api, utils, hooks, types)
- **Styles**: Global styles in `frontend/styles/`
- **Public Assets**: Static assets in `frontend/public/`

#### Test Organization

**Backend Tests:**
- **Unit Tests**: Co-located with source files (`test_*.py` next to source files) OR in `backend/tests/unit/`
- **Integration Tests**: `backend/tests/integration/` (API tests, agent integration tests)
- **E2E Tests**: `backend/tests/e2e/` (complete user journey tests)
- **Fixtures**: `backend/tests/conftest.py` (pytest fixtures)

**Frontend Tests:**
- **Component Tests**: Co-located with components (`*.test.tsx` next to components)
- **Unit Tests**: `frontend/tests/` or co-located with source files
- **E2E Tests**: `frontend/tests/e2e/` (Playwright tests)
- **Mocks**: `frontend/tests/__mocks__/` (mock files)

#### Asset Organization

**Static Assets:**
- **Images**: `frontend/public/images/{category}/{filename}` (organized by category)
- **Fonts**: `frontend/public/fonts/{font-family}.woff2`
- **Icons**: `frontend/public/icons/{icon-name}.svg` or use icon library
- **Favicon**: `frontend/public/favicon.ico`

**Build Outputs:**
- **Backend**: No build output (Python runs directly or Docker image)
- **Frontend**: `.next/` directory (Next.js build output, gitignored)
- **Docker Images**: Built images tagged with version numbers

### Development Workflow Integration

**Development Server Structure:**
- **Local Development**: `docker-compose.yml` runs all services (backend, frontend, Redis, RabbitMQ)
- **Backend Dev Server**: `uvicorn app.main:app --reload` (hot reload enabled)
- **Frontend Dev Server**: `npm run dev` (Next.js dev server with hot reload)

**Build Process Structure:**
- **Backend Build**: Docker image build (`docker build -t backend:latest backend/`)
- **Frontend Build**: Next.js build (`npm run build` in `frontend/`)
- **CI/CD**: GitHub Actions runs lint → test → build → deploy pipeline

**Deployment Structure:**
- **MVP Deployment**: Railway or Render (simple container deployment)
- **Production Deployment**: AWS ECS or GCP Cloud Run (container orchestration)
- **Docker Images**: Separate images for backend and frontend
- **Environment Variables**: Set via deployment platform (no `.env` files in production)

This complete project structure provides a concrete implementation guide for AI agents, mapping all functional requirements to specific files and directories while maintaining clear architectural boundaries and integration points.

## Architecture Validation Results

### Coherence Validation ✅

**Decision Compatibility:**
All architectural decisions work together seamlessly:

- ✅ **Technology Stack Compatibility**: FastAPI (Python) backend with Next.js (TypeScript/React) frontend are fully compatible. FastAPI provides clean REST API endpoints that Next.js consumes via HTTP client. WebSocket support is native in FastAPI and works with Next.js WebSocket clients.

- ✅ **Agent Framework Integration**: pydantic-ai integrates cleanly with FastAPI backend, allowing agents to be called directly from FastAPI services. Prefect orchestration works seamlessly with pydantic-ai agents, enabling complex multi-agent workflows.

- ✅ **Database & ORM Compatibility**: SQLModel (extends Pydantic) works perfectly with Supabase PostgreSQL, providing type-safe database models that align with FastAPI's Pydantic validation. Alembic migrations work seamlessly with SQLModel.

- ✅ **Message Queue & Caching**: RabbitMQ for agent communication and Redis for caching are well-established patterns that integrate cleanly with FastAPI (via pika and redis libraries) and Prefect workflows.

- ✅ **API Gateway**: Kong API Gateway sits cleanly in front of FastAPI backend, providing rate limiting and cost management for external API calls without requiring backend code changes.

- ✅ **Monitoring Stack**: Prometheus, Loki, Jaeger, and Grafana form a complete observability stack that integrates with FastAPI, Next.js, and Prefect workflows via standard instrumentation.

- ✅ **Deployment Compatibility**: Docker containers for backend and frontend enable independent scaling and deployment, supporting MVP (Railway/Render) and production (AWS ECS/GCP Cloud Run) deployment strategies.

**Pattern Consistency:**
All implementation patterns align with architectural decisions:

- ✅ **Naming Conventions**: Consistent snake_case for Python/PostgreSQL and camelCase for TypeScript, with clear conversion at API boundary. All patterns documented with examples and anti-patterns.

- ✅ **Structure Patterns**: Project structure supports FastAPI + Next.js separation, with clear boundaries between backend (API-only) and frontend (SSR/SSG). Feature-based organization aligns with functional requirement categories.

- ✅ **Communication Patterns**: JSON-RPC 2.0 for agent-to-agent, REST for API, WebSocket for real-time tutoring - all patterns are consistent and well-defined. Event naming conventions (snake_case with domain.action format) are consistent.

- ✅ **Process Patterns**: Error handling, loading states, authentication flows are all standardized and consistent across backend and frontend.

**Structure Alignment:**
Project structure fully supports all architectural decisions:

- ✅ **Backend Structure**: FastAPI API-only structure with versioned routes (`/api/v1/`), clear service layer separation, agent services organized by domain, and Prefect workflows in separate orchestration directory. Structure enables all architectural decisions.

- ✅ **Frontend Structure**: Next.js App Router structure with Server/Client Components, clear feature-based component organization, API client abstraction, and WebSocket client separation. Structure supports SSR/SSG and real-time features.

- ✅ **Boundary Definitions**: Clear boundaries between backend/frontend, services/agents, orchestration/workflows, and models/services. Integration points are well-defined and structured.

- ✅ **Integration Points**: All integration points (API endpoints, WebSocket connections, RabbitMQ events, database queries) are clearly specified in structure with specific file locations.

### Requirements Coverage Validation ✅

**Functional Requirements Coverage:**
All 88 functional requirements are architecturally supported and mapped to specific implementation locations:

**✅ User Account Management (FR1-FR4):**
- FR1-FR4: All mapped to `backend/app/api/v1/auth.py`, `backend/app/services/auth_service.py`, and `frontend/app/(auth)/` pages. Architecture supports JWT authentication with refresh tokens, password reset flows, and account management.

**✅ Course Management (FR5-FR15, FR66):**
- FR5-FR6: Course/unit generation mapped to `backend/app/services/agents/curriculum_agent.py` and `backend/orchestration/workflows/course_generation_workflow.py` (Prefect).
- FR7: Course hierarchy mapped to `backend/app/models/course.py`, `unit.py`, `module.py`.
- FR8-FR11: Course catalog, browsing, searching mapped to `backend/app/api/v1/courses.py` and `frontend/app/courses/` pages.
- FR12-FR15: Enrollment, access, progress reset mapped to `backend/app/services/course_service.py` and `frontend/app/learning/` pages.
- FR66: Admin course generation trigger mapped to `frontend/app/admin/courses/generate/page.tsx` and admin API routes.

**✅ Content Generation & Quality (FR16-FR21, FR64-FR65, FR67):**
- FR16-FR17: Content generation mapped to `backend/app/services/agents/content_agent.py` and Prefect workflows.
- FR18, FR20: Quality assurance mapped to `backend/app/services/agents/qa_agent.py` and QA workflow.
- FR19: Knowledge base storage mapped to `backend/app/services/knowledge/knowledge_base.py` (Supabase).
- FR21: Quality tracking mapped to agent logging and optimization workflows.
- FR64-FR65: Content versioning mapped to `backend/app/models/content_version.py` and versioning service.
- FR67: Storage lifecycle mapped to knowledge base service with hot/archive/cleanup patterns.

**✅ Learning & Assessment (FR22-FR29, FR68-FR86):**
- FR22: Onboarding mapped to `frontend/components/course/OnboardingGuide.tsx`.
- FR23: Sequential module access mapped to `frontend/app/learning/[courseId]/modules/[moduleId]/page.tsx`.
- FR24-FR28: Assessments mapped to `backend/app/api/v1/assessments.py`, `assessment_service.py`, and frontend assessment pages.
- FR29: Completion acknowledgments mapped to `frontend/components/learning/CompletionBadge.tsx`.
- FR68-FR69: Error handling mapped to `backend/app/middleware/error_handler.py` and `frontend/components/ui/ErrorBoundary.tsx`.
- FR80-FR86: UX features (empty states, loading, accessibility, help, milestones) mapped to frontend components and services.

**✅ Interactive Tutoring (FR30-FR34, FR76-FR77):**
- FR30-FR33: Tutoring mapped to `backend/app/api/v1/tutoring.py` (WebSocket), `backend/app/services/agents/tutor_agent.py`, and `frontend/components/tutoring/` components.
- FR34: Tutoring access during learning mapped to module learning pages with tutoring integration.
- FR76-FR77: Session persistence and WebSocket reconnection mapped to `backend/app/models/tutoring_session.py` and `frontend/components/tutoring/ReconnectionHandler.tsx`.

**✅ Progress Tracking (FR35-FR40):**
- FR35-FR40: Progress tracking mapped to `backend/app/api/v1/progress.py`, `progress_service.py`, `progress.py` model, and `frontend/components/learning/` progress components.

**✅ Multi-Agent Orchestration (FR41-FR46, FR74-FR75, FR78-FR79):**
- FR41-FR46: Agent orchestration mapped to `backend/app/services/orchestration/` services, Prefect workflows, and RabbitMQ integration.
- FR74: Real-time monitoring mapped to Prometheus + Grafana and `backend/app/services/agents/health_monitor_agent.py`.
- FR75: Quality gates mapped to Prefect workflow triggers and QA agent.
- FR78: Rate limiting mapped to `backend/app/middleware/rate_limiting.py` and Kong API Gateway.
- FR79: API cost monitoring mapped to `frontend/app/admin/api-costs/page.tsx` and admin service.

**✅ Self-Improvement & Optimization (FR47-FR53):**
- FR47-FR53: Optimization mapped to `backend/app/services/agents/optimizer_agent.py`, `optimization_workflow.py`, `mem0_client.py` for learnings, and `frontend/app/admin/optimization/page.tsx`.

**✅ Platform Administration (FR54-FR63, FR70-FR73, FR87-FR88):**
- FR54-FR58: Admin dashboard mapped to `frontend/app/admin/` pages and `backend/app/api/v1/admin.py`.
- FR59: SEO optimization mapped to Next.js SSR/SSG capabilities and meta tags.
- FR60: Responsive design mapped to Next.js and Tailwind CSS configuration.
- FR61: WCAG AA compliance mapped to frontend accessibility components and testing requirements.
- FR62: Data persistence mapped to Supabase (PostgreSQL) with backup/recovery strategies.
- FR63: Notifications mapped to `backend/orchestration/tasks/notification_tasks.py` and Prefect workflows.
- FR70-FR73: Content rollback, data deletion, GDPR compliance, and audit logging mapped to admin services and models.
- FR87-FR88: Test data management mapped to `backend/scripts/seed_data.py` and admin test data pages.

**Non-Functional Requirements Coverage:**

**✅ Performance Requirements:**
- 3-second tutoring responses: Architecture supports WebSocket connections with pydantic-ai agents optimized for low latency. Redis caching reduces knowledge base query times.
- 30-minute course generation: Prefect workflows enable long-running tasks with progress tracking. Background task pattern supports async course generation.
- 5-second assessment grading: Auto-grading logic in `assessment_service.py` supports fast synchronous grading.
- 3-second page load: Next.js SSR/SSG with image optimization and caching meets requirements.

**✅ Security Requirements:**
- AES-256 encryption at rest: Supabase PostgreSQL provides encryption at rest.
- TLS 1.3+ in transit: All API and WebSocket connections use TLS (FastAPI + Next.js native support).
- JWT authentication: Architecture specifies JWT with refresh tokens in `backend/app/utils/jwt.py` and `frontend/lib/api/auth.ts`.
- Password hashing: Bcrypt/Argon2 specified in `backend/app/utils/password.py`.
- RBAC: Role-based access control specified in authentication middleware and dependencies.
- GDPR compliance: Data deletion (FR71), audit logging (FR73), and privacy policies architecturally supported.

**✅ Scalability Requirements:**
- Horizontal scaling: Docker containers enable horizontal scaling. FastAPI instances can scale independently from Next.js instances.
- 50,000 users within 12 months: Architecture supports horizontal scaling with load balancing. Database scaling via Supabase managed scaling (free → Pro tier).
- 10x growth with <10% degradation: Caching (Redis), CDN (Cloudflare), and stateless API design enable linear scaling.
- 5-20 concurrent course generation: Prefect workflows with RabbitMQ message queues support concurrent long-running tasks.

**✅ Accessibility Requirements:**
- WCAG 2.1 AA compliance: Architecture specifies accessibility components (`SkipToContent.tsx`, `AccessibilitySettings.tsx`), keyboard navigation (FR82), screen reader support (FR83), and text size/contrast settings (FR84).
- Frontend components must meet WCAG standards as specified in implementation patterns.

**✅ Reliability Requirements:**
- 99.5% uptime: Architecture supports container-based deployment with health checks, monitoring (Prometheus), and automated recovery.
- 30-second agent failure detection: Health monitor agent (`health_monitor_agent.py`) and Prefect workflows enable fast failure detection.
- 2-minute automatic recovery: Fallback handlers (`fallback_handler.py`) and Prefect retry mechanisms enable automatic recovery.
- Data integrity: Daily backups, RPO 24 hours, RTO 4 hours supported via Supabase backup features.

### Implementation Readiness Validation ✅

**Decision Completeness:**
All critical decisions are fully documented:

- ✅ **Technology Versions**: All major technologies have version verification notes ("verify during implementation"). Specific commands provided for initialization (e.g., `create-next-app@latest`, `uv add fastapi`).

- ✅ **Architectural Decisions**: All 5 decision categories (Data Architecture, Authentication & Security, API & Communication, Frontend Architecture, Infrastructure & Deployment) are fully documented with rationale, implementation details, and impact analysis.

- ✅ **Implementation Patterns**: Comprehensive patterns defined for naming, structure, format, communication, and process. All patterns include examples and anti-patterns.

- ✅ **Consistency Rules**: Clear enforcement guidelines with linting, type checking, CI/CD validation requirements.

**Structure Completeness:**
Project structure is complete and specific:

- ✅ **Complete Directory Tree**: Full project structure with all files and directories specified, including backend, frontend, infrastructure, tests, scripts, and configuration files.

- ✅ **Integration Points**: All integration points (API endpoints, WebSocket connections, RabbitMQ events, database queries, external APIs) are clearly specified with file locations.

- ✅ **Component Boundaries**: Clear boundaries between backend/frontend, services/agents, orchestration/workflows, models/services, and API routes/services.

- ✅ **Requirements Mapping**: All 88 functional requirements mapped to specific files and directories with FR numbers documented in structure.

**Pattern Completeness:**
All potential conflict points are addressed:

- ✅ **Naming Conventions**: Comprehensive naming patterns for database, API, code (Python and TypeScript), with API boundary conversion strategy.

- ✅ **Structure Patterns**: Complete project organization patterns for backend, frontend, tests, and assets.

- ✅ **Format Patterns**: API response formats, error formats, date/time formats, pagination patterns all specified.

- ✅ **Communication Patterns**: RabbitMQ event patterns, WebSocket message patterns, state management patterns all defined.

- ✅ **Process Patterns**: Error handling, loading states, authentication flows, retry patterns all documented with examples.

### Gap Analysis Results

**Critical Gaps: None Found**
All critical architectural decisions are complete. No blocking gaps identified.

**Important Gaps: None Found**
All important architectural capabilities are specified. Structure and patterns are comprehensive.

**Nice-to-Have Enhancements (Optional):**
- **Agent Communication Examples**: Additional code examples showing agent-to-agent JSON-RPC 2.0 communication patterns could help implementation.
- **Prefect Workflow Templates**: Specific Prefect workflow templates for common patterns (course generation, content generation) could accelerate development.
- **Testing Strategy Details**: More specific testing patterns for agent integration testing and WebSocket testing could be beneficial.
- **Deployment Scripts**: Specific deployment scripts for Railway/Render could help MVP deployment.

**Note**: These enhancements are optional and don't block implementation. The current architecture is complete and ready for AI agents to begin implementation.

### Validation Issues Addressed

**No Critical or Important Issues Found**

All architectural decisions are coherent, all requirements are covered, and implementation patterns are comprehensive. The architecture is ready for implementation handoff.

### Architecture Completeness Checklist

**✅ Requirements Analysis**
- [x] Project context thoroughly analyzed
- [x] Scale and complexity assessed (High/Enterprise - multi-agent orchestration, real-time interactions, self-improving systems)
- [x] Technical constraints identified (Free tier services, MVP timeline, scalability to 50k users)
- [x] Cross-cutting concerns mapped (Security, monitoring, caching, accessibility, compliance)

**✅ Architectural Decisions**
- [x] Critical decisions documented with versions (FastAPI, Next.js, pydantic-ai, Prefect, Supabase, RabbitMQ, Redis)
- [x] Technology stack fully specified (Backend: FastAPI + Python, Frontend: Next.js + TypeScript, Database: Supabase PostgreSQL, Agents: pydantic-ai, Orchestration: Prefect)
- [x] Integration patterns defined (REST API, WebSocket, JSON-RPC 2.0, RabbitMQ events, Supabase queries)
- [x] Performance considerations addressed (Caching, CDN, horizontal scaling, async processing, database optimization)

**✅ Implementation Patterns**
- [x] Naming conventions established (snake_case for Python/DB, camelCase for TypeScript, API boundary conversion)
- [x] Structure patterns defined (Feature-based organization, versioned API routes, Next.js App Router)
- [x] Communication patterns specified (RabbitMQ events, WebSocket messages, state management)
- [x] Process patterns documented (Error handling, loading states, authentication flows, retry patterns)

**✅ Project Structure**
- [x] Complete directory structure defined (Backend: FastAPI API structure, Frontend: Next.js App Router structure, Infrastructure: Docker/Kubernetes)
- [x] Component boundaries established (API boundaries, service boundaries, data boundaries, integration points)
- [x] Integration points mapped (Internal communication, external APIs, data flow patterns)
- [x] Requirements to structure mapping complete (All 88 FRs mapped to specific files and directories)

### Architecture Readiness Assessment

**Overall Status:** ✅ **READY FOR IMPLEMENTATION**

**Confidence Level:** **HIGH** - The architecture is comprehensive, coherent, and complete. All requirements are covered, all decisions are documented, all patterns are specified, and the project structure is detailed and specific.

**Key Strengths:**
- **Complete Requirements Coverage**: All 88 functional requirements and all non-functional requirements are architecturally supported and mapped to specific implementation locations.
- **Clear Decision Documentation**: All architectural decisions include rationale, implementation details, and impact analysis.
- **Comprehensive Patterns**: Implementation patterns cover all potential conflict points with examples and anti-patterns.
- **Specific Project Structure**: Complete directory structure with all files specified, not generic placeholders.
- **Clear Boundaries**: Architectural boundaries (API, component, service, data) are well-defined and structured.
- **Technology Compatibility**: All technology choices work together seamlessly without conflicts.
- **Scalability**: Architecture supports growth from MVP (5k users) to production (50k users) without redesign.

**Areas for Future Enhancement:**
- Additional code examples for complex agent-to-agent communication patterns
- Prefect workflow templates for common orchestration patterns
- More detailed testing patterns for agent integration and WebSocket testing
- Specific deployment automation scripts for MVP platforms

**Note**: These enhancements are optional and don't impact implementation readiness. The architecture is complete and ready for AI agents to begin consistent implementation.

### Implementation Handoff

**AI Agent Guidelines:**

All AI agents implementing this architecture MUST:

1. **Follow All Architectural Decisions Exactly**: Use the specified technology stack (FastAPI, Next.js, pydantic-ai, Prefect, Supabase, etc.) with versions verified during implementation.

2. **Use Implementation Patterns Consistently**: Follow all naming conventions, structure patterns, format patterns, communication patterns, and process patterns exactly as documented. Refer to pattern examples and avoid anti-patterns.

3. **Respect Project Structure and Boundaries**: Implement features in the specified directories and files. Maintain clear boundaries between backend/frontend, services/agents, and models/services.

4. **Map Requirements to Implementation**: Refer to the "Requirements to Structure Mapping" section to ensure each functional requirement is implemented in the correct location.

5. **Maintain Architectural Coherence**: Ensure all implementation aligns with the documented architectural decisions. Don't introduce new technologies or patterns without updating the architecture document first.

6. **Reference This Document**: Use this architecture document as the single source of truth for all architectural questions. All decisions, patterns, and structure are documented here.

**First Implementation Priority:**

Based on the architecture, the first implementation step should be:

1. **Initialize Project Structure**: Create the complete directory structure as specified in "Project Structure & Boundaries" section.

2. **Backend Setup**: Initialize FastAPI backend with dependencies:
   ```bash
   cd backend
   uv sync  # Installs all dependencies from pyproject.toml
   ```

3. **Frontend Setup**: Initialize Next.js frontend:
   ```bash
   cd frontend
   npx create-next-app@latest . --typescript --tailwind --app --no-src-dir --import-alias "@/*"
   npm install axios @tanstack/react-query zustand
   ```

4. **Database Setup**: Configure Supabase connection and initialize Alembic migrations:
   ```bash
   cd backend
   alembic init migrations
   # Configure alembic.ini with database connection
   ```

5. **Development Environment**: Set up Docker Compose for local development:
   ```bash
   docker-compose up -d  # Starts backend, frontend, Redis, RabbitMQ
   ```

6. **First Feature**: Implement user authentication (FR1-FR4) as specified in `backend/app/api/v1/auth.py` and `frontend/app/(auth)/` pages, following all patterns and structure exactly as documented.

**Architecture Document Status:**
✅ **COMPLETE AND READY FOR IMPLEMENTATION**

All sections completed:
- ✅ Project Context Analysis
- ✅ Starter Template Evaluation  
- ✅ Core Architectural Decisions (5 categories)
- ✅ Implementation Patterns & Consistency Rules
- ✅ Project Structure & Boundaries
- ✅ Architecture Validation Results

The architecture document is now a comprehensive guide for consistent, coherent implementation by AI agents.

