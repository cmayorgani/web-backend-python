from fastapi import FastAPI, HTTPException
from .schemas import LoginRequest, TokenResponse
from .security import create_token

app = FastAPI(title="Auth Service")

# Login anónimo: se acepta cualquier usuario/contraseña para la simulación
@app.post("/auth/login", response_model=TokenResponse)
def login(req: LoginRequest):
    # Rol fijo para pruebas; podrías mapear según usuario
    role = "uploader"
    token, exp = create_token(user_id=req.username or "anon", role=role)
    return TokenResponse(access_token=token, expires_in=15)
