"""Supabase client wrapper for knowledge base operations."""

from supabase import Client, create_client

from app.config import get_settings

# Initialize Supabase client (lazy initialization)
# This client is used for Supabase REST API operations (not direct PostgreSQL)
supabase_client: Client | None = None


def get_supabase_client() -> Client:
    """Get or create Supabase client instance."""
    global supabase_client

    if supabase_client is None:
        settings = get_settings()
        supabase_client = create_client(settings.supabase_url, settings.supabase_key)

    return supabase_client


def get_supabase_service_client() -> Client:
    """Get Supabase client with service role key (for admin operations)."""
    settings = get_settings()
    return create_client(settings.supabase_url, settings.supabase_service_key)
