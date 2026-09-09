from fastapi import APIRouter, BackgroundTasks, status
from app.schemas.document import DocumentProcessRequest, DocumentProcessResponse
from app.services.document_service import document_service

router = APIRouter()


@router.post(
    "/process",
    response_model=DocumentProcessResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Recebe e agenda o processamento de um documento",
)

def process_document(
    payload: DocumentProcessRequest,
    background_tasks: BackgroundTasks,
):
    response = document_service.process_document(payload)

    ### Agenda a execução em segundo plano ###
    background_tasks.add_task(
        document_service.execute_background_processing,
        task_id=response.task_id,
        filename=payload.filename,
    )

    return response