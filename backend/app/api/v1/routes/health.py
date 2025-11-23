"""Health check routes."""

from fastapi import APIRouter

from app.models.schemas import Message

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=Message)
async def health_check() -> Message:
    """Health check endpoint."""
    return Message(message="API is healthy")


@router.get("/", response_model=Message)
async def root() -> Message:
    """Root endpoint."""
    return Message(message="AI Projects Portfolio API")

