# Stop development environment script
# This script stops all Docker Compose services

$ErrorActionPreference = "Stop"

Write-Host "=== Stopping Development Environment ===" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is available
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Docker is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

# Check if docker-compose.yml exists
if (-not (Test-Path "docker-compose.yml")) {
    Write-Host "ERROR: docker-compose.yml not found in current directory." -ForegroundColor Red
    Write-Host "Please run this script from the project root." -ForegroundColor Yellow
    exit 1
}

# Stop services
Write-Host "Stopping Docker Compose services..." -ForegroundColor Yellow
try {
    docker-compose down

    Write-Host ""
    Write-Host "=== Development Environment Stopped ===" -ForegroundColor Green
    Write-Host ""

} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to stop services: $_" -ForegroundColor Red
    exit 1
}
