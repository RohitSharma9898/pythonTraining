"""
COMMON BUILT-IN EXCEPTIONS
"""


# ==========================================
# VALUE ERROR
# ==========================================

try:

    number = int("hello")

except ValueError:

    print("ValueError")


# ==========================================
# ZERO DIVISION ERROR
# ==========================================

try:

    result = 10 / 0

except ZeroDivisionError:

    print("ZeroDivisionError")


# ==========================================
# INDEX ERROR
# ==========================================

try:

    numbers = [10, 20, 30]

    print(numbers[10])

except IndexError:

    print("IndexError")


# ==========================================
# KEY ERROR
# ==========================================

try:

    student = {
        "name": "Rohit"
    }

    print(student["age"])

except KeyError:

    print("KeyError")


# ==========================================
# TYPE ERROR
# ==========================================

try:

    result = "10" + 5

except TypeError:

    print("TypeError")


# ==========================================
# NAME ERROR
# ==========================================

try:

    print(age)

except NameError:

    print("NameError")