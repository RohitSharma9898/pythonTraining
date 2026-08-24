"""
====================================================
              SPECIAL CHARACTERS
====================================================
"""


import re


# ==================================================
# ^ -> START
# ==================================================

text = "Python is easy."


if re.search(r"^Python", text):

    print("Text starts with Python.")


# ==================================================
# $ -> END
# ==================================================

text = "I love Python"


if re.search(r"Python$", text):

    print("Text ends with Python.")


# ==================================================
# . -> ANY CHARACTER
# ==================================================

text = "cat cot cut"


result = re.findall(r"c.t", text)


print(result)


"""
c.t means:

c
any one character
t
"""


# ==================================================
# [] -> CHARACTER SET
# ==================================================

text = "cat bat mat rat"


result = re.findall(r"[cm]at", text)


print(result)


# ==================================================
# [a-z]
# ==================================================

text = "abc XYZ 123"


result = re.findall(r"[a-z]+", text)


print(result)