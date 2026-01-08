"""Example test to verify pytest setup and fixtures."""

import pytest
from fastapi import status


def test_example_basic():
    """Basic test to verify pytest is working."""
    assert 1 + 1 == 2


def test_test_client_fixture(client):
    """Test that the test client fixture works."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "message" in response.json()


@pytest.mark.asyncio
async def test_async_client_fixture(async_client):
    """Test that the async test client fixture works."""
    response = await async_client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert "message" in response.json()


def test_database_session_fixture(session):
    """Test that the database session fixture works."""
    assert session is not None
    # Verify session is usable with SQLModel
    from sqlalchemy import text

    result = session.execute(text("SELECT 1"))
    assert result.scalar() == 1


def test_mock_redis_fixture(mock_redis):
    """Test that the mock Redis fixture works."""
    assert mock_redis is not None
    # Mock should have expected methods
    assert hasattr(mock_redis, "ping")
    assert hasattr(mock_redis, "get")
    assert hasattr(mock_redis, "set")


def test_mock_rabbitmq_fixture(mock_rabbitmq):
    """Test that the mock RabbitMQ fixture works."""
    assert mock_rabbitmq is not None
    assert "connection" in mock_rabbitmq
    assert "channel" in mock_rabbitmq
    assert mock_rabbitmq["connection"] is not None
    assert mock_rabbitmq["channel"] is not None


def test_mock_supabase_fixture(mock_supabase):
    """Test that the mock Supabase fixture works."""
    assert mock_supabase is not None
    # Mock should have expected methods
    assert hasattr(mock_supabase, "table")
    assert hasattr(mock_supabase, "select")
    assert hasattr(mock_supabase, "insert")
