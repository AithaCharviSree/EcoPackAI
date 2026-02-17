import os
import psycopg2
from urllib.parse import urlparse

def get_db_connection():
    database_url = os.getenv("DATABASE_URL")
    result = urlparse(database_url)

    return psycopg2.connect(
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )
