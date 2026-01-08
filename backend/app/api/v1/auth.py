"""Authentication API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.post("/register")
# async def register():
#     pass
