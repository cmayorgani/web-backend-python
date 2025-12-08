from fastapi import FastAPI, HTTPException
from .schemas import TokenRenewRequest, TokenResponse
from .security import renew_token
from .config import JWT_EXP_MIN

app = FastAPI(title="Token Service")

@app.post("/token/renew", response_model=TokenResponse)
def renew(req: TokenRenewRequest):
    try:
        new_token = renew_token(req.token)
    except ValueError as e:
        if str(e) == "expired":
            raise HTTPException(status_code=400, detail="Token expirado")
        raise HTTPException(status_code=400, detail="Token inválido")
    return TokenResponse(access_token=new_token, expires_in=JWT_EXP_MIN)
