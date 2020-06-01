"""Написать свой контекстный менеджер для работы с файлами"""

class MyContextManager:

    def __init__(self, name_file, mode):

        self.name_file = name_file
        self.mode = mode

    def __enter__(self):

        self.file = open(self.name_file, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with MyContextManager('file_1.txt', 'w') as file:
    file.write('Some text')

with MyContextManager('file_1.txt', 'r') as file:
    print(file.read())
