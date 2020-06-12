from flask import Flask, request, jsonify
from lesson_9 import base_manager as cm

"""
1) Создать базу данных студентов (ФИО, группа, оценки, куратор студента, факультет).
Написать РЕСТ ко всем сущностям в бд (работа со студентами, оценками, кураторами, факультетами).
Создать отдельные контроллей, который будет выводить отличников по факультету.
"""

app = Flask(__name__)
base = 'students_info.db'


def get_all(sql):
    with cm.BaseManager(base) as bm:
        bm.execute(sql)
        result = bm.fetchall()
        key_dict = []
        for i in bm.description:
            key_dict.append(i[0])
        values_dict = []
        for j in result:
            values_dict.append(j)

    dict_base = {}
    for i in values_dict:
        dict_base[i[0]] = dict(zip(key_dict[1:], i[1:]))
    return dict_base


def get_id(sql, some_id):
    with cm.BaseManager(base) as bm:
        bm.execute(sql, [some_id])
        result = bm.fetchone()
        key_dict = []
        for i in bm.description:
            key_dict.append(i[0])
    dict_id = {}
    dict_id[result[0]] = dict(zip(key_dict[1:], result[1:]))
    return dict_id


def get_best(sql, some_id):
    with cm.BaseManager(base) as bm:
        bm.execute(sql, [some_id])
        result = bm.fetchall()
        key_dict = []
        for i in bm.description:
            key_dict.append(i[0])
        values_dict = []
        for j in result:
            values_dict.append(j)

    dict_base = {}
    for i in values_dict:
        dict_base[i[0]] = dict(zip(key_dict[1:], i[1:]))
    return dict_base


def add_some(sql, list_new):
    values_list = []
    for k, v in list_new.items():
        values_list.append(list_new[k])

    with cm.BaseManager(base, "w") as bm:
        bm.execute(sql, values_list)
        result = bm.fetchone()
    return result


def update_some(sql, some_id, update_list):
    values_list = []
    for k, v in update_list.items():
        values_list.append(update_list[k])
    values_list.append(some_id)

    with cm.BaseManager(base, "w") as bm:
        bm.execute(sql, values_list)
        result = bm.fetchone()
    return result


def delete_some(sql, some_id):
    with cm.BaseManager(base, "w") as bm:
        bm.execute(sql, [some_id])
        result = bm.fetchone()
    return result


sql_all_students = 'SELECT students.id, first_name, last_name, surname, group_name, faculty.faculty_name, curators.curator_name\
     FROM students \
    INNER JOIN faculty on students.faculty_id = faculty.id INNER JOIN curators on students.curator_id = curators.id'

sql_id_student = 'SELECT students.id, first_name, last_name, surname, group_name, faculty.faculty_name, curators.curator_name\
     FROM students \
        INNER JOIN faculty on students.faculty_id = faculty.id INNER JOIN curators on students.curator_id = curators.id\
        WHERE students.id = (?)'

sql_add_student = 'INSERT INTO students (first_name, last_name, surname, group_name, faculty_id, curator_id)' \
          'VALUES (?, ?, ?, ?, ?, ?)'

sql_upd_student = 'UPDATE students SET first_name = ?, last_name = ?, surname = ?, group_name = ?, faculty_id = ?, curator_id = ?' \
          'WHERE id = ?'

sql_del_student = 'DELETE FROM students WHERE id = ?'


@app.route('/students', methods=['GET', 'POST'])
@app.route('/students/<int:students_id>', methods=['GET', 'PUT', 'DELETE'])
def students(students_id=None):
    if request.method == 'GET':
        data = get_all(sql_all_students)
        if students_id:
            data = get_id(sql_id_student, students_id)
        return jsonify(data)

    elif request.method == 'POST':
        add_some(sql_add_student, request.json)
        return jsonify(request.json)

    elif request.method == 'PUT':
        update_some(sql_upd_student, students_id, request.json)
        return jsonify(request.json)

    elif request.method == 'DELETE':
        delete_some(sql_del_student, students_id)
        return get_all(sql_all_students)


sql_all_rating = 'SELECT subjects_rating.id, subject, rating, students.surname FROM subjects_rating' \
          ' INNER JOIN students on subjects_rating.id_students = students.id'

