import sqlite3

"""
Создать базу данных студентов. У студента есть факультет,
группа, оценки, номер студенческого билета. Написать программу,
с двумя ролями: Администратор, Пользователь. Администратор
может добавлять, изменять существующих студентов.
Пользователь может получать список отличников, список всех
студентов, искать студентов по по номеру студенческого, получать
полную информацию о конкретном студенте (включая оценки,
факультет)

"""


class Student:

    @classmethod
    def all_students(cls):

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        res = cursor.execute("""
                                SELECT first_name, last_name, faculty.name FROM students
                                INNER JOIN faculty on students.faculty = faculty.id
                            
                            """)
        result = res.fetchall()
        conn.close()
        return result

    @classmethod
    def find_student(cls, ticket):

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        res = cursor.execute("""
                                SELECT student_ticket, first_name, last_name, faculty.name FROM students
                                INNER JOIN faculty on students.faculty = faculty.id
                                WHERE student_ticket = ?
                            
                            """, [ticket])
        result = res.fetchall()
        conn.close()
        return result

    @classmethod
    def get_info(cls, name, surname):

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        res = cursor.execute(f"""
                                SELECT student_ticket, first_name, last_name, faculty.name,
                                subj.math, subj.physics, subj.history, subj.chemistry, subj.literature,
                                subj.average_rating  FROM students
                                INNER JOIN subj on students.subj_grades = subj.id
                                INNER JOIN faculty on students.faculty = faculty.id
                                WHERE first_name = ? and last_name = ?
                            """, [name, surname])

        result = res.fetchall()
        conn.close()
        return result

    @classmethod
    def best_stud(cls):

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        res = cursor.execute("""
                                SELECT student_ticket, first_name, last_name, faculty.name,
                                subj.math, subj.physics, subj.history, subj.chemistry, subj.literature,
                                subj.average_rating  FROM students
                                INNER JOIN subj on students.subj_grades = subj.id
                                INNER JOIN faculty on students.faculty = faculty.id
                                WHERE average_rating >= 4
                            """)

        result = res.fetchall()
        conn.close()
        return result


class Admin:

    @classmethod
    def add_student(cls, name, surname, faculty, grades):

        conn = sqlite3.connect('students.db')
        cursore = conn.cursor()
        res = cursore.execute("INSERT INTO students ('first_name', 'last_name', 'faculty', 'subj_grades')"
                              "VALUES (?, ?, ?, ?)",
                              [name, surname, faculty, grades])
        res.fetchall()
        conn.commit()
        conn.close()

    @classmethod
    def update_student(cls, id_ticket, faculty):

        conn = sqlite3.connect('students.db')
        cursore = conn.cursor()
        cursore.execute(f"""
                        UPDATE students
                        SET faculty = ?
                        WHERE student_ticket = ?
                        """, [faculty, id_ticket])
        conn.commit()
        conn.close()


student = Student()
admin = Admin()



