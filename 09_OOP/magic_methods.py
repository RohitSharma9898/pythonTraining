"""
MAGIC METHODS

Magic methods have double underscores.

Examples:

__init__
__str__
__len__
"""


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"{self.name} - {self.age}"

    def __len__(self):

        return self.age


student = Student("Rohit", 21)


# __str__

print(student)


# __len__

print(len(student))