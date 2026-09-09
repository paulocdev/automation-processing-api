from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.core.exceptions import DomainException

client = TestClient(app)


def test_process_document_success():
    payload = {
        "filename": "relatorio_financeiro.pdf",
        "document_type": "pdf",
        "priority": 2,
    }
    response = client.post(f"{settings.API_PREFIX}/documents/process", json=payload)

    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "queued"
    assert "task_id" in data


def test_process_document_invalid_payload():
    payload = {
        "document_type": "pdf",
    }
    response = client.post(f"{settings.API_PREFIX}/documents/process", json=payload)

    assert response.status_code == 422

def test_process_unsupported_type():
    payload = {
        "filename": "planilha.xlsx",
        "document_type": "xlsx",
        "priority": 1
    }
    response = client.post("/api/documents/process", json=payload)

    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "InvalidDocumentTypeError"
    assert "não é suportado" in data["message"]