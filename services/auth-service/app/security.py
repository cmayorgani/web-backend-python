from datetime import datetime, timedelta, timezone
from jose import jwt
from .config import JWT_SECRET, JWT_ALG, JWT_EXP_MIN

def create_token(user_id: str, role: str):
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=JWT_EXP_MIN)
    payload = {
        "sub": user_id,
        "role": role,
        "exp": int(exp.timestamp()),
        "iat": int(now.timestamp())
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
    return token, exp
