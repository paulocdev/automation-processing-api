from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
    
client = TestClient(app)

def test_health_check():
    response = client.get(f"{settings.API_PREFIX}/health")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "automation-processing-api"
    assert "version" in data