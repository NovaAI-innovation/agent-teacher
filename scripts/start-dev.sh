#!/bin/bash
# Start development environment script
# This script starts all services using Docker Compose

set -e

echo "=== Starting Development Environment ==="
echo ""

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed or not in PATH."
    echo "Please install Docker: https://www.docker.com/"
    exit 1
fi

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo "ERROR: docker-compose.yml not found in current directory."
    echo "Please run this script from the project root."
    exit 1
fi

# Start services
echo "Starting Docker Compose services..."
docker-compose up -d

echo ""
echo "Waiting for services to be healthy..."
sleep 5

# Check service status
echo ""
echo "Service Status:"
docker-compose ps

echo ""
echo "=== Development Environment Started ==="
echo ""
echo "Service URLs:"
echo "  Backend API:    http://localhost:8000"
echo "  Backend Docs:   http://localhost:8000/docs"
echo "  Frontend:       http://localhost:3000"
echo "  Redis:          localhost:6379"
echo "  RabbitMQ:       localhost:5672"
echo "  RabbitMQ UI:    http://localhost:15672 (guest/guest)"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop:      scripts/stop-dev.sh"
echo ""
