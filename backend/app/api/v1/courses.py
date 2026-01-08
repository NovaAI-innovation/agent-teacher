"""Course management API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.get("/")
# async def list_courses():
#     pass
