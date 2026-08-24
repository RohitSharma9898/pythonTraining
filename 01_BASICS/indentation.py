"""
Indentation in Python

Python uses indentation (spaces) to define blocks of code.

Usually, 4 spaces are recommended.
"""


age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote.")


# Another example

number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative number")


# Nested indentation

age = 20
has_id = True

if age >= 18:
    print("Age is valid.")

    if has_id:
        print("ID is available.")
    else:
        print("ID is not available.")


# Incorrect indentation would cause an IndentationError.
# Example:
#
# if age >= 18:
# print("Adult")
#
# Correct:
#
# if age >= 18:
#     print("Adult")