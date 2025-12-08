from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI(
    title="Files Service",
    description="Servicio de gestión de archivos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/files/list")
async def list_files():
    """
    Devuelve la lista de archivos disponibles.
    Por ahora es un ejemplo fijo.
    """
    return ["file1.txt", "file2.txt"]

@app.post("/files/upload")
async def upload_file(
    file: UploadFile = File(...),
    param_a: str = Form(...),
    param_b: str = Form(...)
):
    """
    Sube un archivo junto con parámetros adicionales.
    """
    return {
        "filename": file.filename,
        "param_a": param_a,
        "param_b": param_b
    }

@app.delete("/files/delete")
async def delete_file(filename: str):
    """
    Elimina un archivo por nombre.
    """
    return {"deleted": filename}
