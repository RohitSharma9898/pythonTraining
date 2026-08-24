"""
====================================================
                CHARACTER CLASSES
====================================================

Character classes allow us to define
what characters we want to match.
"""


import re


# ==================================================
# \d -> DIGIT
# ==================================================

text = "Age: 21"


print(re.findall(r"\d", text))

print(re.findall(r"\d+", text))


"""
\d
    One digit

\d+
    One or more digits
"""


# ==================================================
# \D -> NOT A DIGIT
# ==================================================

text = "Python123"


print(re.findall(r"\D+", text))


# ==================================================
# \w -> WORD CHARACTER
# ==================================================

text = "Python_123"


print(re.findall(r"\w+", text))


# ==================================================
# \W -> NOT A WORD CHARACTER
# ==================================================

text = "Python@123"


print(re.findall(r"\W", text))


# ==================================================
# \s -> WHITESPACE
# ==================================================

text = "Python is easy"


print(re.findall(r"\s", text))


# ==================================================
# \S -> NOT WHITESPACE
# ==================================================

print(re.findall(r"\S+", text))