from fastapi import APIRouter, status
from app.schemas.document import DocumentProcessRequest, DocumentProcessResponse
from app.services.document_service import document_service

router = APIRouter()


@router.post(
    "/process",
    response_model=DocumentProcessResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Recebe e agenda o processamento de um documento",
)

def process_document(payload: DocumentProcessRequest):
    return document_service.process_document(payload)