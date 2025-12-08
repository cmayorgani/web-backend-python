# Imagen base oficial de SQL Server 2019 en Linux
FROM mcr.microsoft.com/mssql/server:2019-latest

USER root

# Instalar herramientas cliente de SQL Server (sqlcmd, bcp) y dependencias
RUN apt-get update && \
    apt-get install -y curl gnupg apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools unixodbc-dev && \
    rm -rf /var/lib/apt/lists/* microsoft.gpg

ENV PATH="$PATH:/opt/mssql-tools/bin"

USER mssql

# Copiar scripts y entrypoint
COPY init-db.sql /init-db.sql
COPY init-test.sql /init-test.sql
COPY entrypoint.sh /entrypoint.sh

# Cambiar permisos después de copiar
USER root
RUN chmod +x /entrypoint.sh
USER mssql

CMD ["/entrypoint.sh"]
