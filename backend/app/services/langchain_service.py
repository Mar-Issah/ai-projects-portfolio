"""LangChain service with LangSmith tracing."""

from typing import Optional

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage

from app.config import get_settings
from app.utils.exceptions import OpenAIException

settings = get_settings()


class LangChainService:
    """Service for LangChain operations with LangSmith tracing."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize LangChain service."""
        self.api_key = api_key or settings.OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("OpenAI API key is required")

        # Initialize LangChain models (these will automatically trace to LangSmith)
        self.llm = ChatOpenAI(
            model=settings.OPENAI_MODEL,
            api_key=self.api_key,
            temperature=0.7,
        )
        self.embeddings = OpenAIEmbeddings(
            model=settings.OPENAI_EMBEDDING_MODEL,
            openai_api_key=self.api_key,
        )

    def chat_completion(
        self,
        messages: list[dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs,
    ) -> str:
        """Generate chat completion with LangSmith tracing."""
        try:
            # Convert dict messages to LangChain messages
            langchain_messages = []
            for msg in messages:
                if msg["role"] == "system":
                    langchain_messages.append(SystemMessage(content=msg["content"]))
                else:
                    langchain_messages.append(HumanMessage(content=msg["content"]))

            # Use LangChain model (automatically traced)
            if model and model != settings.OPENAI_MODEL:
                llm = ChatOpenAI(
                    model=model,
                    api_key=self.api_key,
                    temperature=temperature,
                )
            else:
                llm = self.llm
                if temperature != 0.7:
                    llm = ChatOpenAI(
                        model=settings.OPENAI_MODEL,
                        api_key=self.api_key,
                        temperature=temperature,
                    )

            response = llm.invoke(langchain_messages)
            return response.content
        except Exception as e:
            raise OpenAIException(f"Failed to generate completion: {str(e)}")

    def generate_embeddings(
        self, texts: list[str], model: Optional[str] = None
    ) -> list[list[float]]:
        """Generate embeddings with LangSmith tracing."""
        try:
            if model and model != settings.OPENAI_EMBEDDING_MODEL:
                embeddings = OpenAIEmbeddings(
                    model=model,
                    openai_api_key=self.api_key,
                )
            else:
                embeddings = self.embeddings

            return embeddings.embed_documents(texts)
        except Exception as e:
            raise OpenAIException(f"Failed to generate embeddings: {str(e)}")


def get_langchain_service() -> LangChainService:
    """Get LangChain service instance."""
    return LangChainService()
