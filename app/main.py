from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings

app = FastAPI(  
    title=settings.PROJECT_NAME,
    description="API para processamento e automação de documentos e tarefas.",
    version=settings.VERSION,
)

app.include_router(api_router, prefix=settings.API_PREFIX)