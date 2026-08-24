"""
====================================================
            BUILT-IN DECORATORS
====================================================

Python provides some decorators itself.

Common examples:

    @staticmethod
    @classmethod
    @property
"""


# ==================================================
# staticmethod
# ==================================================

class Calculator:


    @staticmethod
    def add(a, b):

        return a + b


print(Calculator.add(10, 20))


# ==================================================
# classmethod
# ==================================================

class Student:

    school = "ABC School"


    @classmethod
    def show_school(cls):

        print(cls.school)


Student.show_school()


# ==================================================
# property
# ==================================================

class Person:

    def __init__(self, name):

        self._name = name


    @property
    def name(self):

        return self._name


person = Person("Rohit")


print(person.name)