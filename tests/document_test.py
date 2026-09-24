import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_process_document_success():
    # Cria um arquivo PDF simulado em memória
    file_data = io.BytesIO(b"conteudo do pdf de teste")
    files = {"file": ("relatorio.pdf", file_data, "application/pdf")}
    data = {"priority": 1}

    response = client.post("/api/documents/process", files=files, data=data)

    assert response.status_code == 202
    json_data = response.json()
    assert json_data["status"] == "queued"
    assert "relatorio.pdf" in json_data["message"]


def test_process_unsupported_type():
    file_data = io.BytesIO(b"conteudo de planilha")
    files = {"file": ("planilha.xlsx", file_data, "application/vnd.ms-excel")}
    data = {"priority": 1}

    response = client.post("/api/documents/process", files=files, data=data)

    assert response.status_code == 400
    json_data = response.json()
    assert json_data["error"] == "InvalidDocumentTypeError"
    assert "não é suportado" in json_data["message"]