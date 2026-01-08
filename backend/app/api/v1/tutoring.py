"""Interactive tutoring API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/tutoring",
    tags=["tutoring"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.websocket("/session/{session_id}")
# async def tutoring_session():
#     pass
