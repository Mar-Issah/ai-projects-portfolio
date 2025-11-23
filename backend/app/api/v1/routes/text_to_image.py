"""Text-to-Image API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.models.schemas import Message, TextToImageRequest, TextToImageResponse
from app.services.openai_service import OpenAIService, get_openai_service

router = APIRouter(prefix="/text-to-image", tags=["Text-to-Image"])


@router.post("/generate", response_model=TextToImageResponse)
async def generate_image(
    request: TextToImageRequest,
    openai_service: OpenAIService = Depends(get_openai_service),
) -> TextToImageResponse:
    """Generate image from text prompt."""
    try:
        response = openai_service.generate_image(
            prompt=request.prompt,
            size=request.size,
            quality=request.quality,
            n=request.n,
        )

        image_urls = [item.url for item in response.data]
        revised_prompt = response.data[0].revised_prompt if response.data else None

        return TextToImageResponse(
            image_urls=image_urls,
            revised_prompt=revised_prompt,
        )
    except Exception as e:
        print(f"Image generation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate image: {str(e)}",
        )


@router.get("/health", response_model=Message)
async def text_to_image_health() -> Message:
    """Health check for text-to-image service."""
    return Message(message="Text-to-image service is healthy")
