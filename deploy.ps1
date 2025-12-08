# deploy.ps1
# Script de despliegue automático para levantar todo el ecosistema en Docker Windows

Write-Host "=== Limpieza previa de contenedores e imágenes ==="
docker-compose down -v

# Opcional: eliminar imágenes construidas previamente para evitar duplicados
Write-Host "Eliminando imágenes previas..."
docker image prune -f
docker container prune -f
docker volume prune -f

Write-Host "=== Construyendo e iniciando servicios ==="
docker-compose up --build -d

Write-Host "=== Esperando inicialización de LocalStack y SQL Server ==="
Start-Sleep -Seconds 25

Write-Host "=== Estado de los contenedores ==="
docker ps

Write-Host "=== Información de acceso ==="
Write-Host "Frontend:   http://localhost:8080"
Write-Host "Auth API:   http://localhost:8001/docs"
Write-Host "Files API:  http://localhost:8002/docs"
Write-Host "Token API:  http://localhost:8003/docs"
Write-Host "LocalStack: http://localhost:4566"
Write-Host "SQL Server: localhost, puerto 1433 (usuario sa / YourStrong!Passw0rd)"

Write-Host "=== Despliegue completado ==="
