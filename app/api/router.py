from fastapi import APIRouter
from app.api.endpoints.health import health_router
from app.api.endpoints.documents import documents_router 

api_router = APIRouter()
api_router.include_router(health_router, tags=["Saúde da API"])
api_router.include_router(documents_router, prefix="/documents", tags=["Processar documentos"])
