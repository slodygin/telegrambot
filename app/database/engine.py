# todo: Database engine
import sqlite3
from contextlib import contextmanager
from typing import Any, LiteralString


class SQLite:
    def __init__(self, database: str):
        self.__database = database

    @contextmanager
    def connection(self, autocommit: bool = True):
        connection = sqlite3.connect(self.__database)
        try:
            yield connection
        finally:
            if autocommit:
                connection.commit()
            connection.close()

    @contextmanager
    def cursor(self, connection: sqlite3.Connection | None = None):
        _connection = sqlite3.connect(self.__database) if connection is None else connection
        cursor = _connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
            if connection is None:
                _connection.close()

    def fetchone(self, sql: LiteralString, values: tuple[Any, ...] | None = None) -> Any:
        with self.cursor() as cursor:
            cursor.execute(sql, values or ())
            return cursor.fetchone()

    def fetchall(self, sql: LiteralString, values: tuple[Any, ...] | None = None):
        with self.cursor() as cursor:
            cursor.execute(sql, values or ())
            return cursor.fetchall()

    def execute(self, sql: LiteralString, values: tuple[Any, ...] | None = None) -> int:
        with self.connection() as connection:
            with self.cursor(connection) as cursor:
                cursor.execute(sql, values or ())
                return cursor.rowcount
