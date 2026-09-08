from fastapi import APIRouter
from app.api.endpoints.health import health_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["Saúde da API"])