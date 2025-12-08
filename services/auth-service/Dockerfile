FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
RUN pip install fastapi uvicorn python-jose[cryptography] pydantic
EXPOSE 8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
