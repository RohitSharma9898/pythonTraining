"""
DEFAULT ARGUMENTS

A default argument already has a value.

If the user does not provide a value,
the default value is used.
"""


# ==========================================
# BASIC EXAMPLE
# ==========================================

def greet(name="Student"):

    print("Hello", name)


greet("Rohit")

greet()


# ==========================================
# DEFAULT AGE
# ==========================================

def student(name, age=18):

    print("Name:", name)
    print("Age:", age)


student("Rohit", 21)

student("Rahul")


# ==========================================
# MULTIPLE DEFAULT VALUES
# ==========================================

def introduce(name, course="Python", city="Vadodara"):

    print("Name:", name)
    print("Course:", course)
    print("City:", city)


introduce("Rohit")

introduce("Rahul", "Java")

introduce("Aman", "Python", "Delhi")


# ==========================================
# IMPORTANT
# ==========================================

# Non-default argument should come
# before default argument.

# Correct:

def example(name, age=18):
    print(name, age)


# Incorrect:

# def example(age=18, name):
#     print(name, age)