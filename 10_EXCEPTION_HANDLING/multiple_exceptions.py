"""
MULTIPLE EXCEPTIONS

A program can have different types
of errors.

We can handle them separately.
"""


try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print(result)

except ValueError:

    print("Please enter a valid number")

except ZeroDivisionError:

    print("Number cannot be zero")