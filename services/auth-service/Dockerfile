FROM python:3.12-slim

WORKDIR /app
COPY app/ /app/

# Instalar dependencias necesarias
RUN pip install fastapi uvicorn python-jose[cryptography] pydantic python-multipart

EXPOSE 8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload", "--app-dir", "/app"]
