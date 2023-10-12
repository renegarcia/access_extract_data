"""
export_access_to_csv.py - Creates a compressed dump of an MSAccess database tables.

USAGE

invoke from the same directory where `settings.toml` is located.

RETURNS

A comprezed zip file in the format '%Y-%m-%dT%H_%M_%S-database_name.zip'
"""
from datetime import datetime
from zipfile import ZipFile, ZIP_DEFLATED
from io import StringIO
import tomllib
import pyodbc
import csv


with open("settings.toml", "rb") as f:
    settings = tomllib.load(f)


now = datetime.now().strftime("%FT%H_%M_%S")
db_dsn = settings["database"]["dsn"]
tables = settings["database"]["export_tables"]
conn = pyodbc.connect(f"DSN={db_dsn}")
database_name = settings["database"]["name"].replace(" ", "_")
zipfile_name = f"{now}-{database_name}.zip"

with ZipFile(zipfile_name, mode="w", compression=ZIP_DEFLATED) as zipfile:
    for tablename in tables:
        cur = conn.cursor()
        dest = f"tables/{tablename}.csv"
        rows = cur.execute(f"SELECT * from {tablename}").fetchall()
        buffer = StringIO()
        writer = csv.writer(buffer, quoting=csv.QUOTE_NONNUMERIC, strict=True)
        header = [row[0] for row in cur.description]
        writer.writerow(header)
        writer.writerows(rows)
        zipfile.writestr(dest, buffer.getvalue())
