"""
Módulo principal da aplicação FastAPI.

Responsável por inicializar a aplicação, configurar middlewares, incluir rotas e expor endpoints básicos.
"""

from fastapi import FastAPI
from app.config.settings import Settings
from app.routers.search import router as search_router
from app.routers.openai import router as openai_router
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def get_settings():
    """
    Instancia e retorna as configurações da aplicação.
    """
    return Settings()


def create_application():
    """
    Cria e configura a aplicação FastAPI, incluindo middlewares e rotas.
    """
    # Initialize settings
    settings = get_settings()

    # Create FastAPI app
    app = FastAPI(
        title=settings.api_title,
        description=settings.api_description,
        version=settings.api_version,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ],  # Frontend local
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add routers
    app.include_router(search_router)
    app.include_router(openai_router)

    @app.get("/")
    async def root():
        """
        Endpoint raiz. Retorna mensagem de boas-vindas.
        """
        return {"message": "Welcome to RAG API"}

    @app.get("/health")
    async def health_check():
        """
        Endpoint de verificação de saúde da API.
        """
        logging.info("Health endpoint was called")
        return {"status": "Ok"}

    return app


app = create_application()
