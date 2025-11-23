"""RAG (Retrieval-Augmented Generation) service."""

from typing import Optional

from fastapi import Depends

from app.models.schemas import RAGQueryRequest, RAGQueryResponse
from app.services.openai_service import OpenAIService, get_openai_service


class RAGService:
    """Service for RAG operations."""

    def __init__(self, openai_service: OpenAIService):
        """Initialize RAG service."""
        self.openai_service = openai_service
        # TODO: Initialize vector store (e.g., Chroma, Pinecone, Weaviate)
        self.documents: list[dict] = []

    def add_document(self, text: str, metadata: Optional[dict] = None) -> str:
        """Add document to the knowledge base."""
        doc_id = f"doc_{len(self.documents)}"
        self.documents.append(
            {
                "id": doc_id,
                "text": text,
                "metadata": metadata or {},
            }
        )
        logger.info(f"Added document: {doc_id}")
        return doc_id

    def query(self, request: RAGQueryRequest) -> RAGQueryResponse:
        """Process RAG query."""
        # TODO: Implement proper vector search
        # For now, simple keyword matching
        query = request.query.lower()
        relevant_docs = [doc for doc in self.documents if query in doc["text"].lower()][
            : request.top_k
        ]

        # Build context from retrieved documents
        context = "\n\n".join([doc["text"] for doc in relevant_docs])

        # Generate answer using OpenAI
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based on the provided context. If the context doesn't contain enough information, say so.",
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {request.query}\n\nAnswer:",
            },
        ]

        answer = self.openai_service.chat_completion(messages)

        return RAGQueryResponse(
            answer=answer,
            sources=[
                {"text": doc["text"], "metadata": doc["metadata"]}
                for doc in relevant_docs
            ],
            conversation_id=request.conversation_id,
        )


def get_rag_service(
    openai_service: OpenAIService = Depends(get_openai_service),
) -> RAGService:
    """Get RAG service instance."""
    return RAGService(openai_service)
