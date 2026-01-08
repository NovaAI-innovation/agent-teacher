# agent-teacher

An autonomous learning platform that eliminates the traditional bottleneck of educational content creation through AI-driven automation. The platform serves individuals interested in learning AI and its subcategories, delivering high-quality educational content at a pace and scale impossible for human teams to achieve.

## Project Overview

agent-teacher (MENTOR-web) is a full-stack web application that autonomously generates educational content using a multi-agent AI architecture. The platform enables learners to access comprehensive courses on-demand, with content that adapts and improves over time through autonomous self-improvement mechanisms.

### Key Features

- **Autonomous Content Generation**: Multi-agent system generates courses, units, modules, and assessments automatically
- **Real-Time Interactive Tutoring**: WebSocket-based chat tutoring with context-aware responses
- **Self-Improving Platform**: Continuous quality improvement through feedback loops and optimization algorithms
- **Progress Tracking**: Comprehensive progress tracking at module, unit, and course levels
- **Quality Assurance**: Automated quality benchmarks and content evaluation

## Architecture Summary

### Technology Stack

**Backend:**
- **Framework**: FastAPI (Python 3.12+)
- **Package Manager**: `uv`
- **ORM**: SQLModel (built on SQLAlchemy)
- **Database**: Supabase (PostgreSQL)
- **Agent Framework**: pydantic-ai
- **Orchestration**: Prefect
- **Message Queue**: RabbitMQ
- **Caching**: Redis
- **Migrations**: Alembic

**Frontend:**
- **Framework**: Next.js (App Router, SSR/SSG)
- **Language**: TypeScript
- **Package Manager**: `npm`
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Data Fetching**: React Query
- **HTTP Client**: Axios

**Infrastructure:**
- **Containerization**: Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus, Loki, Jaeger

### Project Structure

```
agent-teacher/
├── backend/              # FastAPI backend application
│   ├── app/             # Main application package
│   │   ├── api/         # API routes (versioned)
│   │   ├── services/    # Business logic layer
│   │   ├── models/      # Database models
│   │   ├── middleware/  # FastAPI middleware
│   │   └── utils/       # Utility functions
│   ├── agents/          # Standalone agent definitions
│   ├── orchestration/   # Prefect workflows and tasks
│   ├── migrations/      # Alembic database migrations
│   └── tests/           # Backend tests
├── frontend/             # Next.js frontend application
│   ├── app/             # Next.js App Router
│   ├── components/      # React components
│   └── lib/             # Utilities and helpers
├── infrastructure/       # Infrastructure as code
├── scripts/             # Utility scripts
└── _bmad-output/        # BMAD workflow artifacts
```

### Multi-Agent Architecture

The platform uses a hierarchical orchestration pattern with specialized agents:

- **Curriculum Agent**: Designs course structure and learning paths
- **Content Agent**: Generates text-based learning content
- **Tutor Agent**: Provides interactive tutoring sessions
- **QA Agent**: Evaluates content quality against benchmarks
- **Optimizer Agent**: Identifies and implements platform improvements
- **Health Monitor Agent**: Monitors agent health and performance

