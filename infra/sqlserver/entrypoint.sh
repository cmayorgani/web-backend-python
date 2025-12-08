#!/bin/bash
/opt/mssql/bin/sqlservr &

# Esperar a que SQL Server esté listo
sleep 30

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P YourStrong!Passw0rd -d master -i /init-db.sql
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P YourStrong!Passw0rd -d master -i /init-test.sql

wait
