import pyodbc
import os

def test_sqlserver_connection():
    HOST = os.getenv("SQLSERVER_HOST", "localhost")
    USER = os.getenv("SQLSERVER_USER", "sa")
    PWD = os.getenv("SQLSERVER_PASSWORD", "YourStrong!Passw0rd")
    DB  = os.getenv("SQLSERVER_DB", "FileDB")

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={HOST};DATABASE={DB};UID={USER};PWD={PWD}"
    cn = pyodbc.connect(conn_str)
    cur = cn.cursor()
    cur.execute("SELECT COUNT(*) FROM UploadedFiles")
    count = cur.fetchone()[0]
    assert isinstance(count, int)
    cn.close()
