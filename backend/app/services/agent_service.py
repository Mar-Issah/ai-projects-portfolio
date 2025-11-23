"""Agent service for autonomous task execution."""

from typing import Optional

from fastapi import Depends

from app.models.schemas import AgentTaskRequest, AgentTaskResponse
from app.services.openai_service import OpenAIService, get_openai_service


class AgentService:
    """Service for agent operations."""

    def __init__(self, openai_service: OpenAIService):
        """Initialize agent service."""
        self.openai_service = openai_service

    def execute_task(self, request: AgentTaskRequest) -> AgentTaskResponse:
        """Execute agent task."""
        # TODO: Implement proper agent orchestration with tools and reasoning
        # For now, simple task execution
        messages = [
            {
                "role": "system",
                "content": "You are an autonomous AI agent. Break down tasks into steps and execute them systematically. Provide clear reasoning for your actions.",
            },
            {
                "role": "user",
                "content": f"Task: {request.task}\n\nContext: {request.context}\n\nExecute this task step by step.",
            },
        ]

        result = self.openai_service.chat_completion(
            messages,
            temperature=0.7,
        )

        # TODO: Implement proper step tracking
        steps = [
            {
                "step": 1,
                "action": "Task analysis",
                "result": "Task understood",
            },
            {
                "step": 2,
                "action": "Execution",
                "result": result[:100] + "..." if len(result) > 100 else result,
            },
        ]

        return AgentTaskResponse(
            result=result,
            steps=steps,
            task_id=None,  # TODO: Generate unique task ID
        )


def get_agent_service(
    openai_service: OpenAIService = Depends(get_openai_service),
) -> AgentService:
    """Get agent service instance."""
    return AgentService(openai_service)
