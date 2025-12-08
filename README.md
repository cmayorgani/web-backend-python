# Descripción del Proyecto

Este proyecto es un **aplicativo web en Python con FastAPI**, desplegado en contenedores Docker sobre Windows, que simula un entorno AWS completo usando **LocalStack** y una base de datos **SQL Server**.  

## Componentes principales
- **Frontend (FastAPI + Jinja2)**  
  Pantallas de login y subida de documentos CSV. Lista los archivos subidos y permite borrarlos. Usa JWT para autenticación.

- **Backend dividido en tres microservicios (FastAPI)**  
  1. **Auth Service**: inicio de sesión anónimo, genera JWT con rol y expiración de 15 minutos.  
  2. **Files Service**: subida de CSV con parámetros adicionales, validación de datos, almacenamiento en S3 simulado y persistencia en SQL Server. Lista y elimina archivos.  
  3. **Token Service**: renovación de JWT si aún no ha expirado.

- **Infraestructura simulada con LocalStack**  
  - **S3**: buckets para frontend y archivos.  
  - **API Gateway**: enruta `/auth`, `/files`, `/token` hacia los microservicios.  
  - **Lambda**: simulado para desplegar el frontend.  

- **SQL Server en contenedor**  
  - Tablas `UploadedFiles` y `CsvRows`.  
  - Scripts de inicialización (`init-db.sql` y `init-test.sql`) para crear estructura y datos de prueba.  
  - `entrypoint.sh` asegura que los scripts se ejecuten al arrancar.

## Características técnicas
- Drivers ODBC instalados en el contenedor de `files-service` para conexión real con SQL Server.  
- Archivos `__init__.py` en cada carpeta `app/` para que los módulos sean importables.  
- `requirements.txt` en cada servicio para reproducibilidad de dependencias.  
- Tests unitarios e integrados con Pytest, incluyendo fixtures (`conftest.py`) y pruebas de conexión a SQL Server.  
- Script de despliegue `deploy.ps1` que limpia imágenes/volúmenes, reconstruye todo y muestra URLs de acceso.  

---

# Estructura del Proyecto

fastapi-aws-sim/
├─ docker-compose.yml
├─ deploy.ps1
├─ README.md
├─ localstack/
│  ├─ init/
│  │  ├─ create-resources.sh
│  │  ├─ lambda_deploy.sh
│  │  ├─ apigw_config.json
│  │  └─ s3_setup.json
├─ infra/
│  ├─ sqlserver/
│  │  ├─ init-db.sql
│  │  ├─ init-test.sql
│  │  ├─ entrypoint.sh
│  │  └─ Dockerfile
│  └─ frontend/
│     ├─ Dockerfile
│     ├─ app/
│     │  ├─ __init__.py
│     │  ├─ server.py
│     │  ├─ config.py
│     │  ├─ templates/
│     │  │  ├─ login.html
│     │  │  └─ upload.html
│     │  └─ static/
│     │     └─ styles.css
├─ services/
│  ├─ auth-service/
│  │  ├─ Dockerfile
│  │  ├─ requirements.txt
│  │  ├─ app/
│  │  │  ├─ __init__.py
│  │  │  ├─ main.py
│  │  │  ├─ models.py
│  │  │  ├─ schemas.py
│  │  │  ├─ security.py
│  │  │  ├─ config.py
│  │  │  └─ tests/
│  │  │     ├─ conftest.py
│  │  │     └─ test_auth.py
│  ├─ files-service/
│  │  ├─ Dockerfile
│  │  ├─ requirements.txt
│  │  ├─ app/
│  │  │  ├─ __init__.py
│  │  │  ├─ main.py
│  │  │  ├─ storage.py
│  │  │  ├─ s3_client.py
│  │  │  ├─ db.py
│  │  │  ├─ validation.py
│  │  │  ├─ schemas.py
│  │  │  ├─ security.py
│  │  │  └─ tests/
│  │  │     ├─ conftest.py
│  │  │     ├─ test_files.py
│  │  │     └─ test_db.py
│  └─ token-service/
│     ├─ Dockerfile
│     ├─ requirements.txt
│     ├─ app/
│     │  ├─ __init__.py
│     │  ├─ main.py
│     │  ├─ security.py
│     │  ├─ schemas.py
│     │  ├─ config.py
│     │  └─ tests/
│     │     ├─ conftest.py
│     │     └─ test_token.py
