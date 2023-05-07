from sqlalchemy import create_engine,text
#from google.cloud.sql.connector import Connector
import os

db_connection_str = os.environ['DB_CONNECT_STR_DEV']

engine = create_engine(db_connection_str,connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}})


def update_db(content):
  with engine.connect() as conn:
    query = "insert into rawdata (rawjson) values (" + content + ")"
    result = conn.execute(text(query))
    return result
