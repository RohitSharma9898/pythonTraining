"""
TRY-EXCEPT

try:
    Contains code that may cause an exception.

except:
    Handles the exception.
"""


# ==========================================
# DIVISION
# ==========================================

try:

    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except:

    print("Something went wrong")


# ==========================================
# INVALID INPUT
# ==========================================

try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)

except:

    print("Please enter a valid number")


# ==========================================
# PROGRAM CONTINUES
# ==========================================

try:

    print(10 / 0)

except:

    print("Cannot divide by zero")


print("This line will execute.")