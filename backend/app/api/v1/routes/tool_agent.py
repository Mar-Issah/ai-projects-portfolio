"""Tool-Using Agent API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.models.schemas import Message, ToolAgentRequest, ToolAgentResponse
from app.services.openai_service import OpenAIService, get_openai_service

router = APIRouter(prefix="/tool-agent", tags=["Tool Agent"])


@router.post("/execute", response_model=ToolAgentResponse)
async def execute_tool_agent(
    request: ToolAgentRequest,
    openai_service: OpenAIService = Depends(get_openai_service),
) -> ToolAgentResponse:
    """Execute a tool-using agent."""
    try:
        # TODO: Implement proper tool calling with function calling API
        # For now, simulate tool usage
        system_message = (
            "You are a tool-using AI agent. You can use various tools to accomplish tasks. "
            "When you need to use a tool, explain which tool you would use and why."
        )

        if request.tools:
            system_message += f"\n\nAvailable tools: {', '.join([t.get('name', 'unknown') for t in request.tools])}"

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": request.query},
        ]

        result = openai_service.chat_completion(
            messages,
            temperature=0.7,
        )

        # TODO: Implement actual tool calling and tracking
        tool_calls = [
            {
                "tool": "example_tool",
                "input": {"query": request.query},
                "output": "Tool executed successfully",
            }
        ]

        return ToolAgentResponse(
            result=result,
            tool_calls=tool_calls,
            reasoning="Agent analyzed the query and executed appropriate tools",
        )
    except Exception as e:
        print(f"Tool agent error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to execute tool agent: {str(e)}",
        )


@router.get("/health", response_model=Message)
async def tool_agent_health() -> Message:
    """Health check for tool agent service."""
    return Message(message="Tool agent service is healthy")
