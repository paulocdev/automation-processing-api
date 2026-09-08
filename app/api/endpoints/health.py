from fastapi import APIRouter
from app.schemas.schemas import HealthCheckResponse

health_router = APIRouter()

@health_router.get("/health", response_model=HealthCheckResponse)
def health_check():
    return HealthCheckResponse(
        status="ok",
        service="automation-processing-api",
        version="0.1.0",
    )