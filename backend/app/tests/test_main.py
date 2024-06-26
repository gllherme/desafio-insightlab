from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}
