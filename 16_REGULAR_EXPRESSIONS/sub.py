"""
====================================================
                    re.sub()
====================================================

re.sub() is used to replace matching text.
"""


import re


text = "I love Java. Java is popular."


result = re.sub(
    r"Java",
    "Python",
    text
)


print(result)


# ==================================================
# REMOVE ALL DIGITS
# ==================================================

text = "My number is 9876543210."


result = re.sub(
    r"\d",
    "*",
    text
)


print(result)