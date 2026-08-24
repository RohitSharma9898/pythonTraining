"""
====================================================
                  re.findall()
====================================================

findall() finds ALL occurrences of a pattern
and returns them as a list.
"""


import re


text = "Python Java Python C++ Python"


result = re.findall(r"Python", text)


print(result)

print("Total:", len(result))


# ==================================================
# FIND ALL NUMBERS
# ==================================================

text = "I have 10 apples and 5 oranges."


numbers = re.findall(r"\d+", text)


print(numbers)