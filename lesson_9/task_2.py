import random
from lesson_9 import base_manager as cb
import json

"""
2) Создать модуль, который будет заполнять базу данных
случайными валидными значениями (минимум 100 студентов).
"""

base = 'students_info.db'

with open('russian_surnames.json', encoding='utf-8-sig') as f:
    surnames = json.load(f)

list_surname = []
for surname in surnames:
    list_surname.append(surname['Surname'])

with open('russian_names.json', encoding='utf-8-sig') as f:
    names = json.load(f)

list_names = []
for name in names:
    list_names.append(name['Name'])

subjects_list = ['Math', 'History', 'Physics', 'Geography', 'English', 'Literature']
groups_list = ['pm-52', 'st-52', 'tk-51', 'tk-52', 'rt-42']


sql = 'INSERT INTO students (first_name, last_name, surname, group_name, faculty_id, curator_id)' \
      'VALUES (?, ?, ?, ?, ?, ?)'


with cb.BaseManager(base, 'w') as bm:

    for i in range(1, 101):
        bm.execute(sql, [random.choice(list_names), random.choice(list_names), random.choice(list_surname),
                         random.choice(groups_list), random.randint(1, 7), random.randint(1, 5)])
        bm.fetchall()

sql = 'INSERT INTO subjects_rating (subject, id_students, rating)' \
      'VALUES (?, ?, ?)'

with cb.BaseManager(base, 'w') as bm:
    for i in range(1, 101):
        bm.execute(sql, [random.choice(subjects_list), random.randint(1, 100), random.randint(1, 5)])
        bm.fetchall()
