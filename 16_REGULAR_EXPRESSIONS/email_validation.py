"""
====================================================
                EMAIL VALIDATION
====================================================
"""


import re


def is_valid_email(email):

    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"


    if re.fullmatch(pattern, email):

        return True

    return False


email = input("Enter email: ")


if is_valid_email(email):

    print("Valid email.")

else:

    print("Invalid email.")