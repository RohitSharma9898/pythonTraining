"""
====================================================
          FUNCTIONS AS OBJECTS
====================================================

In Python, functions are objects.

This means we can:

    1. Store a function in a variable.
    2. Pass a function to another function.
    3. Return a function from another function.
"""


# ==================================================
# NORMAL FUNCTION
# ==================================================

def greet():

    print("Hello, Python!")


# Store the function in another variable

message = greet


# Call the function

message()


"""
IMPORTANT:

greet
    ↓
refers to the function

greet()
    ↓
calls the function
"""


# ==================================================
# FUNCTION IN A LIST
# ==================================================

def add():

    print("Addition")


def subtract():

    print("Subtraction")


operations = [add, subtract]


for operation in operations:

    operation()