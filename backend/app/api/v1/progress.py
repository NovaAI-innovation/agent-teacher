"""Progress tracking API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/progress",
    tags=["progress"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.get("/courses/{course_id}")
# async def get_course_progress():
#     pass
