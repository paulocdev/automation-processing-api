from fastapi import APIRouter
from app.schemas.schemas import HealthCheckResponse
from app.core.config import Settings

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthCheckResponse,
    summary="Verifica o status operacional da aplicação",
)
def health_check():
    return HealthCheckResponse(
        status="ok",
        service="automation-processing-api",
        version="0.1.0",
    )