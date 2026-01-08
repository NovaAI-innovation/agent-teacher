# Start development environment script
# This script starts all services using Docker Compose

$ErrorActionPreference = "Stop"

Write-Host "=== Starting Development Environment ===" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is available
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Docker is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Docker Desktop: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit 1
}

# Check if docker-compose.yml exists
if (-not (Test-Path "docker-compose.yml")) {
    Write-Host "ERROR: docker-compose.yml not found in current directory." -ForegroundColor Red
    Write-Host "Please run this script from the project root." -ForegroundColor Yellow
    exit 1
}

# Start services
Write-Host "Starting Docker Compose services..." -ForegroundColor Yellow
try {
    docker-compose up -d

    Write-Host ""
    Write-Host "Waiting for services to be healthy..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5

    # Check service status
    Write-Host ""
    Write-Host "Service Status:" -ForegroundColor Cyan
    docker-compose ps

    Write-Host ""
    Write-Host "=== Development Environment Started ===" -ForegroundColor Green
    Write-Host ""
    Write-Host "Service URLs:" -ForegroundColor Yellow
    Write-Host "  Backend API:    http://localhost:8000" -ForegroundColor White
    Write-Host "  Backend Docs:   http://localhost:8000/docs" -ForegroundColor White
    Write-Host "  Frontend:       http://localhost:3000" -ForegroundColor White
    Write-Host "  Redis:          localhost:6379" -ForegroundColor White
    Write-Host "  RabbitMQ:       localhost:5672" -ForegroundColor White
    Write-Host "  RabbitMQ UI:    http://localhost:15672 (guest/guest)" -ForegroundColor White
    Write-Host ""
    Write-Host "To view logs: docker-compose logs -f" -ForegroundColor Gray
    Write-Host "To stop:      scripts/stop-dev.ps1" -ForegroundColor Gray
    Write-Host ""

} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to start services: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  1. Ensure Docker Desktop is running" -ForegroundColor White
    Write-Host "  2. Check if ports 3000, 8000, 6379, 5672, 15672 are available" -ForegroundColor White
    Write-Host "  3. Run 'docker-compose logs' to see error messages" -ForegroundColor White
    exit 1
}
