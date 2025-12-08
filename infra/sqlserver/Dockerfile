FROM mcr.microsoft.com/mssql/server:2019-latest
USER root
COPY init-db.sql /init-db.sql
USER mssql
ENV MSSQL_PID=Express
# Entrypoint default inicia el server; usaremos sqlcmd en healthcheck para esperar.
