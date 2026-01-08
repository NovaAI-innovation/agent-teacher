#!/bin/bash
# Setup script for agent-teacher project
# This script initializes the development environment

set -e

echo "=== Agent Teacher Setup ==="
echo ""

# Check if required tools are installed
echo "Checking prerequisites..."

if ! command -v uv &> /dev/null; then
    echo "ERROR: uv is not installed. Please install uv first."
    echo "Visit: https://github.com/astral-sh/uv"
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed. Please install Node.js first."
    echo "Visit: https://nodejs.org/"
    exit 1
fi

if ! command -v docker &> /dev/null; then
    echo "WARNING: Docker is not installed. Docker Compose features will not work."
fi

echo "✓ Prerequisites check passed"
echo ""

# Setup backend
echo "Setting up backend..."
cd backend
echo "  Installing backend dependencies with uv..."
uv sync
echo "  ✓ Backend dependencies installed"

# Setup pre-commit hooks
if [ -f ".pre-commit-config.yaml" ]; then
    echo "  Installing pre-commit hooks..."
    uv run pre-commit install
    echo "  ✓ Pre-commit hooks installed"
fi
cd ..
echo ""

# Setup frontend
echo "Setting up frontend..."
cd frontend
echo "  Installing frontend dependencies..."
npm install
echo "  ✓ Frontend dependencies installed"
cd ..
echo ""

# Setup environment files
echo "Setting up environment files..."

# Backend .env
if [ ! -f "backend/.env" ]; then
    if [ -f "backend/.env.example" ]; then
        echo "  Copying backend/.env.example to backend/.env..."
        cp backend/.env.example backend/.env
        echo "  ✓ Backend .env file created"
        echo "  ⚠ Please update backend/.env with your configuration"
    else
        echo "  ⚠ backend/.env.example not found. Please create backend/.env manually."
    fi
else
    echo "  ✓ Backend .env file already exists"
fi

# Frontend .env.local
if [ ! -f "frontend/.env.local" ]; then
    if [ -f "frontend/.env.local.example" ]; then
        echo "  Copying frontend/.env.local.example to frontend/.env.local..."
        cp frontend/.env.local.example frontend/.env.local
        echo "  ✓ Frontend .env.local file created"
        echo "  ⚠ Please update frontend/.env.local with your configuration"
    else
        echo "  ⚠ frontend/.env.local.example not found. Please create frontend/.env.local manually."
    fi
else
    echo "  ✓ Frontend .env.local file already exists"
fi
echo ""

echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "  1. Update backend/.env with your configuration"
echo "  2. Update frontend/.env.local with your configuration"
echo "  3. Run scripts/start-dev.sh to start the development environment"
echo ""
