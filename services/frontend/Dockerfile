FROM python:3.12-slim

WORKDIR /app

# Copiar el código del frontend
COPY services/frontend/app/ /app/

# Copiar las plantillas desde infra
COPY infra/frontend/app/templates/ /app/templates/

# Instalar dependencias necesarias
RUN pip install fastapi uvicorn jinja2 python-multipart requests requests-toolbelt httpx

EXPOSE 8080

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
