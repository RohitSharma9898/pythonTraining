"""
====================================================
                CLASS DECORATOR
====================================================

A decorator can also modify a class.
"""


def add_message(cls):


    cls.message = "Hello from decorator!"


    return cls


@add_message
class Student:

    pass


student = Student()


print(student.message)