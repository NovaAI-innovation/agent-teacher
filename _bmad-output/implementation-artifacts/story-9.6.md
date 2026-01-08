# Story 9.6: Manage User Accounts and Permissions

Status: ready-for-dev

## Story

As an administrator,
I want to manage user accounts and permissions,
so that I can control access to the platform.

## Acceptance Criteria

1. **Given** I am an administrator **When** I manage users **Then** I can view all user accounts (FR57)
2. **Given** I am an administrator **When** I manage users **Then** I can view user details (email, enrollment status, progress)
3. **Given** I am an administrator **When** I manage users **Then** I can manage user permissions and roles
4. **Given** I am an administrator **When** I manage users **Then** I can deactivate or activate user accounts
5. **Given** I am an administrator **When** I manage users **Then** I can search and filter users
6. **Given** I am an administrator **When** I manage users **Then** User management interface is accessible and secure

## Tasks / Subtasks

- [ ] Task 1: Create user management API (AC: 1, 2, 3, 4, 5)
  - [ ] Create `backend/app/api/v1/admin/users.py`
  - [ ] Return all users
  - [ ] Return user details
  - [ ] Support user updates (permissions, roles, status)
  - [ ] Support search and filtering
  - [ ] Require admin authentication
- [ ] Task 2: Create user management page (AC: 1, 2, 3, 4, 5, 6)
  - [ ] Create `frontend/app/admin/users/page.tsx`
  - [ ] Display user list
  - [ ] Show user details
  - [ ] Allow permission/role management
  - [ ] Allow account activation/deactivation
  - [ ] Add search and filters
  - [ ] Make accessible and secure
- [ ] Task 3: Create user detail component (AC: 2, 3, 4)
  - [ ] Create `frontend/components/admin/UserDetail.tsx`
  - [ ] Display user information
  - [ ] Allow permission editing
  - [ ] Allow status changes
- [ ] Task 4: Implement RBAC (AC: 3)
  - [ ] Create role model
  - [ ] Create permission model
  - [ ] Assign roles to users
  - [ ] Enforce permissions

## Dev Notes

- **Architecture Patterns**: User management. RBAC. Secure access control.
- **Source Tree Components**:
  - `backend/app/api/v1/admin/users.py` - User management API
  - `backend/app/models/role.py` - Role model
  - `backend/app/models/permission.py` - Permission model
  - `frontend/app/admin/users/page.tsx` - User management page
  - `frontend/components/admin/UserDetail.tsx` - User detail component
- **Testing Standards**: Unit tests for components, integration tests for API, security tests
- **Dependencies**: Story 2.1 must be complete (User model), Story 2.2 must be complete (Authentication)
- **Security**: Require admin authentication. Secure user management. RBAC enforcement.

### Project Structure Notes

- **Alignment**: User management follows architecture.md admin patterns. Secure and comprehensive.
- **RBAC**: Implement role-based access control. Assign roles and permissions.
- **User Details**: Show user information, enrollment, progress. Support management actions.
- **Security**: Secure user management. Require admin privileges. Audit user changes.

### References

- [Source: _bmad-output/planning-artifacts/architecture.md#Administration] - User management patterns
- [Source: _bmad-output/planning-artifacts/prd.md#FR57] - FR57: Manage Users requirement
- [Source: _bmad-output/planning-artifacts/epics.md#Story 9.6] - Original story definition

## Dev Agent Record

### Agent Model Used

_To be filled by dev agent_

### Debug Log References

_To be filled by dev agent_

### Completion Notes List

_To be filled by dev agent_

### File List

_To be filled by dev agent_
