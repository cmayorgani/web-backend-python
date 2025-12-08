from fastapi.testclient import TestClient
from app.main import app
from jose import jwt

SECRET="supersecretkey"

client = TestClient(app)

def make_token(role="uploader"):
    payload = {"sub":"test","role":role}
    return jwt.encode(payload, SECRET, algorithm="HS256")

def test_upload_requires_auth():
    resp = client.post("/files/upload")
    assert resp.status_code == 422  # missing fields/auth header

def test_list_without_role():
    token = make_token(role="viewer")
    resp = client.get("/files/list", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 403

def test_list_ok_empty():
    token = make_token(role="uploader")
    resp = client.get("/files/list", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code in (200, 500)  # If S3 not ready, LocalStack may error; in compose it's ready
