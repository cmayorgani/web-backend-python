# Detener todos los contenedores en ejecución
docker stop $(docker ps -aq)

# Eliminar todos los contenedores
docker rm -f $(docker ps -aq)

# Eliminar todas las imágenes
docker rmi -f $(docker images -aq)

# Eliminar todos los volúmenes
docker volume rm $(docker volume ls -q)

# Eliminar todas las redes personalizadas (excepto las default: bridge, host, none)
docker network rm $(docker network ls -q | Where-Object {$_ -notin @("bridge","host","none")})

# Limpiar caché y espacio
docker system prune -a --volumes -f
