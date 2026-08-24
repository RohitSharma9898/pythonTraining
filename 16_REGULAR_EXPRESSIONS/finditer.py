"""
====================================================
                 re.finditer()
====================================================

finditer() finds all matches and returns
Match objects one by one.
"""


import re


text = "Python Java Python C++ Python"


matches = re.finditer(r"Python", text)


for match in matches:

    print("Value:", match.group())

    print("Starting position:", match.start())

    print("Ending position:", match.end())

    print()