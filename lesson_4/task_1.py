import abc
from datetime import date


class AbstractPerson(abc.ABC):

    def __init__(self, name, surname, year, faculty):
        self._name = name
        self._surname = surname
        self._year = year
        self._faculty = faculty
        self._age = self.years_old()

    @abc.abstractmethod
    def full_name(self):
        return f'{self._name} {self._surname}'

    @abc.abstractmethod
    def years_old(self):
        return date.today().year - self._year

    @property
    def age(self):
        return self._age

    @abc.abstractmethod
    def show_info(self):
        return f'Person: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty}'


class Enroll(AbstractPerson):

    def full_name(self):
        return super().full_name()

    def years_old(self):
        return super().years_old()

    def show_info(self):
        return f'Enroll: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty}'

    # def __str__(self):
    #     return f'Enroll: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty}'


class Student(AbstractPerson):

    def __init__(self, name, surname, year, faculty, curs):
        super().__init__(name, surname, year, faculty)
        self._curs = curs

    def full_name(self):
        return super().full_name()

    def years_old(self):
        return super().years_old()

    def show_info(self):
        return f'Student: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty}, ' \
               f'\nCurs: {self._curs}'

    # def __str__(self):
    #     return f'Student: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty},
    #     \nCurs: {self._curs}'


class Teacher(AbstractPerson):

    def __init__(self, name, surname, year, faculty, position, experience):
        super().__init__(name, surname, year, faculty)
        self._position = position
        self._experience = experience

    def full_name(self):
        return super().full_name()

    def years_old(self):
        return super().years_old()

    def show_info(self):
        return f'Teacher: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty}, ' \
               f'\nPosition: {self._position}, \nExperience: {self._experience}'

    # def __str__(self):
    #     return f'Teacher: {self._name} {self._surname}, \nYears: {self._age}, \nFaculty: {self._faculty}, ' \
    #            f'\nPosition: {self._position}, \nExperience: {self._experience}'


enroll = Enroll('Max', 'Pupkin', 2000, 'TEV')
student = Student('Ksenia', 'Kravets', 1990, 'Economics', 4)
teacher = Teacher('Pasha', 'Turin', 1961, 'TEV', 'teacher', 10)

person_list = [enroll, student, teacher]

for person in person_list:
    print(person.show_info())

for person in person_list:
    if person.age < 30:
        print(person.show_info())
