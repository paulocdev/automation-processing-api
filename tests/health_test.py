from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check_returns_correct_response():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_check_includes_process_time_header():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert "x-process-time" in response.headers