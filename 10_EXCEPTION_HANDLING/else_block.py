"""
ELSE BLOCK

else executes only when
no exception occurs.

Structure:

try
except
else
"""


try:

    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:

    print("Invalid input")

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Division successful")

    print("Result:", result)