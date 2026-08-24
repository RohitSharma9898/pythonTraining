"""
FUNCTION AS AN ARGUMENT

Python allows us to pass a function
to another function.
"""


def add(a, b):

    return a + b


def multiply(a, b):

    return a * b


def calculate(function, a, b):

    return function(a, b)


# ==========================================
# PASS ADD FUNCTION
# ==========================================

result = calculate(add, 10, 20)

print("Addition:", result)


# ==========================================
# PASS MULTIPLY FUNCTION
# ==========================================

result = calculate(multiply, 10, 20)

print("Multiplication:", result)


# ==========================================
# PASS LAMBDA
# ==========================================

result = calculate(
    lambda a, b: a - b,
    20,
    10
)

print("Subtraction:", result)