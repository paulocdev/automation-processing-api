from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import DomainException

app = FastAPI(  
    title=settings.PROJECT_NAME,
    description="API para processamento e automação de documentos e tarefas.",
    version=settings.VERSION,
)

@app.exception_handler(DomainException)
async def domain_exception_handler(Request: Request, exc: DomainException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": exc.__class__.__name__,
            "message": exc.message,
        },
    )

app.include_router(api_router, prefix=settings.API_PREFIX)