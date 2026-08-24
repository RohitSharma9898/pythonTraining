"""
====================================================
              PHONE NUMBER VALIDATION
====================================================
"""


import re


phone = input("Enter 10-digit phone number: ")


pattern = r"^[6-9]\d{9}$"


if re.fullmatch(pattern, phone):

    print("Valid Indian mobile number.")

else:

    print("Invalid mobile number.")


"""
Pattern:

[6-9]
    First digit must be 6, 7, 8 or 9

\d{9}
    Followed by exactly 9 digits

Total:
    10 digits
"""