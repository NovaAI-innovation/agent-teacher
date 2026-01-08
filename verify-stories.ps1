# Story Verification Script
Write-Host "=== Story Verification ===" -ForegroundColor Cyan

# Story 1.1: Git repo and structure
Write-Host "`nStory 1.1: Git Repository and Project Structure" -ForegroundColor Yellow
$story1_1 = @{
    ".gitignore" = Test-Path ".gitignore"
    "backend/" = Test-Path "backend"
    "frontend/" = Test-Path "frontend"
    "infrastructure/" = Test-Path "infrastructure"
    "scripts/" = Test-Path "scripts"
    "backend/__init__.py" = Test-Path "backend/__init__.py"
    "backend/app/__init__.py" = Test-Path "backend/app/__init__.py"
}
foreach ($item in $story1_1.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.2: Documentation
Write-Host "`nStory 1.2: Project Documentation" -ForegroundColor Yellow
$story1_2 = @{
    "README.md" = Test-Path "README.md"
    ".env.example" = Test-Path ".env.example"
}
foreach ($item in $story1_2.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.3: Backend structure
Write-Host "`nStory 1.3: Backend Directory Structure" -ForegroundColor Yellow
$story1_3 = @{
    "backend/app/api/v1/" = Test-Path "backend/app/api/v1"
    "backend/app/services/agents/" = Test-Path "backend/app/services/agents"
    "backend/app/services/orchestration/" = Test-Path "backend/app/services/orchestration"
    "backend/app/services/knowledge/" = Test-Path "backend/app/services/knowledge"
    "backend/app/models/" = Test-Path "backend/app/models"
    "backend/app/middleware/" = Test-Path "backend/app/middleware"
    "backend/app/utils/" = Test-Path "backend/app/utils"
    "backend/orchestration/workflows/" = Test-Path "backend/orchestration/workflows"
    "backend/orchestration/tasks/" = Test-Path "backend/orchestration/tasks"
    "backend/migrations/versions/" = Test-Path "backend/migrations/versions"
    "backend/tests/unit/" = Test-Path "backend/tests/unit"
    "backend/tests/integration/" = Test-Path "backend/tests/integration"
    "backend/tests/e2e/" = Test-Path "backend/tests/e2e"
}
foreach ($item in $story1_3.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.4: Backend dependencies
Write-Host "`nStory 1.4: Backend Dependencies" -ForegroundColor Yellow
$story1_4 = @{
    "backend/pyproject.toml" = Test-Path "backend/pyproject.toml"
    "backend/uv.lock" = Test-Path "backend/uv.lock"
}
foreach ($item in $story1_4.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.5: Backend environment
Write-Host "`nStory 1.5: Backend Environment Configuration" -ForegroundColor Yellow
$story1_5 = @{
    "backend/.env.example" = Test-Path "backend/.env.example"
    "backend/app/config.py" = Test-Path "backend/app/config.py"
}
foreach ($item in $story1_5.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.6: Database and services
Write-Host "`nStory 1.6: Database and Service Connections" -ForegroundColor Yellow
$story1_6 = @{
    "backend/app/models/database.py" = Test-Path "backend/app/models/database.py"
    "backend/app/services/knowledge/supabase_client.py" = Test-Path "backend/app/services/knowledge/supabase_client.py"
    "backend/app/utils/redis_client.py" = Test-Path "backend/app/utils/redis_client.py"
    "backend/app/utils/rabbitmq_client.py" = Test-Path "backend/app/utils/rabbitmq_client.py"
}
foreach ($item in $story1_6.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.7: FastAPI app
Write-Host "`nStory 1.7: FastAPI Application" -ForegroundColor Yellow
$story1_7 = @{
    "backend/app/main.py" = Test-Path "backend/app/main.py"
    "backend/app/api/v1/health.py" = Test-Path "backend/app/api/v1/health.py"
}
foreach ($item in $story1_7.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.8: API routers
Write-Host "`nStory 1.8: API Router Structure" -ForegroundColor Yellow
$story1_8 = @{
    "backend/app/api/v1/auth.py" = Test-Path "backend/app/api/v1/auth.py"
    "backend/app/api/v1/courses.py" = Test-Path "backend/app/api/v1/courses.py"
    "backend/app/api/v1/learning.py" = Test-Path "backend/app/api/v1/learning.py"
    "backend/app/api/v1/tutoring.py" = Test-Path "backend/app/api/v1/tutoring.py"
    "backend/app/api/v1/assessments.py" = Test-Path "backend/app/api/v1/assessments.py"
    "backend/app/api/v1/progress.py" = Test-Path "backend/app/api/v1/progress.py"
    "backend/app/api/v1/admin.py" = Test-Path "backend/app/api/v1/admin.py"
}
foreach ($item in $story1_8.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.9: Middleware
Write-Host "`nStory 1.9: Middleware and Utilities" -ForegroundColor Yellow
$story1_9 = @{
    "backend/app/middleware/cors.py" = Test-Path "backend/app/middleware/cors.py"
    "backend/app/middleware/error_handler.py" = Test-Path "backend/app/middleware/error_handler.py"
    "backend/app/middleware/logging.py" = Test-Path "backend/app/middleware/logging.py"
    "backend/app/middleware/rate_limiting.py" = Test-Path "backend/app/middleware/rate_limiting.py"
    "backend/app/middleware/security.py" = Test-Path "backend/app/middleware/security.py"
    "backend/app/utils/logger.py" = Test-Path "backend/app/utils/logger.py"
    "backend/app/utils/exceptions.py" = Test-Path "backend/app/utils/exceptions.py"
}
foreach ($item in $story1_9.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.10: Models and migrations
Write-Host "`nStory 1.10: Models and Migrations" -ForegroundColor Yellow
$story1_10 = @{
    "backend/app/models/base.py" = Test-Path "backend/app/models/base.py"
    "backend/migrations/env.py" = Test-Path "backend/migrations/env.py"
    "backend/migrations/alembic.ini" = Test-Path "backend/alembic.ini"
}
foreach ($item in $story1_10.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.11: Testing
Write-Host "`nStory 1.11: Testing Infrastructure" -ForegroundColor Yellow
$story1_11 = @{
    "backend/tests/conftest.py" = Test-Path "backend/tests/conftest.py"
    "backend/tests/unit/" = Test-Path "backend/tests/unit"
    "backend/tests/integration/" = Test-Path "backend/tests/integration"
    "backend/tests/e2e/" = Test-Path "backend/tests/e2e"
}
foreach ($item in $story1_11.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.12: Pre-commit
Write-Host "`nStory 1.12: Development Tooling" -ForegroundColor Yellow
$story1_12 = @{
    "backend/.pre-commit-config.yaml" = Test-Path "backend/.pre-commit-config.yaml"
}
foreach ($item in $story1_12.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.13: Frontend Next.js
Write-Host "`nStory 1.13: Frontend Next.js" -ForegroundColor Yellow
$story1_13 = @{
    "frontend/package.json" = Test-Path "frontend/package.json"
    "frontend/tsconfig.json" = Test-Path "frontend/tsconfig.json"
    "frontend/tailwind.config.ts" = Test-Path "frontend/tailwind.config.ts"
    "frontend/app/" = Test-Path "frontend/app"
}
foreach ($item in $story1_13.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.14: Frontend environment
Write-Host "`nStory 1.14: Frontend Environment" -ForegroundColor Yellow
$story1_14 = @{
    "frontend/.env.local.example" = Test-Path "frontend/.env.local.example"
    "frontend/.env.local" = Test-Path "frontend/.env.local"
}
foreach ($item in $story1_14.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

# Story 1.15: Frontend API client
Write-Host "`nStory 1.15: Frontend API Client" -ForegroundColor Yellow
$story1_15 = @{
    "frontend/lib/api/client.ts" = Test-Path "frontend/lib/api/client.ts"
    "frontend/lib/api/endpoints.ts" = Test-Path "frontend/lib/api/endpoints.ts"
    "frontend/lib/api/auth.ts" = Test-Path "frontend/lib/api/auth.ts"
    "frontend/lib/api/courses.ts" = Test-Path "frontend/lib/api/courses.ts"
    "frontend/lib/api/learning.ts" = Test-Path "frontend/lib/api/learning.ts"
    "frontend/lib/api/assessments.ts" = Test-Path "frontend/lib/api/assessments.ts"
    "frontend/lib/api/tutoring.ts" = Test-Path "frontend/lib/api/tutoring.ts"
    "frontend/lib/api/progress.ts" = Test-Path "frontend/lib/api/progress.ts"
    "frontend/lib/api/admin.ts" = Test-Path "frontend/lib/api/admin.ts"
    "frontend/lib/websocket/client.ts" = Test-Path "frontend/lib/websocket/client.ts"
    "frontend/lib/websocket/handlers.ts" = Test-Path "frontend/lib/websocket/handlers.ts"
    "frontend/lib/websocket/reconnect.ts" = Test-Path "frontend/lib/websocket/reconnect.ts"
}
foreach ($item in $story1_15.GetEnumerator()) {
    $status = if ($item.Value) { "✓" } else { "✗" }
    Write-Host "  $status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

Write-Host "`n=== Verification Complete ===" -ForegroundColor Cyan
