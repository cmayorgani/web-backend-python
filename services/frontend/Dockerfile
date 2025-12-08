# Imagen base ligera de Python
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el código del frontend (cuando lo tengas)
COPY app/ /app/

# Instalar dependencias necesarias para un frontend en FastAPI
RUN pip install fastapi uvicorn jinja2 python-multipart requests

# Exponer el puerto donde correrá el frontend
EXPOSE 8080

# Comando de arranque: servidor FastAPI
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
