"""Pytest configuration and fixtures for backend tests."""

import os
from collections.abc import AsyncGenerator, Generator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.config import Settings, get_settings
from app.main import create_app

# Pytest configuration
pytest_plugins = ["pytest_asyncio"]


# ============================================================================
# Application Fixtures
# ============================================================================


@pytest.fixture(scope="session")
def test_settings() -> Settings:
    """Create test settings with overridden values."""
    # Use in-memory SQLite for tests unless overridden
    test_database_url = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")

    # Create test settings with minimal required values
    # Most values can be dummy/test values for unit tests
    return Settings(
        # Application
        app_name="agent-teacher-test",
        environment="test",
        debug=True,
        secret_key="test-secret-key-for-testing-only-not-for-production",
        algorithm="HS256",
        access_token_expire_minutes=1440,
        # Database - use test database URL
        supabase_url="https://test.supabase.co",
        supabase_key="test-key",
        supabase_service_key="test-service-key",
        database_url=test_database_url,
        # External services - use dummy values
        mem0_api_url="http://localhost:8001",
        mem0_api_key="test-mem0-key",
        openai_api_key="test-openai-key",
        anthropic_api_key="test-anthropic-key",
        gemini_api_key="test-gemini-key",
        prefect_api_url="http://localhost:4200/api",
        prefect_api_key="test-prefect-key",
        rabbitmq_url="amqp://guest:guest@localhost:5672/",
        redis_url="redis://localhost:6379/0",
        kong_admin_url="http://localhost:8001",
        kong_api_url="http://localhost:8000",
        frontend_urls=["http://localhost:3000"],
        brave_search_api_key="test-brave-key",
        youtube_api_key="test-youtube-key",
    )


@pytest.fixture(scope="session", autouse=True)
def override_settings(test_settings: Settings):
    """Override get_settings() to return test settings."""
    # Clear the cache
    get_settings.cache_clear()

    # Patch get_settings to return test settings
    with patch("app.config.get_settings", return_value=test_settings):
        yield test_settings

    # Clear cache after tests
    get_settings.cache_clear()


@pytest.fixture(scope="session")
def app(test_settings: Settings):
    """Create FastAPI application instance for testing."""
    with patch("app.config.get_settings", return_value=test_settings):
        app = create_app()
        # Set up middleware and routes (normally done in app.main module)
        from app.api.v1 import health
        from app.middleware import setup_middleware

        setup_middleware(app)
        app.include_router(health.router, prefix="/api/v1", tags=["health"])

        # Add root endpoint
        @app.get("/")
        async def root():
            """Root endpoint."""
            return {
                "message": "agent-teacher API",
                "version": "0.1.0",
                "docs": "/docs",
            }

        return app


# ============================================================================
# Test Client Fixtures
# ============================================================================


