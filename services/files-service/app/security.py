import os
from fastapi import HTTPException, Header
from jose import jwt

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
REQUIRED_ROLE = os.getenv("REQUIRED_ROLE", "uploader")

def require_auth(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
    if payload.get("role") != REQUIRED_ROLE:
        raise HTTPException(status_code=403, detail="Insufficient role")
    return payload
