# Story 4.4: Connect to External AI/LLM Services

Status: ready-for-dev

## Story

As the system,
I want to connect to external AI/LLM services,
so that agents can generate high-quality content.

## Acceptance Criteria

1. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** API connections are authenticated securely
2. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** API keys are stored in secure key management system
3. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** Rate limiting is implemented per service (FR78)
4. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** API usage costs are monitored and capped (FR79)
5. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** Failed API calls are logged and retried with exponential backoff
6. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** API failures are handled gracefully without blocking content generation
7. **Given** Agents need to use AI/LLM services **When** An agent makes an API call to an external service **Then** Cost monitoring alerts are triggered when approaching limits

## Tasks / Subtasks

- [ ] Task 1: Create LLM service client (AC: 1, 2)
  - [ ] Create `backend/app/services/llm/llm_client.py`
  - [ ] Support multiple LLM providers (OpenAI, Anthropic, etc.)
  - [ ] Implement secure authentication
  - [ ] Load API keys from secure storage (environment variables or key management)
- [ ] Task 2: Implement rate limiting (AC: 3)
  - [ ] Create rate limiter per LLM service
  - [ ] Configure rate limits per service
  - [ ] Track API call rates
  - [ ] Enforce rate limits
- [ ] Task 3: Implement cost monitoring (AC: 4, 7)
  - [ ] Create `backend/app/services/monitoring/cost_monitor.py`
  - [ ] Track API usage costs per service
  - [ ] Calculate costs based on usage (tokens, requests)
  - [ ] Set cost caps per service
  - [ ] Create alert system for approaching limits
- [ ] Task 4: Implement retry logic (AC: 5)
  - [ ] Add retry logic to LLM client
  - [ ] Use exponential backoff
  - [ ] Log failed API calls
- [ ] Task 5: Handle API failures gracefully (AC: 6)
  - [ ] Implement error handling
  - [ ] Don't block content generation on API failures
  - [ ] Use fallback mechanisms
- [ ] Task 6: Create API usage tracking (AC: 4)
  - [ ] Create `backend/app/models/api_usage.py`
  - [ ] Track API calls, tokens, costs
  - [ ] Create database migration

## Dev Notes

- **Architecture Patterns**: Secure API key management. Rate limiting per service. Cost monitoring and capping. Graceful failure handling.
- **Source Tree Components**: 
  - `backend/app/services/llm/llm_client.py` - LLM service client
  - `backend/app/services/monitoring/cost_monitor.py` - Cost monitoring
  - `backend/app/models/api_usage.py` - API usage tracking model
  - `backend/app/utils/rate_limiter.py` - Rate limiting utilities
- **Testing Standards**: Unit tests for LLM client, rate limiting, cost monitoring. Integration tests for API calls.
- **Dependencies**: Epic 1 must be complete (Infrastructure), Story 4.1 must be complete (Agent orchestration)
- **Security**: API keys in secure storage. Never log API keys. Use environment variables or key management service.

### Project Structure Notes

- **Alignment**: LLM integration follows architecture.md external service patterns. Secure key management.
- **Rate Limiting**: Per-service rate limits to avoid exceeding API quotas
- **Cost Monitoring**: Track and cap costs to control spending. Alert when approaching limits.
- **Failure Handling**: Graceful degradation when APIs fail. Don't block entire workflow.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#External Services] - LLM service integration patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR78, FR79] - FR78: Rate Limiting, FR79: Cost Monitoring requirements
- [Source: _bmad-output/planning-artifacts/epics.md#Story 4.4] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_