Agents communicate via JSON-RPC 2.0 for agent-to-agent communication and REST APIs for orchestrator-to-agent task assignment. Real-time tutoring uses WebSocket connections.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.12+**: Required for backend development
- **Node.js 18+**: Required for frontend development
- **Docker & Docker Compose**: Required for local development environment
- **Git**: Version control
- **uv**: Python package manager (install via: `pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Optional but Recommended

- **Supabase Account**: For database hosting (free tier available)
- **LLM API Keys**: OpenAI, Anthropic, or Google Gemini API keys for agent functionality
- **Prefect Cloud Account**: For workflow orchestration (free tier available)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd agent-teacher
```

### 2. Configure Environment Variables

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your actual values:
- Database connection strings (Supabase)
- API keys (OpenAI, Anthropic, etc.)
- Service URLs (Redis, RabbitMQ, Prefect)

See `.env.example` for detailed descriptions of each variable.

### 3. Backend Setup

```bash
cd backend
uv sync
```

This will:
- Install all Python dependencies
- Generate `uv.lock` file
- Set up the Python virtual environment

### 4. Frontend Setup

```bash
cd frontend
npm install
```

This will:
- Install all Node.js dependencies
- Generate `package-lock.json` file

### 5. Start Development Environment

From the project root:

```bash
docker-compose up -d
```

This starts:
- Backend API server (port 8000)
- Frontend dev server (port 3000)
- Redis (port 6379)
- RabbitMQ (ports 5672, 15672)

### 6. Initialize Database

```bash
cd backend
uv run alembic upgrade head
```

This runs all database migrations to set up the schema.

## Development Workflow

### Running the Backend

```bash
cd backend
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### Running the Frontend

```bash
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Running Tests

**Backend Tests:**
```bash
cd backend
uv run pytest
```

**Frontend Tests:**
```bash
cd frontend
npm test
```

**E2E Tests:**
```bash
cd frontend
npm run test:e2e
```

### Code Quality

**Backend:**
```bash
cd backend
uv run black .          # Format code
uv run ruff check .     # Lint code
uv run mypy .           # Type checking
```

**Frontend:**
```bash
cd frontend
npm run lint            # ESLint
npm run format          # Prettier
```

### Database Migrations

**Create a new migration:**
```bash
cd backend
uv run alembic revision --autogenerate -m "description"
```

**Apply migrations:**
```bash
uv run alembic upgrade head
```

**Rollback migration:**
```bash
uv run alembic downgrade -1
```

## Commands Reference

### Setup Commands

```bash
# Initial project setup
./scripts/setup.sh

# Start development environment
./scripts/start-dev.sh

# Stop development environment
./scripts/stop-dev.sh
```

### Backend Commands

```bash
# Install dependencies
cd backend && uv sync

# Run development server
cd backend && uv run uvicorn app.main:app --reload

# Run tests
cd backend && uv run pytest

# Run linting
cd backend && uv run ruff check .

# Format code
cd backend && uv run black .
```

### Frontend Commands

```bash
# Install dependencies
cd frontend && npm install

# Run development server
cd frontend && npm run dev

# Build for production
cd frontend && npm run build

# Run tests
cd frontend && npm test

# Run linting
cd frontend && npm run lint
```

### Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Restart a specific service
docker-compose restart backend
```

## Troubleshooting

### Backend Issues

**Import errors:**
- Ensure you're using `uv run` to execute commands
- Verify virtual environment is activated: `uv venv`

**Database connection errors:**
- Check `.env` file has correct Supabase credentials
- Verify Supabase project is active
- Test connection: `uv run python -c "from app.config import settings; print(settings.supabase_url)"`

**Port already in use:**
- Change port in `.env` or `docker-compose.yml`
- Kill process using port: `lsof -ti:8000 | xargs kill` (macOS/Linux)

### Frontend Issues

**Module not found errors:**
- Run `npm install` to ensure all dependencies are installed
- Clear `.next` cache: `rm -rf .next`

**Port already in use:**
- Change port in `package.json` scripts or `.env.local`
- Kill process: `lsof -ti:3000 | xargs kill` (macOS/Linux)

### Docker Issues

**Container won't start:**
- Check logs: `docker-compose logs [service-name]`
- Verify Docker is running: `docker ps`
- Rebuild containers: `docker-compose up -d --build`

**Volume mount issues:**
- Ensure file permissions are correct
- Check `docker-compose.yml` volume paths

### Environment Variable Issues

**Variables not loading:**
- Ensure `.env` file exists in project root
- Check variable names match exactly (case-sensitive)
- Restart services after changing `.env`

## Contributing

1. Create a feature branch from `main`
2. Make your changes following the project's coding standards
3. Write tests for new functionality
4. Ensure all tests pass and code quality checks pass
5. Submit a pull request

## License

[Add license information here]

## Support

For issues, questions, or contributions, please [add support contact information].
