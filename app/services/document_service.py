import uuid
from app.schemas.document import DocumentProcessRequest, DocumentProcessResponse


class DocumentService:
    def process_document(self, payload: DocumentProcessRequest) -> DocumentProcessResponse:
        # Aqui no futuro entrará a integração com filas, banco de dados e pipelines de OCR
        task_id = str(uuid.uuid4())

        return DocumentProcessResponse(
            task_id=task_id,
            status="queued",
            message=f"Documento '{payload.filename}' recebido para processamento do tipo '{payload.document_type}'.",
        )


document_service = DocumentService()