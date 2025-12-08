from fastapi.testclient import TestClient
from app.main import app
from jose import jwt
SECRET="supersecretkey"

client = TestClient(app)

def test_renew_ok():
    old = jwt.encode({"sub":"carlos","role":"uploader"}, SECRET, algorithm="HS256")
    resp = client.post("/token/renew", json={"token": old})
    assert resp.status_code == 200
    assert "access_token" in resp.json()

def test_renew_invalid():
    resp = client.post("/token/renew", json={"token": "bad"})
    assert resp.status_code == 400
