import uuid
from fastapi import APIRouter, status
from app.schemas.document import DocumentProcessRequest, DocumentProcessResponse

router = APIRouter()


@documents_router.post(
    "/process",
    response_model=DocumentProcessResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Recebe e agenda o processamento de um documento",
)
def process_document(payload: DocumentProcessRequest):
    task_id = str(uuid.uuid4())

    return DocumentProcessResponse(
        task_id=task_id,
        status="queued",
        message=f"Documento '{payload.filename}' recebido para processamento do tipo '{payload.document_type}'.",
    )