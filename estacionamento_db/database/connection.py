import sqlite3
import time


def connect_db():
    time.sleep(3)  # Simulate connection delay
    sqlite3.connect("database.db")
    return print("Conexão estabelecida!")
