"""Pydantic schemas for request/response models."""

from typing import Any, Optional

from pydantic import BaseModel, Field


# Common schemas
class Message(BaseModel):
    """Standard message response."""

    message: str


class ErrorResponse(BaseModel):
    """Error response schema."""

    error: str
    detail: Optional[str] = None


# RAG schemas
class RAGQueryRequest(BaseModel):
    """RAG query request."""

    query: str = Field(..., description="User query")
    conversation_id: Optional[str] = Field(
        None, description="Conversation ID for context"
    )
    top_k: int = Field(
        default=5, ge=1, le=20, description="Number of documents to retrieve"
    )


class RAGQueryResponse(BaseModel):
    """RAG query response."""

    answer: str = Field(..., description="Generated answer")
    sources: list[dict[str, Any]] = Field(
        default_factory=list, description="Source documents"
    )
    conversation_id: Optional[str] = Field(None, description="Conversation ID")


class DocumentUploadRequest(BaseModel):
    """Document upload request."""

    text: str = Field(..., description="Document text content")
    metadata: Optional[dict[str, Any]] = Field(
        default_factory=dict, description="Document metadata"
    )


# Agent schemas
class AgentTaskRequest(BaseModel):
    """Agent task request."""

    task: str = Field(..., description="Task description")
    context: Optional[dict[str, Any]] = Field(
        default_factory=dict, description="Additional context"
    )
    max_iterations: int = Field(
        default=10, ge=1, le=50, description="Maximum iterations"
    )


class AgentTaskResponse(BaseModel):
    """Agent task response."""

    result: str = Field(..., description="Task result")
    steps: list[dict[str, Any]] = Field(
        default_factory=list, description="Execution steps"
    )
    task_id: Optional[str] = Field(None, description="Task ID")


# Embeddings schemas
class EmbeddingRequest(BaseModel):
    """Embedding generation request."""

    text: str | list[str] = Field(..., description="Text or list of texts to embed")
    model: Optional[str] = Field(None, description="Embedding model to use")


class EmbeddingResponse(BaseModel):
    """Embedding response."""

    embeddings: list[list[float]] = Field(..., description="Generated embeddings")
    model: str = Field(..., description="Model used")
    dimensions: int = Field(..., description="Embedding dimensions")


class SimilarityRequest(BaseModel):
    """Similarity search request."""

    query: str = Field(..., description="Query text")
    texts: list[str] = Field(..., description="Texts to search in")
    top_k: int = Field(default=5, ge=1, le=20, description="Number of results")


class SimilarityResponse(BaseModel):
    """Similarity search response."""

    results: list[dict[str, Any]] = Field(
        ..., description="Similarity results with scores"
    )


# Text-to-Image schemas
class TextToImageRequest(BaseModel):
    """Text-to-image generation request."""

    prompt: str = Field(..., description="Image generation prompt")
    size: str = Field(default="1024x1024", description="Image size")
    quality: str = Field(default="standard", description="Image quality")
    style: Optional[str] = Field(None, description="Image style")
    n: int = Field(default=1, ge=1, le=4, description="Number of images")


class TextToImageResponse(BaseModel):
    """Text-to-image response."""

    image_urls: list[str] = Field(..., description="Generated image URLs")
    revised_prompt: Optional[str] = Field(None, description="Revised prompt used")


# Tool Agent schemas
class ToolAgentRequest(BaseModel):
    """Tool-using agent request."""

    query: str = Field(..., description="User query")
    tools: Optional[list[dict[str, Any]]] = Field(
        default_factory=list, description="Available tools"
    )
    max_iterations: int = Field(
        default=5, ge=1, le=20, description="Maximum tool calls"
    )


class ToolAgentResponse(BaseModel):
    """Tool-using agent response."""

    result: str = Field(..., description="Final result")
    tool_calls: list[dict[str, Any]] = Field(
        default_factory=list, description="Tool calls made"
    )
    reasoning: Optional[str] = Field(None, description="Agent reasoning")
