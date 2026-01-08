# Setup script for agent-teacher project
# This script initializes the development environment

param(
    [switch]$SkipEnv
)

$ErrorActionPreference = "Stop"

Write-Host "=== Agent Teacher Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check if required tools are installed
Write-Host "Checking prerequisites..." -ForegroundColor Yellow

# Check for uv
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: uv is not installed. Please install uv first." -ForegroundColor Red
    Write-Host "Visit: https://github.com/astral-sh/uv" -ForegroundColor Yellow
    exit 1
}

# Check for Node.js
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Node.js is not installed. Please install Node.js first." -ForegroundColor Red
    Write-Host "Visit: https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

# Check for Docker
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "WARNING: Docker is not installed. Docker Compose features will not work." -ForegroundColor Yellow
}

Write-Host "✓ Prerequisites check passed" -ForegroundColor Green
Write-Host ""

# Setup backend
Write-Host "Setting up backend..." -ForegroundColor Yellow
Push-Location backend
try {
    Write-Host "  Installing backend dependencies with uv..." -ForegroundColor Gray
    uv sync
    Write-Host "  ✓ Backend dependencies installed" -ForegroundColor Green

    # Setup pre-commit hooks
    if (Test-Path ".pre-commit-config.yaml") {
        Write-Host "  Installing pre-commit hooks..." -ForegroundColor Gray
        uv run pre-commit install
        Write-Host "  ✓ Pre-commit hooks installed" -ForegroundColor Green
    }
} catch {
    Write-Host "  ✗ Error setting up backend: $_" -ForegroundColor Red
    Pop-Location
    exit 1
} finally {
    Pop-Location
}
Write-Host ""

# Setup frontend
Write-Host "Setting up frontend..." -ForegroundColor Yellow
Push-Location frontend
try {
    Write-Host "  Installing frontend dependencies..." -ForegroundColor Gray
    npm install
    Write-Host "  ✓ Frontend dependencies installed" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Error setting up frontend: $_" -ForegroundColor Red
    Pop-Location
    exit 1
} finally {
    Pop-Location
}
Write-Host ""

# Setup environment files
if (-not $SkipEnv) {
    Write-Host "Setting up environment files..." -ForegroundColor Yellow

    # Backend .env
    if (-not (Test-Path "backend/.env")) {
        if (Test-Path "backend/.env.example") {
            Write-Host "  Copying backend/.env.example to backend/.env..." -ForegroundColor Gray
            Copy-Item "backend/.env.example" "backend/.env"
            Write-Host "  ✓ Backend .env file created" -ForegroundColor Green
            Write-Host "  ⚠ Please update backend/.env with your configuration" -ForegroundColor Yellow
        } else {
            Write-Host "  ⚠ backend/.env.example not found. Please create backend/.env manually." -ForegroundColor Yellow
        }
    } else {
        Write-Host "  ✓ Backend .env file already exists" -ForegroundColor Green
    }

    # Frontend .env.local
    if (-not (Test-Path "frontend/.env.local")) {
        if (Test-Path "frontend/.env.local.example") {
            Write-Host "  Copying frontend/.env.local.example to frontend/.env.local..." -ForegroundColor Gray
            Copy-Item "frontend/.env.local.example" "frontend/.env.local"
            Write-Host "  ✓ Frontend .env.local file created" -ForegroundColor Green
            Write-Host "  ⚠ Please update frontend/.env.local with your configuration" -ForegroundColor Yellow
        } else {
            Write-Host "  ⚠ frontend/.env.local.example not found. Please create frontend/.env.local manually." -ForegroundColor Yellow
        }
    } else {
        Write-Host "  ✓ Frontend .env.local file already exists" -ForegroundColor Green
    }
    Write-Host ""
}

Write-Host "=== Setup Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Update backend/.env with your configuration" -ForegroundColor White
Write-Host "  2. Update frontend/.env.local with your configuration" -ForegroundColor White
Write-Host "  3. Run scripts/start-dev.ps1 to start the development environment" -ForegroundColor White
Write-Host ""
