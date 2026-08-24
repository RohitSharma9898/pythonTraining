"""
IF STATEMENT

The if statement is used to execute a block of code
when a condition is True.

Syntax:

if condition:
    statement
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

age = 20

if age >= 18:
    print("You are eligible to vote.")


# ==========================================
# CONDITION IS FALSE
# ==========================================

age = 15

if age >= 18:
    print("You can vote.")

# Nothing will be printed because the condition is False.


# ==========================================
# COMPARISON WITH IF
# ==========================================

marks = 75

if marks >= 40:
    print("Student has passed.")


# ==========================================
# MULTIPLE CONDITIONS
# ==========================================

number = 10

if number > 0:
    print("Number is positive.")

if number % 2 == 0:
    print("Number is even.")


# ==========================================
# USER INPUT
# ==========================================

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")


# ==========================================
# STRING CONDITION
# ==========================================

name = input("Enter your name: ")

if name == "Rohit":
    print("Welcome Rohit!")


# ==========================================
# LOGICAL OPERATOR WITH IF
# ==========================================

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")