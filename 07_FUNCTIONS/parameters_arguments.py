"""
PARAMETERS AND ARGUMENTS

Parameter:
    Variable written inside the function definition.

Argument:
    Actual value passed to the function.
"""


# ==========================================
# PARAMETERS
# ==========================================

def greet(name):
    print("Hello", name)


# "name" is a parameter.

greet("Rohit")

# "Rohit" is an argument.


# ==========================================
# MULTIPLE PARAMETERS
# ==========================================

def student_details(name, age, course):

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_details("Rohit", 21, "Python")


# ==========================================
# DIFFERENT ARGUMENTS
# ==========================================

def add(a, b):
    print(a + b)


add(10, 20)

add(100, 200)


# ==========================================
# ARGUMENT TYPES
# ==========================================

def introduce(name, age):
    print(name, age)


# Positional arguments

introduce("Rohit", 21)


# Keyword arguments

introduce(name="Rohit", age=21)