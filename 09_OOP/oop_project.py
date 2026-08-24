"""
STUDENT MANAGEMENT SYSTEM

Simple OOP Project
"""


class Student:

    def __init__(self, name, roll_no, marks):

        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):

        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def result(self):

        if self.marks >= 40:

            print("Result: Pass")

        else:

            print("Result: Fail")


# ==========================================
# CREATE STUDENTS
# ==========================================

student1 = Student("Rohit", 101, 90)

student2 = Student("Rahul", 102, 35)


# ==========================================
# DISPLAY
# ==========================================

student1.display()

student1.result()

print()

student2.display()

student2.result()