"""
====================================================
       STUDENT MARKS DATA PROCESSOR
====================================================

Imagine we have thousands of students.

Instead of loading every student's marks
into memory at once, we can process them
one by one using a generator.
"""


students = [
    ("Rohit", 85),
    ("Rahul", 72),
    ("Aman", 91),
    ("Priya", 65),
    ("Neha", 88)
]


def passing_students(students):

    for name, marks in students:

        if marks >= 40:

            yield name, marks


print("Passing Students:")


for student in passing_students(students):

    print(student)