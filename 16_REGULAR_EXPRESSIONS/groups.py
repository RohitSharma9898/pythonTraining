"""
====================================================
                    GROUPS
====================================================

Parentheses () are used to create groups.

Groups allow us to extract specific
parts of a match.
"""


import re


text = "Name: Rohit, Age: 21"


pattern = r"Name: (\w+), Age: (\d+)"


result = re.search(pattern, text)


if result:

    print("Complete match:", result.group())

    print("Name:", result.group(1))

    print("Age:", result.group(2))