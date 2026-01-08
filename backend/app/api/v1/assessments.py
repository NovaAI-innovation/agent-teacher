"""Assessment-specific API routes."""

from fastapi import APIRouter

router = APIRouter(
    prefix="/assessments",
    tags=["assessments"],
)

# Placeholder routes will be implemented in future stories
# Example structure:
# @router.post("/{assessment_id}/submit")
# async def submit_assessment():
#     pass
