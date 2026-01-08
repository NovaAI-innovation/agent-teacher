#!/bin/bash
# Stop development environment script
# This script stops all Docker Compose services

set -e

echo "=== Stopping Development Environment ==="
echo ""

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker is not installed or not in PATH."
    exit 1
fi

# Check if docker-compose.yml exists
if [ ! -f "docker-compose.yml" ]; then
    echo "ERROR: docker-compose.yml not found in current directory."
    echo "Please run this script from the project root."
    exit 1
fi

# Stop services
echo "Stopping Docker Compose services..."
docker-compose down

echo ""
echo "=== Development Environment Stopped ==="
echo ""
