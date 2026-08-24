"""
====================================================
             REAL-WORLD EXAMPLES
====================================================
"""


# ==================================================
# EXAMPLE 1: STUDENT MARKS
# ==================================================

marks = [35, 80, 90, 25, 70, 60]


# Add 5 grace marks

updated_marks = map(
    lambda mark: mark + 5,
    marks
)


print("Updated marks:")

print(list(updated_marks))


# ==================================================
# EXAMPLE 2: PASSING STUDENTS
# ==================================================

marks = [35, 80, 90, 25, 70, 60]


passing_students = filter(
    lambda mark: mark >= 40,
    marks
)


print("Passing marks:")

print(list(passing_students))


# ==================================================
# EXAMPLE 3: TOTAL SALES
# ==================================================

from functools import reduce


sales = [1000, 2500, 1500, 3000]


total_sales = reduce(
    lambda total, sale: total + sale,
    sales
)


print("Total sales:", total_sales)


# ==================================================
# EXAMPLE 4: STUDENT RANKING
# ==================================================

students = [

    ("Rohit", 85),

    ("Rahul", 92),

    ("Aman", 78),

    ("Priya", 95)
]


ranking = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)


print("Ranking:")

for student in ranking:

    print(student)