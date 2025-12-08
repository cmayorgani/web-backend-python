from datetime import datetime, timedelta, timezone
from jose import jwt, ExpiredSignatureError, JWTError
from .config import JWT_SECRET, JWT_ALG, JWT_EXP_MIN

def renew_token(old_token: str):
    try:
        payload = jwt.decode(old_token, JWT_SECRET, algorithms=[JWT_ALG], options={"verify_exp": True})
    except ExpiredSignatureError:
        raise ValueError("expired")
    except JWTError:
        raise ValueError("invalid")

    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=JWT_EXP_MIN)
    new_payload = {
        "sub": payload.get("sub"),
        "role": payload.get("role"),
        "exp": int(exp.timestamp()),
        "iat": int(now.timestamp())
    }
    token = jwt.encode(new_payload, JWT_SECRET, algorithm=JWT_ALG)
    return token
