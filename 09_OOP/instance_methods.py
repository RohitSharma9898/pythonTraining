"""
INSTANCE METHODS

Methods that work with instance/object data.

They normally take self as the first parameter.
"""


class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def show_details(self):

        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):

        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")


student = Student("Rohit", 85)

student.show_details()

student.check_result()