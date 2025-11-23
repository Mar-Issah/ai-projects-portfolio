"""OpenAI service for API interactions."""

from typing import Optional

from openai import OpenAI
from openai.types import ImagesResponse

from app.config import get_settings
from app.utils.exceptions import OpenAIException

settings = get_settings()


class OpenAIService:
    """Service for interacting with OpenAI API."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize OpenAI client."""
        self.api_key = api_key or settings.OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        self.client = OpenAI(api_key=self.api_key)
        self.default_model = settings.OPENAI_MODEL
        self.embedding_model = settings.OPENAI_EMBEDDING_MODEL

    def chat_completion(
        self,
        messages: list[dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> str:
        """Generate chat completion."""
        try:
            response = self.client.chat.completions.create(
                model=model or self.default_model,
                messages=messages,
                temperature=temperature,
                **kwargs,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            raise OpenAIException(f"Failed to generate completion: {str(e)}")

    def generate_embeddings(
        self, texts: list[str], model: Optional[str] = None
    ) -> list[list[float]]:
        """Generate embeddings for texts."""
        try:
            model = model or self.embedding_model
            response = self.client.embeddings.create(
                model=model,
                input=texts,
            )
            return [item.embedding for item in response.data]
        except Exception as e:
            print(f"OpenAI embedding error: {str(e)}")
            raise OpenAIException(f"Failed to generate embeddings: {str(e)}")

    def generate_image(
        self,
        prompt: str,
        size: str = "1024x1024",
        quality: str = "standard",
        n: int = 1,
        **kwargs,
    ) -> ImagesResponse:
        """Generate image from text prompt."""
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                quality=quality,
                n=n,
                **kwargs,
            )
            return response
        except Exception as e:
            print(f"OpenAI image generation error: {str(e)}")
            raise OpenAIException(f"Failed to generate image: {str(e)}")


def get_openai_service() -> OpenAIService:
    """Get OpenAI service instance."""
    return OpenAIService()
