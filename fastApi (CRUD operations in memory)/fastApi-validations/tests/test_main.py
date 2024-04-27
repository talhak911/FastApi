from fastapi.testclient import TestClient
from fastapi_validations.main import app

def test_1():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message":"return from home page"}