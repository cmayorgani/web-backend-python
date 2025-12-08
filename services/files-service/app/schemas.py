from pydantic import BaseModel
from typing import List, Optional

class FileInfo(BaseModel):
    file_name: str
    uploaded_at: str

class ValidationResult(BaseModel):
    rule: str
    status: str
    detail: Optional[str] = None

class UploadResponse(BaseModel):
    file_name: str
    s3_bucket: str
    validations: List[ValidationResult]
