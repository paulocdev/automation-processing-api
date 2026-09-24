from fastapi import APIRouter, BackgroundTasks, File, Form, UploadFile, status
from app.schemas.document import DocumentProcessResponse
from app.services.document_service import document_service

router = APIRouter()


@router.post(
    "/process",
    response_model=DocumentProcessResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Recebe e agenda o processamento de um documento real",
)
async def process_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    priority: int = Form(1),
):
    response = await document_service.process_document(file=file, priority=priority)

    background_tasks.add_task(
        document_service.execute_background_processing,
        task_id=response.task_id,
        filename=file.filename or "desconhecido",
    )

    return response