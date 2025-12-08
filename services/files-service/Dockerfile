FROM python:3.12-slim

WORKDIR /app
COPY app/ /app/

RUN apt-get update && \
    apt-get install -y gcc g++ unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install fastapi uvicorn boto3 python-jose[cryptography] pydantic python-multipart pyodbc

EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
