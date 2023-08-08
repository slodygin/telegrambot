from app.controls import sqlite


def create_tables():
    sqlite.execute("CREATE TABLE IF NOT EXISTS users (id VARCHAR(255), cur_status INTEGER);")
    sqlite.execute("CREATE TABLE IF NOT EXISTS schedule (description VARCHAR(255));")
