"""
====================================================
                    re.split()
====================================================

re.split() splits a string using a
regular expression pattern.
"""


import re


# ==================================================
# SPLIT USING SPACE
# ==================================================

text = "Python is easy"


result = re.split(r"\s+", text)


print(result)


# ==================================================
# SPLIT USING COMMA
# ==================================================

text = "Python,Java,C++,JavaScript"


result = re.split(r",", text)


print(result)