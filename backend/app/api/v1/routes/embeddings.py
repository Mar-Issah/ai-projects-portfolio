"""Embeddings API routes."""

import numpy as np
from fastapi import APIRouter, Depends, HTTPException, status

from app.models.schemas import (
    EmbeddingRequest,
    EmbeddingResponse,
    Message,
    SimilarityRequest,
    SimilarityResponse,
)
from app.services.openai_service import OpenAIService, get_openai_service

router = APIRouter(prefix="/embeddings", tags=["Embeddings"])


@router.post("/generate", response_model=EmbeddingResponse)
async def generate_embeddings(
    request: EmbeddingRequest,
    openai_service: OpenAIService = Depends(get_openai_service),
) -> EmbeddingResponse:
    """Generate embeddings for text(s)."""
    try:
        texts = [request.text] if isinstance(request.text, str) else request.text
        if not texts:
            raise ValueError("At least one text is required")

        embeddings = openai_service.generate_embeddings(texts, model=request.model)
        model = request.model or openai_service.embedding_model
        dimensions = len(embeddings[0]) if embeddings else 0

        return EmbeddingResponse(
            embeddings=embeddings,
            model=model,
            dimensions=dimensions,
        )
    except Exception as e:
        print(f"Embedding generation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate embeddings: {str(e)}",
        )


@router.post("/similarity", response_model=SimilarityResponse)
async def find_similar(
    request: SimilarityRequest,
    openai_service: OpenAIService = Depends(get_openai_service),
) -> SimilarityResponse:
    """Find similar texts using cosine similarity."""
    try:
        if not request.texts:
            raise ValueError("At least one text is required")

        # Generate embeddings
        all_texts = [request.query] + request.texts
        embeddings = openai_service.generate_embeddings(all_texts)
        query_embedding = np.array(embeddings[0])
        text_embeddings = np.array(embeddings[1:])

        # Calculate cosine similarity
        query_norm = np.linalg.norm(query_embedding)
        text_norms = np.linalg.norm(text_embeddings, axis=1)
        similarities = np.dot(text_embeddings, query_embedding) / (
            text_norms * query_norm
        )

        # Get top k results
        top_indices = np.argsort(similarities)[::-1][: request.top_k]
        results = [
            {
                "text": request.texts[idx],
                "similarity": float(similarities[idx]),
                "index": int(idx),
            }
            for idx in top_indices
        ]

        return SimilarityResponse(results=results)
    except Exception as e:
        print(f"Similarity search error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to find similar texts: {str(e)}",
        )


@router.get("/health", response_model=Message)
async def embeddings_health() -> Message:
    """Health check for embeddings service."""
    return Message(message="Embeddings service is healthy")
