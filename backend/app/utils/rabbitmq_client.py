"""RabbitMQ connection management with aio-pika."""

try:
    import aio_pika
    from aio_pika import Channel, Connection, connect_robust
except ImportError:
    # Handle case where aio-pika is not installed
    aio_pika = None
    Connection = None
    Channel = None
    connect_robust = None

import logging
from typing import Any

from app.config import get_settings

logger = logging.getLogger(__name__)

# Global connection and channel (lazy initialization)
rabbitmq_connection: Any | None = None
rabbitmq_channel: Any | None = None


async def get_rabbitmq_connection():
    """Get or create RabbitMQ connection."""
    global rabbitmq_connection

    if aio_pika is None:
        raise ImportError("aio-pika package is not installed. Install it with: uv add aio-pika")

    if rabbitmq_connection is None or rabbitmq_connection.is_closed:
        try:
            settings = get_settings()
            rabbitmq_connection = await connect_robust(
                settings.rabbitmq_url, client_properties={"connection_name": settings.app_name}
            )
            logger.info("RabbitMQ connection established")
        except Exception as e:
            logger.error(f"Failed to connect to RabbitMQ: {e}")
            raise

    return rabbitmq_connection


async def get_rabbitmq_channel():
    """Get or create RabbitMQ channel."""
    global rabbitmq_channel

    if aio_pika is None:
        raise ImportError("aio-pika package is not installed. Install it with: uv add aio-pika")

    if rabbitmq_channel is None or rabbitmq_channel.is_closed:
        connection = await get_rabbitmq_connection()
        rabbitmq_channel = await connection.channel()
        logger.info("RabbitMQ channel created")

    return rabbitmq_channel


async def close_rabbitmq_connection() -> None:
    """Close RabbitMQ connection and channel."""
    global rabbitmq_connection, rabbitmq_channel

    if rabbitmq_channel and not rabbitmq_channel.is_closed:
        await rabbitmq_channel.close()
        rabbitmq_channel = None
        logger.info("RabbitMQ channel closed")

    if rabbitmq_connection and not rabbitmq_connection.is_closed:
        await rabbitmq_connection.close()
        rabbitmq_connection = None
        logger.info("RabbitMQ connection closed")


# Connection will be established when actually used (lazy initialization)
