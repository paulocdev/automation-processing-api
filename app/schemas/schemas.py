from pydantic import BaseModel
from app.core.config import settings
class HealthCheckResponse(BaseModel):
    status: str
    service: str
    version: str

class InfoResponse(BaseModel):
    project: str
    version: str
    status: str