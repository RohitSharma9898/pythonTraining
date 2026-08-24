"""
STRING SLICING

Slicing is used to extract a portion of a string.

Syntax:

string[start:stop:step]

start -> starting index
stop  -> ending index (not included)
step  -> jump between characters
"""

text = "Python Programming"

# ==========================================
# BASIC SLICING
# ==========================================

print(text[0:6])

print(text[7:18])


# ==========================================
# OMITTING START
# ==========================================

print(text[:6])


# ==========================================
# OMITTING STOP
# ==========================================

print(text[7:])


# ==========================================
# COPY ENTIRE STRING
# ==========================================

print(text[:])


# ==========================================
# USING STEP
# ==========================================

text = "Python"

print(text[0:6:1])

print(text[0:6:2])

print(text[::2])


# ==========================================
# REVERSE STRING
# ==========================================

print(text[::-1])


# ==========================================
# REVERSE USING NEGATIVE STEP
# ==========================================

print(text[5:0:-1])


# ==========================================
# PRACTICAL EXAMPLES
# ==========================================

name = "Rohit Sharma"

# First name

print(name[:5])

# Last name

print(name[6:])


# ==========================================
# EVEN INDEX CHARACTERS
# ==========================================

text = "ABCDEFGHIJ"

print(text[::2])


# ==========================================
# ODD INDEX CHARACTERS
# ==========================================

print(text[1::2])


# ==========================================
# NEGATIVE INDEX SLICING
# ==========================================

text = "Python"

print(text[-4:-1])

print(text[-1:-5:-1])