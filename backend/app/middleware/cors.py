"""CORS middleware configuration."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings


def setup_cors(app: FastAPI) -> None:
    """Configure CORS middleware for FastAPI app."""
    try:
        settings = get_settings()
        frontend_urls = settings.frontend_urls
    except Exception:
        # Fallback to default if settings can't be loaded
        frontend_urls = ["http://localhost:3000", "http://localhost:3001"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=frontend_urls,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
