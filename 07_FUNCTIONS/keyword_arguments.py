"""
KEYWORD ARGUMENTS

We provide arguments using parameter names.

Syntax:

function(parameter=value)
"""


def student_details(name, age, course):

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


# ==========================================
# KEYWORD ARGUMENTS
# ==========================================

student_details(
    name="Rohit",
    age=21,
    course="Python"
)


# ==========================================
# ORDER DOES NOT MATTER
# ==========================================

student_details(
    course="Python",
    name="Rohit",
    age=21
)


# ==========================================
# MIXING POSITIONAL AND KEYWORD
# ==========================================

student_details(
    "Rohit",
    age=21,
    course="Python"
)