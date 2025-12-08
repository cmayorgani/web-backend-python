from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_issues_jwt():
    resp = client.post("/auth/login", json={"username": "carlos", "password": "x"})
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["expires_in"] == 15
