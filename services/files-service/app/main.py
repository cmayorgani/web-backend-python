from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
import csv
from io import StringIO
from .security import require_auth
from .storage import upload_to_s3, delete_from_s3, list_s3
from .db import insert_file, insert_rows
from .validation import validate_rows
from .schemas import UploadResponse, FileInfo

app = FastAPI(title="Files Service")

@app.get("/files/list")
def list_files(payload=Depends(require_auth)):
    items = list_s3()
    return [FileInfo(**i) for i in items]

@app.delete("/files/delete")
def delete_file(filename: str, payload=Depends(require_auth)):
    delete_from_s3(filename)
    return {"deleted": filename}

@app.post("/files/upload", response_model=UploadResponse)
async def upload_csv(
    file: UploadFile = File(...),
    param_a: str = Form(...),
    param_b: str = Form(...),
    payload=Depends(require_auth)
):
    content = await file.read()
    try:
        decoded = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Archivo debe ser UTF-8")
    reader = csv.DictReader(StringIO(decoded))
    rows = []
    for r in reader:
        rows.append({
            "Col1": r.get("Col1"),
            "Col2": r.get("Col2"),
            "Col3": r.get("Col3"),
        })

    validations = validate_rows(rows)

    # Guardar en S3
    upload_to_s3(file.filename, content, file.content_type or "text/csv")

    # Guardar en SQL Server
    file_id = insert_file(file.filename, param_a, param_b)
    insert_rows(file_id, rows)

    return UploadResponse(file_name=file.filename, s3_bucket="files-bucket", validations=validations)
