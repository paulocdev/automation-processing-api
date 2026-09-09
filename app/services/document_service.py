import time
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

    def execute_background_processing(self, task_id: str, filename: str) -> None:
        """Simula a execução pesada de OCR/Parsing em segundo plano."""
        print(f"[BACKGROUND TASK] Iniciando processamento do arquivo '{filename}' (ID: {task_id})...")
        time.sleep(2)
        print(f"[BACKGROUND TASK] Processamento do arquivo '{filename}' (ID: {task_id}) concluído com sucesso.")

document_service = DocumentService()