@pytest.fixture(scope="function")
def client(app) -> Generator[TestClient, None, None]:
    """Create a test client for FastAPI."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
async def async_client(app) -> AsyncGenerator[AsyncClient, None]:
    """Create an async test client for FastAPI."""
    from httpx import ASGITransport

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as async_test_client:
        yield async_test_client


# ============================================================================
# Database Fixtures
# ============================================================================


@pytest.fixture(scope="function")
def test_engine(test_settings: Settings):
    """Create a test database engine (in-memory SQLite)."""
    # Create in-memory SQLite database for testing
    database_url = test_settings.database_url or "sqlite:///:memory:"

    # Use StaticPool for in-memory SQLite to allow sharing across threads
    engine = create_engine(
        database_url,
        connect_args={"check_same_thread": False} if "sqlite" in database_url else {},
        poolclass=StaticPool if "sqlite" in database_url else None,
        echo=False,  # Set to True for SQL query debugging
    )

    # Create all tables
    SQLModel.metadata.create_all(engine)

    yield engine

    # Cleanup
    SQLModel.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope="function")
def session(test_engine) -> Generator[Session, None, None]:
    """Create a database session for testing."""
    with Session(test_engine) as session:
        yield session
        session.rollback()


@pytest.fixture(scope="function")
def db_session(session: Session) -> Generator[Session, None, None]:
    """Alias for session fixture - matches FastAPI dependency name."""
    yield session


# ============================================================================
# Mock Service Fixtures
# ============================================================================


@pytest.fixture(scope="function")
def mock_redis():
    """Create a mock Redis client."""
    mock_client = AsyncMock()
    mock_client.ping = AsyncMock(return_value=True)
    mock_client.get = AsyncMock(return_value=None)
    mock_client.set = AsyncMock(return_value=True)
    mock_client.delete = AsyncMock(return_value=1)
    mock_client.exists = AsyncMock(return_value=False)
    return mock_client


@pytest.fixture(scope="function")
def mock_rabbitmq():
    """Create a mock RabbitMQ connection and channel."""
    mock_connection = AsyncMock()
    mock_connection.is_closed = False
    mock_connection.close = AsyncMock()

    mock_channel = AsyncMock()
    mock_connection.channel = AsyncMock(return_value=mock_channel)
    mock_channel.basic_publish = AsyncMock()
    mock_channel.basic_consume = AsyncMock()
    mock_channel.close = AsyncMock()

    return {
        "connection": mock_connection,
        "channel": mock_channel,
    }


@pytest.fixture(scope="function")
def mock_supabase():
    """Create a mock Supabase client."""
    mock_client = MagicMock()
    mock_client.table = MagicMock(return_value=mock_client)
    mock_client.select = MagicMock(return_value=mock_client)
    mock_client.insert = MagicMock(return_value=mock_client)
    mock_client.update = MagicMock(return_value=mock_client)
    mock_client.delete = MagicMock(return_value=mock_client)
    mock_client.execute = MagicMock(return_value=MagicMock(data=[]))
    return mock_client


# ============================================================================
# Testcontainers Fixtures (for integration tests)
# ============================================================================


@pytest.fixture(scope="session")
def postgres_container():
    """Create a PostgreSQL container for integration tests."""
    try:
        from testcontainers.postgres import PostgresContainer

        postgres = PostgresContainer("postgres:15")
        postgres.start()
        yield postgres
        postgres.stop()
    except ImportError:
        pytest.skip("testcontainers not available - install with: uv add testcontainers --dev")
    except Exception as e:
        pytest.skip(f"Could not start PostgreSQL container: {e}")


@pytest.fixture(scope="session")
def redis_container():
    """Create a Redis container for integration tests."""
    try:
        from testcontainers.redis import RedisContainer

        redis = RedisContainer("redis:7")
        redis.start()
        yield redis
        redis.stop()
    except ImportError:
        pytest.skip("testcontainers not available - install with: uv add testcontainers --dev")
    except Exception as e:
        pytest.skip(f"Could not start Redis container: {e}")


@pytest.fixture(scope="session")
def rabbitmq_container():
    """Create a RabbitMQ container for integration tests."""
    try:
        from testcontainers.rabbitmq import RabbitMqContainer

        rabbitmq = RabbitMqContainer("rabbitmq:3-management")
        rabbitmq.start()
        yield rabbitmq
        rabbitmq.stop()
    except ImportError:
        pytest.skip("testcontainers not available - install with: uv add testcontainers --dev")
    except Exception as e:
        pytest.skip(f"Could not start RabbitMQ container: {e}")


# ============================================================================
# Integration Test Database Fixture
# ============================================================================


@pytest.fixture(scope="function")
def integration_db_session(postgres_container):
    """Create a database session using testcontainers PostgreSQL."""
    try:
        database_url = postgres_container.get_connection_url()

        engine = create_engine(
            database_url,
            echo=False,
            pool_pre_ping=True,
        )

        # Create all tables
        SQLModel.metadata.create_all(engine)

        with Session(engine) as session:
            yield session
            session.rollback()

        # Cleanup
        SQLModel.metadata.drop_all(engine)
        engine.dispose()
    except AttributeError:
        # Fallback if get_connection_url doesn't exist - use direct properties
        database_url = (
            f"postgresql+psycopg2://{postgres_container.username}:{postgres_container.password}@"
            f"{postgres_container.get_container_host_ip()}:"
            f"{postgres_container.get_exposed_port(5432)}/{postgres_container.dbname}"
        )

        engine = create_engine(
            database_url,
            echo=False,
            pool_pre_ping=True,
        )

        SQLModel.metadata.create_all(engine)

        with Session(engine) as session:
            yield session
            session.rollback()

        SQLModel.metadata.drop_all(engine)
        engine.dispose()
