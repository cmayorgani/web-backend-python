# web-backend-python
fullstack creado con python y simulado en aws con dockers windows

Estructura del proyecto

fastapi-aws-sim/
├─ docker-compose.yml
├─ deploy.ps1
├─ README.md
├─ .env
├─ nginx-apigw/
│  ├─ Dockerfile
│  └─ nginx.conf
├─ localstack/
│  ├─ Dockerfile
│  └─ init-scripts/
│     ├─ 01-create-buckets.sh
│     ├─ 02-upload-frontend.sh
│     └─ 03-apigw-routes.sh
├─ sqlserver/
│  ├─ Dockerfile
│  └─ init/
│     └─ init.sql
├─ web-frontend/
│  ├─ Dockerfile
│  ├─ index.html
│  ├─ login.js
│  ├─ upload.js
│  └─ styles.css
├─ auth-service/
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ app/
│     ├─ main.py
│     ├─ config.py
│     └─ security.py
├─ upload-service/
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ app/
│     ├─ main.py
│     ├─ config.py
│     ├─ deps.py
│     ├─ s3_client.py
│     ├─ db.py
│     └─ validators.py
├─ token-service/
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ app/
│     ├─ main.py
│     ├─ config.py
│     └─ security.py


Descripción general (para técnicos y no técnicos)
Este sistema simula un entorno AWS en tu máquina:

LocalStack imita S3, API Gateway y Lambda.

Tres microservicios en FastAPI:

Auth: login anónimo y emisión de JWT (expira a los 15 minutos).

Files: subida y validación de CSV con dos parámetros, guarda en S3 simulado y en SQL Server; lista y elimina archivos.

Token: renovación de JWT si aún no expiró.

Frontend simple con dos pantallas: login y subir documento, usando el JWT para autenticarse.

SQL Server almacena los datos procesados del CSV.

API Gateway (LocalStack) enruta: /auth, /files, /token hacia los microservicios. Lambda simulado despliega el frontend.

Un script de despliegue elimina imágenes previamente creadas para evitar duplicados e inicializa todo.