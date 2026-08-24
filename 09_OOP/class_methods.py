"""
CLASS METHOD

A class method works with the class itself.

It uses cls as the first parameter.

Decorator:

@classmethod
"""


class Student:

    college = "LTSU"

    @classmethod
    def change_college(cls, new_college):

        cls.college = new_college


print(Student.college)

Student.change_college("IIT Delhi")

print(Student.college)