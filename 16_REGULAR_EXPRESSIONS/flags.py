"""
====================================================
                     FLAGS
====================================================

Flags change how regex behaves.
"""


import re


text = "Python PYTHON python"


# ==================================================
# WITHOUT IGNORECASE
# ==================================================

result = re.findall(
    r"python",
    text
)

print(result)


# ==================================================
# WITH IGNORECASE
# ==================================================

result = re.findall(
    r"python",
    text,
    re.IGNORECASE
)

print(result)


"""
re.IGNORECASE
    or
re.I

ignores uppercase/lowercase differences.
"""