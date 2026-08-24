"""
====================================================
               sorted() WITH key
====================================================

We can tell sorted() HOW to sort
our data using the key parameter.
"""


students = [

    ("Rohit", 85),

    ("Rahul", 70),

    ("Aman", 95),

    ("Priya", 80)
]


# ==================================================
# SORT BY MARKS
# ==================================================

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)


print(students_sorted)


# ==================================================
# HIGHEST MARKS FIRST
# ==================================================

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)


print(students_sorted)