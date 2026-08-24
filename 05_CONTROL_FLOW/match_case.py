"""
MATCH-CASE

match-case is used for pattern matching.

It is similar to switch-case in other languages.

Available in Python 3.10+

Syntax:

match value:

    case value1:
        statement

    case value2:
        statement

    case _:
        statement
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

day = 2

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Invalid day")


# ==========================================
# USER INPUT
# ==========================================

choice = int(input("Enter 1, 2 or 3: "))

match choice:

    case 1:
        print("You selected Python.")

    case 2:
        print("You selected Java.")

    case 3:
        print("You selected C++.")

    case _:
        print("Invalid choice.")


# ==========================================
# CALCULATOR
# ==========================================

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator: ")

match operator:

    case "+":
        print("Result:", a + b)

    case "-":
        print("Result:", a - b)

    case "*":
        print("Result:", a * b)

    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")

    case _:
        print("Invalid operator.")