"""Agent API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.models.schemas import AgentTaskRequest, AgentTaskResponse, Message
from app.services.agent_service import AgentService, get_agent_service

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/task", response_model=AgentTaskResponse)
async def execute_task(
    request: AgentTaskRequest,
    agent_service: AgentService = Depends(get_agent_service),
) -> AgentTaskResponse:
    """Execute an agent task."""
    try:
        return agent_service.execute_task(request)
    except Exception as e:
        print(f"Agent task error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to execute task: {str(e)}",
        )


@router.get("/health", response_model=Message)
async def agent_health() -> Message:
    """Health check for agent service."""
    return Message(message="Agent service is healthy")
