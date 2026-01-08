"""Learning and assessment API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/learning",
    tags=["learning"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.get("/modules/{module_id}")
# async def get_module_content():
#     pass
