import uuid
from app.core.exceptions import InvalidDocumentTypeError
from app.schemas.document import DocumentProcessRequest, DocumentProcessResponse

ALLOWED_TYPES = {"pdf", "ocr", "docx"}

class DocumentService:
    def process_document(self, payload: DocumentProcessRequest) -> DocumentProcessResponse:
        # Aqui no futuro entrará a integração com filas, banco de dados e pipelines de OCR
        document_type = payload.document_type.lower()

        if document_type not in ALLOWED_TYPES:
            raise InvalidDocumentTypeError(
                f"Tipo de documento '{payload.document_type}' não é suportado, tipos de arquivo suportados:'{', '.join(ALLOWED_TYPES)}.")
        
        task_id = str(uuid.uuid4())

        return DocumentProcessResponse(
            task_id=task_id,
            status="queued",
            message=f"Documento '{payload.filename}' recebido para processamento do tipo '{payload.document_type}'.",
        )


document_service = DocumentService()