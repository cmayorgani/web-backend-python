FROM python:3.12-slim

WORKDIR /app
COPY app/ /app/

# Instalar dependencias mínimas
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    rm -rf /var/lib/apt/lists/*

# Instalar paquetes de Python necesarios
RUN pip install fastapi uvicorn jinja2 python-multipart requests

EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
