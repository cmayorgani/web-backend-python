from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(
    title="Auth Service",
    description="Servicio de autenticación",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint de login.
    Retorna un token de acceso si las credenciales son correctas.
    """
    # Ejemplo simple: usuario fijo
    if form_data.username == "admin" and form_data.password == "admin":
        return {"access_token": "fake-jwt-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")

@app.get("/auth/me")
async def read_users_me():
    """
    Endpoint de prueba para obtener información del usuario autenticado.
    """
    return {"username": "admin", "roles": ["user"]}
