"""Platform administration API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.get("/metrics")
# async def get_platform_metrics():
#     pass
