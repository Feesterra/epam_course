#!/usr/bin/env python3.6
class SchoolMember:
    """Class represents any schoolmember."""

    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
        print("(Создан {}: {})".format(SchoolMember.__name__, self.name))


class Student(SchoolMember):
    """Class represents Student."""

    def __init__(self, name, age, number):
        super().__init__(name, age, number)
        print("(Создан {}: {})".format(Student.__name__, self.name))

    def show(self):
        """Prints formated object's parameters."""

        print("Имя: {} Возраст: {} Оценки: {}".format(self.name, self.age, self.number))


class Teacher(SchoolMember):
    """Class represents Teacher."""

    def __init__(self, name, age, number):
        super().__init__(name, age, number)
        print("(Создан {}: {})".format(Teacher.__name__, self.name))

    def show(self):
        """Prints formated object's parameters."""

        print("Имя: {} Возраст: {} Зарплата: {}".format(self.name, self.age, self.number))


if __name__ == '__main__':
    persons = [Teacher("Mr. Smith", 40, 3000), Student("Morty", 16, 75)]
    for person in persons:
        person.show()
