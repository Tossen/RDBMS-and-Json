#read json file into dataframe
import pandas as pd
import numpy as np
import json
import os
from glob import glob
import urllib
import sqlalchemy as sa
# import pyodbc
files_path = "C:/Users/Tossen Macs/Downloads/data-assignment/visitors"
files = glob(os.path.join(files_path,"*.json"))
files.sort()
files
df1 = pd.concat((pd.read_json(file, lines = True) for file in files), ignore_index = True)
# df1.tail(5)



connection_string = (
    'Driver={ODBC Driver 11 for SQL Server};'
    'SERVER=TMACS-ENGINE\SA;'
    'Database=EKEDB;'
    'UID=username;'
    'PWD=Password$;'
    'Trusted_Connection=no;'
)
connection_uri = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
engine = sa.create_engine(connection_uri, fast_executemany=True)

# Deleting existing data in SQL Table:-
#with engine.begin() as conn:
#    conn.execute(sa.text("DELETE FROM datbase.schema.TableName"))
df1.to_sql("Visitor", engine, schema="dbo", if_exists="append", index=False)