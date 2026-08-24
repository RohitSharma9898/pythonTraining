"""
NESTED IF

An if statement inside another if statement
is called a nested if.

Syntax:

if condition1:
    if condition2:
        statement
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

age = 20
has_id = True

if age >= 18:

    if has_id:
        print("You can enter.")

    else:
        print("ID is required.")

else:
    print("You are underage.")


# ==========================================
# LOGIN EXAMPLE
# ==========================================

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "1234":
        print("Login successful.")

    else:
        print("Incorrect password.")

else:
    print("Username not found.")


# ==========================================
# NUMBER EXAMPLE
# ==========================================

number = int(input("Enter a number: "))

if number > 0:

    if number % 2 == 0:
        print("Positive even number.")

    else:
        print("Positive odd number.")

else:
    print("Number is not positive.")