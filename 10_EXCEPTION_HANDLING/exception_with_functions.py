"""
EXCEPTION HANDLING WITH FUNCTIONS
"""


def divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        return "Cannot divide by zero"


print(divide(10, 2))

print(divide(10, 0))


# ==========================================
# INPUT VALIDATION
# ==========================================

def get_number():

    try:

        number = int(input("Enter number: "))

        return number

    except ValueError:

        print("Invalid number")

        return None


number = get_number()

print("Number:", number)