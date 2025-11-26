"""RAG API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.models.schemas import (DocumentUploadRequest, Message,
                                RAGQueryRequest, RAGQueryResponse)
from app.services.rag_service import RAGService, get_rag_service
from app.utils.exceptions import ValidationException

router = APIRouter(prefix="/rag", tags=["RAG"])


@router.post("/query", response_model=RAGQueryResponse)
async def query_rag(
    request: RAGQueryRequest,
    rag_service: RAGService = Depends(get_rag_service),
) -> RAGQueryResponse:
    """Query the RAG system."""
    try:
        return rag_service.query(request)
    except Exception as e:
        print(f"RAG query error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process query: {str(e)}",
        )


@router.post("/documents", response_model=Message)
async def upload_document(
    request: DocumentUploadRequest,
    rag_service: RAGService = Depends(get_rag_service),
) -> Message:
    """Upload a document to the knowledge base."""
    try:
        if not request.text.strip():
            raise ValidationException("Document text cannot be empty")
        doc_id = rag_service.add_document(request.text, request.metadata)
        return Message(message=f"Document uploaded successfully with ID: {doc_id}")
    except ValidationException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        print(f"Document upload error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to upload document: {str(e)}",
        )


@router.get("/health", response_model=Message)
async def rag_health() -> Message:
    """Health check for RAG service."""
    return Message(message="RAG service is healthy")
