from fastapi import APIRouter
from app.api.endpoints import health, documents

api_router = APIRouter()
api_router.include_router(health.router, tags=["Saúde da API"])
api_router.include_router(documents.router, prefix="/documents", tags=["Processar documentos"])
