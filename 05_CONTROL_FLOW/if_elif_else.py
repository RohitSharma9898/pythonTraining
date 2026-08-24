"""
IF-ELIF-ELSE

Used when we have multiple conditions.

Syntax:

if condition:
    statement

elif condition:
    statement

else:
    statement
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

marks = 75

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Grade D")


# ==========================================
# NUMBER CHECK
# ==========================================

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")


# ==========================================
# AGE CATEGORY
# ==========================================

age = int(input("Enter your age: "))

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior citizen")


# ==========================================
# SIMPLE CALCULATOR
# ==========================================

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)

elif operator == "-":
    print("Result:", a - b)

elif operator == "*":
    print("Result:", a * b)

elif operator == "/":
    print("Result:", a / b)

else:
    print("Invalid operator")