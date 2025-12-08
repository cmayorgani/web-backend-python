import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_header():
    # Token simulado con rol uploader
    from jose import jwt
    SECRET = "supersecretkey"
    token = jwt.encode({"sub": "test", "role": "uploader"}, SECRET, algorithm="HS256")
    return {"Authorization": f"Bearer {token}"}
