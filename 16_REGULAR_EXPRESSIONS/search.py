"""
====================================================
                    re.search()
====================================================

search() searches for a pattern anywhere
inside the string.

If the pattern is found:

    Match object is returned.

If not found:

    None is returned.
"""


import re


text = "Python is easy to learn."


result = re.search(r"Python", text)


if result:

    print("Pattern found.")

else:

    print("Pattern not found.")


# ==================================================
# SEARCH FOR A NUMBER
# ==================================================

text = "I am 21 years old."


result = re.search(r"\d+", text)


if result:

    print("Number found:", result.group())