sql_id_rating = 'SELECT subjects_rating.id, subject, rating, students.surname FROM subjects_rating ' \
          'INNER JOIN students on subjects_rating.id_students = students.id ' \
          'WHERE subjects_rating.id = (?)'

sql_add_rating = 'INSERT INTO subjects_rating (subject, id_students, rating) VALUES (?, ?, ?)'

sql_upd_rating = 'UPDATE subjects_rating SET subject = ?, id_students = ?, rating = ? WHERE id = ?'

sql_del_rating = 'DELETE FROM subjects_rating WHERE id = ?'


@app.route('/ratings', methods=['GET', 'POST'])
@app.route('/ratings/<int:rating_id>', methods=['GET', 'PUT', 'DELETE'])
def rating(rating_id=None):
    if request.method == 'GET':
        data = get_all(sql_all_rating)
        if rating_id:
            data = get_id(sql_id_rating, rating_id)
        return jsonify(data)

    elif request.method == 'POST':
        add_some(sql_add_rating, request.json)
        return jsonify(request.json)

    elif request.method == 'PUT':
        update_some(sql_upd_rating, rating_id, request.json)
        return jsonify(request.json)
    #
    elif request.method == 'DELETE':
        delete_some(sql_del_rating, rating_id)
        return get_all(sql_all_rating)


sql_all_curators = 'SELECT curators.id, curator_name FROM curators'
sql_id_curator = 'SELECT id, curator_name FROM curators WHERE id = (?)'
sql_add_curator = 'INSERT INTO curators (name) VALUES = (?)'
sql_upd_curator = 'UPDATE curators SET curator_name = ? WHERE id = ?'
sql_del_curator = 'DELETE FROM curators WHERE id = ?'


@app.route('/curators', methods=['GET', 'POST'])
@app.route('/curators/<int:curator_id>', methods=['GET', 'PUT', 'DELETE'])
def curators(curator_id=None):
    if request.method == 'GET':
        data = get_all(sql_all_curators)
        if curator_id:
            data = get_id(sql_id_curator, curator_id)
        return jsonify(data)

    elif request.method == 'POST':
        add_some(sql_add_curator, request.json)
        return jsonify(request.json)

    elif request.method == 'PUT':
        update_some(sql_upd_curator, curator_id, request.json)
        return jsonify(request.json)

    elif request.method == 'DELETE':
        delete_some(sql_del_curator, curator_id)
        return get_all(sql_all_curators)


sql_all_faculty = 'SELECT id, faculty_name FROM faculty'
sql_id_faculty = 'SELECT id, faculty_name FROM faculty WHERE id = (?)'
sql_add_faculty = 'INSERT INTO faculty (faculty_name) VALUES = (?)'
sql_upd_faculty = 'UPDATE faculty SET faculty_name = ? WHERE id = ?'
sql_del_faculty = 'DELETE FROM faculty WHERE id = ?'


@app.route('/faculty', methods=['GET', 'POST'])
@app.route('/faculty/<int:faculty_id>', methods=['GET', 'PUT', 'DELETE'])
def faculty(faculty_id=None):
    if request.method == 'GET':
        data = get_all(sql_all_faculty)
        if faculty_id:
            data = get_id(sql_id_curator, faculty_id)
        return jsonify(data)

    elif request.method == 'POST':
        add_some(sql_add_faculty, request.json)
        return jsonify(request.json)

    elif request.method == 'PUT':
        update_some(sql_upd_faculty, faculty_id, request.json)
        return jsonify(request.json)

    elif request.method == 'DELETE':
        delete_some(sql_del_faculty, faculty_id)
        return get_all(sql_all_faculty)


sql_best_students = 'SELECT students.id, first_name, last_name, surname, group_name, faculty_name, subject, rating ' \
                    'FROM students INNER JOIN faculty on students.faculty_id = faculty.id ' \
                    'INNER JOIN subjects_rating on students.id = subjects_rating.id_students ' \
                    'WHERE rating = 5 and faculty.id = (?)'


@app.route('/best/<int:faculty_id>')
def best_students(faculty_id):
    data = get_best(sql_best_students, faculty_id)
    return jsonify(data)


app.run(debug=True, port=5000)
