"""
POSITIONAL ARGUMENTS

Arguments are passed according to their position.
"""


def student(name, age, course):

    print(name)
    print(age)
    print(course)


# ==========================================
# POSITIONAL ARGUMENTS
# ==========================================

student("Rohit", 21, "Python")


# Here:

# "Rohit" -> name
# 21       -> age
# "Python" -> course


# ==========================================
# ORDER MATTERS
# ==========================================

def divide(a, b):

    return a / b


print(divide(10, 2))

print(divide(2, 10))


# ==========================================
# TOO MANY ARGUMENTS
# ==========================================

# student("Rohit", 21, "Python", "India")

# This will cause TypeError.