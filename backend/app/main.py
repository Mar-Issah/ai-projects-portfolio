"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.config import get_settings
from app.middleware.error_handler import (
    api_exception_handler,
    general_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from app.utils.exceptions import APIException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup: Initialize LangSmith
    if settings.LANGCHAIN_TRACING_V2 and settings.LANGCHAIN_API_KEY:
        import os

        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = settings.LANGCHAIN_API_KEY
        os.environ["LANGCHAIN_PROJECT"] = settings.LANGCHAIN_PROJECT
        if settings.LANGCHAIN_ENDPOINT:
            os.environ["LANGCHAIN_ENDPOINT"] = settings.LANGCHAIN_ENDPOINT
        print(f"✅ LangSmith tracing enabled for project: {settings.LANGCHAIN_PROJECT}")

    yield
    # Shutdown: Cleanup if needed


def create_application() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Production-grade backend API for AI Projects Portfolio",
        debug=settings.DEBUG,
        lifespan=lifespan,
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Exception handlers
    app.add_exception_handler(APIException, api_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)

    # Include API routes
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    return app


app = create_application()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
