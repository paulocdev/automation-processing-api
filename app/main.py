from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Automation Processing API",
    description="API para processamento e automação de documentos e tarefas.",
    version="0.1.0",
)

# Registra todas as rotas da versão 1 com o prefixo /api
app.include_router(api_router, prefix="/api")