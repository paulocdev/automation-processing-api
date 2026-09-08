from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str
    service: str
    version: str

class InfoResponse(BaseModel):
    project: str
    version: str
    status: str