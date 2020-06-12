import sqlite3


class BaseManager:
    def __init__(self, base_name, mode = "r"):
        self._base_name = base_name
        self.mode = mode
        self._connect = None
        self._cursor = None

    def __enter__(self):
        self._connect = sqlite3.connect(self._base_name)
        self._cursor = self._connect.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.mode == "w":
            self._connect.commit()
        self._connect.close()
