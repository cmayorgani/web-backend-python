import os
import pyodbc

HOST = os.getenv("SQLSERVER_HOST", "localhost")
USER = os.getenv("SQLSERVER_USER", "sa")
PWD = os.getenv("SQLSERVER_PASSWORD", "YourStrong!Passw0rd")
DB  = os.getenv("SQLSERVER_DB", "FileDB")

conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={HOST};DATABASE={DB};UID={USER};PWD={PWD}"

def insert_file(file_name: str, a: str, b: str):
    with pyodbc.connect(conn_str) as cn:
        cur = cn.cursor()
        cur.execute("INSERT INTO UploadedFiles(FileName, ParamA, ParamB) VALUES (?, ?, ?)", (file_name, a, b))
        cn.commit()
        cur.execute("SELECT SCOPE_IDENTITY()")
        return int(cur.fetchone()[0])

def insert_rows(file_id: int, rows):
    with pyodbc.connect(conn_str) as cn:
        cur = cn.cursor()
        for i, row in enumerate(rows, start=1):
            cur.execute("INSERT INTO CsvRows(FileId, RowNumber, Col1, Col2, Col3) VALUES (?, ?, ?, ?, ?)",
                        (file_id, i, row.get("Col1"), row.get("Col2"), row.get("Col3")))
        cn.commit()
