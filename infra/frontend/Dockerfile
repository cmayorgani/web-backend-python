FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
RUN pip install fastapi uvicorn jinja2 httpx python-multipart
EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
