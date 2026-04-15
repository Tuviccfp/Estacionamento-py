import sqlite3
import os
from .models import cliente


def connect_db():
    db_path = os.path.join(os.path.dirname(__file__), "database.sqlite")
    conn = sqlite3.connect(db_path)
    print("Conexão estabelecida!")
    cliente.create_cliente_table(conn)
    return conn
