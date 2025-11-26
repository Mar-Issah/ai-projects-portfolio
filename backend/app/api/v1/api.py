"""API v1 router aggregation."""

from fastapi import APIRouter

from app.api.v1.routes import (agent, embeddings, health, rag, text_to_image,
                               tool_agent)

api_router = APIRouter()

# Include all route modules
api_router.include_router(health.router)
api_router.include_router(rag.router)
api_router.include_router(agent.router)
api_router.include_router(embeddings.router)
api_router.include_router(text_to_image.router)
api_router.include_router(tool_agent.router)
