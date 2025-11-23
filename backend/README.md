# AI Projects Portfolio - Backend API

Production-grade FastAPI backend for AI projects including RAG, Agents, Embeddings, Text-to-Image, and Tool-Using Agents.

## Features

- 🚀 **FastAPI** - Modern, fast web framework
- 🔒 **Production-ready** - Error handling, logging, CORS, validation
- 🤖 **OpenAI Integration** - GPT-4, embeddings, DALL-E
- 📚 **RAG Support** - Retrieval-augmented generation
- 🤖 **Agent Framework** - Autonomous task execution
- 🎨 **Text-to-Image** - DALL-E integration
- 🔧 **Tool Agents** - Function calling and tool usage
- 📊 **Embeddings** - Vector similarity search

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── dependencies.py      # Dependency injection
│   ├── api/
│   │   └── v1/
│   │       ├── api.py       # API router aggregation
│   │       └── routes/      # API route modules
│   ├── services/            # Business logic services
│   ├── models/              # Pydantic schemas
│   ├── middleware/          # Custom middleware
│   └── utils/               # Utility functions
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Setup

### Prerequisites

- Python 3.11+
- OpenAI API key

### Installation

1. **Clone and navigate to backend:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

5. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

   Or using Python:
   ```bash
   python -m app.main
   ```

## API Endpoints

### Health Check
- `GET /api/v1/health` - API health check

### RAG (Retrieval-Augmented Generation)
- `POST /api/v1/rag/query` - Query the RAG system
- `POST /api/v1/rag/documents` - Upload documents
- `GET /api/v1/rag/health` - RAG service health

### Agent
- `POST /api/v1/agent/task` - Execute agent task
- `GET /api/v1/agent/health` - Agent service health

### Embeddings
- `POST /api/v1/embeddings/generate` - Generate embeddings
- `POST /api/v1/embeddings/similarity` - Find similar texts
- `GET /api/v1/embeddings/health` - Embeddings service health

### Text-to-Image
- `POST /api/v1/text-to-image/generate` - Generate image from text
- `GET /api/v1/text-to-image/health` - Text-to-image service health

### Tool Agent
- `POST /api/v1/tool-agent/execute` - Execute tool-using agent
- `GET /api/v1/tool-agent/health` - Tool agent service health

## Docker

### Build and run with Docker:
```bash
docker-compose up --build
```

### Run with Dockerfile:
```bash
docker build -t ai-projects-backend .
docker run -p 8000:8000 --env-file .env ai-projects-backend
```

## Development

### Code Quality
```bash
# Format code
black app/

# Sort imports
isort app/

# Lint code
ruff check app/
```

### Testing
```bash
pytest
```

## Configuration

Environment variables (see `.env.example`):

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `OPENAI_MODEL` - Default model (default: gpt-4o)
- `OPENAI_EMBEDDING_MODEL` - Embedding model (default: text-embedding-3-small)
- `DEBUG` - Debug mode (default: false)
- `CORS_ORIGINS` - Allowed CORS origins
- `LOG_LEVEL` - Logging level (default: INFO)

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Production Deployment

1. Set `ENVIRONMENT=production` in `.env`
2. Set `DEBUG=false`
3. Configure proper `CORS_ORIGINS`
4. Set `SECRET_KEY` for security
5. Use a production ASGI server (e.g., Gunicorn with Uvicorn workers)

## License

MIT

