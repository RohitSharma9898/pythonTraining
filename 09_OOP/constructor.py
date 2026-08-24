"""
CONSTRUCTOR

__init__() is called automatically when
an object is created.

It is commonly used to initialize data.
"""


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show_details(self):

        print("Name:", self.name)
        print("Age:", self.age)


# ==========================================
# CREATE OBJECT
# ==========================================

student1 = Student("Rohit", 21)

student1.show_details()


student2 = Student("Rahul", 22)

student2.show_details()