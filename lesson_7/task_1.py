import sqlite3

"""
Написать контекстный менеджер для работы с SQLite DB.
"""


class BaseManager:

    def __init__(self, base_name):

        self._base_name = base_name
        self._conect = None
        self._cursor = None

    def __enter__(self):
        self._conect = sqlite3.connect(self._base_name)
        self._cursor = self._conect.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conect.close()


with BaseManager('students.db') as base:
    res = base.execute("SELECT * FROM students")
    print(res.fetchall())
