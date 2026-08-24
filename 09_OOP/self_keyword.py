"""
SELF KEYWORD

self refers to the current object.

It allows us to access variables and
methods belonging to that object.
"""


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show(self):

        print(self.name)
        print(self.age)


student1 = Student("Rohit", 21)

student1.show()


student2 = Student("Rahul", 22)

student2.show()