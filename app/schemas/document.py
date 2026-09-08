from pydantic import BaseModel, Field


class DocumentProcessRequest(BaseModel):
    filename: str = Field(
        ...,
        description="Nome do arquivo a processar",
        json_schema_extra={"example": "contrato1.pdf"},
    )
    document_type: str = Field(
        ...,
        description="Tipo do documento (ex: pdf, ocr, report)",
        json_schema_extra={"example": "pdf"},
    )
    priority: int = Field(default=1, ge=1, le=5, description="Prioridade de processamento (1 a 5)")


class DocumentProcessResponse(BaseModel):
    task_id: str
    status: str
    message: str
