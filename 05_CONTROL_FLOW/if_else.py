"""
IF-ELSE STATEMENT

if:
    Runs when condition is True.

else:
    Runs when condition is False.

Syntax:

if condition:
    statement
else:
    statement
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")


# ==========================================
# EVEN OR ODD
# ==========================================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ==========================================
# POSITIVE OR NEGATIVE
# ==========================================

number = int(input("Enter a number: "))

if number >= 0:
    print("Positive number")
else:
    print("Negative number")


# ==========================================
# PASS OR FAIL
# ==========================================

marks = float(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# ==========================================
# LOGIN EXAMPLE
# ==========================================

password = input("Enter password: ")

if password == "1234":
    print("Login successful")
else:
    print("Incorrect password")