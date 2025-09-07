# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from src.api.main import app

@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_health(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    
    
#   test/chat.py
def test_chat_food_order(client):
    payload = {"session_id": "test-session", "message": "Order a pizza for room 120"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "pizza" in data["reply"].lower()

def test_chat_maintenance_request(client):
    payload = {"session_id": "test-session", "message": "The light is broken in room 305"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "maintenance" in data["reply"].lower() or "technician" in data["reply"].lower()

# tests/test_analytics.py

def test_get_summary(client):
    response = client.get("/analytics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_events" in data

#pytest -v
