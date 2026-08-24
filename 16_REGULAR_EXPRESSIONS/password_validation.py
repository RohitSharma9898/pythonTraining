"""
====================================================
             PASSWORD VALIDATION
====================================================

Requirements:

    At least 8 characters
    One uppercase letter
    One lowercase letter
    One digit
"""


import re


password = input("Enter password: ")


pattern = (
    r"^(?=.*[A-Z])"
    r"(?=.*[a-z])"
    r"(?=.*\d)"
    r".{8,}$"
)


if re.fullmatch(pattern, password):

    print("Strong password.")

else:

    print("Password does not meet requirements.")