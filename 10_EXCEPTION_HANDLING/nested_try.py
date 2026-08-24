"""
NESTED TRY

A try-except block can exist
inside another try-except block.
"""


try:

    number = int(input("Enter a number: "))

    try:

        result = 100 / number

        print(result)

    except ZeroDivisionError:

        print("Cannot divide by zero")

except ValueError:

    print("Please enter a valid number")