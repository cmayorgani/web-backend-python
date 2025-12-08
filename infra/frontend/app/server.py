from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_AUTH = "http://host.docker.internal:8001"
API_FILES = "http://host.docker.internal:8002"
API_TOKEN = "http://host.docker.internal:8003"

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{API_AUTH}/auth/login", json={"username": username, "password": password})
    if resp.status_code == 200:
        data = resp.json()
        response = RedirectResponse(url="/upload", status_code=303)
        response.set_cookie("token", data["access_token"], httponly=True)
        return response
    return RedirectResponse(url="/?error=1", status_code=303)

@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    token = request.cookies.get("token")
    if not token:
        return RedirectResponse(url="/", status_code=303)

    # Obtener lista de archivos
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_FILES}/files/list", headers={"Authorization": f"Bearer {token}"})
    files = resp.json() if resp.status_code == 200 else []
    return templates.TemplateResponse("upload.html", {"request": request, "files": files})

@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...), param_a: str = Form(...), param_b: str = Form(...)):
    token = request.cookies.get("token")
    if not token:
        return RedirectResponse(url="/", status_code=303)
    async with httpx.AsyncClient() as client:
        form = httpx.MultipartEncoder(fields={
            "file": (file.filename, await file.read(), file.content_type),
            "param_a": param_a,
            "param_b": param_b
        })
        headers = {"Authorization": f"Bearer {token}", "Content-Type": form.content_type}
        resp = await client.post(f"{API_FILES}/files/upload", content=form, headers=headers)
    return RedirectResponse(url="/upload", status_code=303)

@app.post("/delete")
async def delete_file(request: Request, filename: str = Form(...)):
    token = request.cookies.get("token")
    if not token:
        return RedirectResponse(url="/", status_code=303)
    async with httpx.AsyncClient() as client:
        resp = await client.delete(f"{API_FILES}/files/delete", params={"filename": filename}, headers={"Authorization": f"Bearer {token}"})
    return RedirectResponse(url="/upload", status_code=303)
