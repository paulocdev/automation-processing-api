import uuid
from fastapi import UploadFile
from app.core.exceptions import InvalidDocumentTypeError
from app.schemas.document import DocumentProcessResponse

ALLOWED_TYPES = {"pdf", "ocr", "docx"}


class DocumentService:
    async def process_document(self, file: UploadFile, priority: int) -> DocumentProcessResponse:
        filename = file.filename or "desconhecido"
        
        # Extrai a extensão do arquivo enviado
        ext = filename.split(".")[-1].lower() if "." in filename else ""

        if ext not in ALLOWED_TYPES:
            raise InvalidDocumentTypeError(
                f"Tipo de documento '.{ext}' não é suportado. Tipos permitidos: {', '.join(ALLOWED_TYPES)}"
            )

        task_id = str(uuid.uuid4())

        return DocumentProcessResponse(
            task_id=task_id,
            status="queued",
            message=f"Arquivo '{filename}' ({file.content_type}) recebido para processamento assíncrono.",
        )

    def execute_background_processing(self, task_id: str, filename: str) -> None:
        print(f"[BACKGROUND TASK] Processando arquivo '{filename}' (ID: {task_id})...")


document_service = DocumentService()