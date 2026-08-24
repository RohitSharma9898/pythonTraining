"""
EXCEPT AS

We can store the exception object
in a variable using "as".
"""


try:

    number = 10 / 0

except ZeroDivisionError as error:

    print("Error:", error)


# ==========================================
# ANOTHER EXAMPLE
# ==========================================

try:

    number = int("hello")

except ValueError as error:

    print("Error:", error)