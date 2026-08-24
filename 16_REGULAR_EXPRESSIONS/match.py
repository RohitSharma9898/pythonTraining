"""
====================================================
                    re.match()
====================================================

match() checks only at the BEGINNING
of the string.
"""


import re


# ==================================================
# MATCH FOUND
# ==================================================

text = "Python is powerful."


result = re.match(r"Python", text)


if result:

    print("Match found.")

else:

    print("No match.")


# ==================================================
# MATCH NOT FOUND
# ==================================================

text = "I love Python."


result = re.match(r"Python", text)


if result:

    print("Match found.")

else:

    print("No match.")


"""
Why?

Because Python is NOT at the beginning.

Difference:

match()
    ↓
Beginning of string

search()
    ↓
Anywhere in string
"""