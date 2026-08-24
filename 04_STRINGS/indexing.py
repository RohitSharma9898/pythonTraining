"""
STRING INDEXING

Indexing is used to access individual characters
from a string.

Positive indexing starts from 0.

Negative indexing starts from -1.
"""

text = "Python"

# Positive indexing

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])


# Negative indexing

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
print(text[-6])


# ==========================================
# INDEX POSITION
# ==========================================

"""
String: P  y  t  h  o  n
Index:  0  1  2  3  4  5
Negative:
       -6 -5 -4 -3 -2 -1
"""


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================

name = "Rohit Sharma"

print("First character:", name[0])
print("Last character:", name[-1])


# ==========================================
# ACCESSING USER INPUT
# ==========================================

word = input("Enter a word: ")

print("First character:", word[0])
print("Last character:", word[-1])


# ==========================================
# INDEX ERROR
# ==========================================

text = "Python"

# text[10]

# This causes:
# IndexError: string index out of range


# ==========================================
# LENGTH AND LAST INDEX
# ==========================================

text = "Programming"

print("Length:", len(text))

print("Last character:", text[len(text) - 1])

# Easier way:

print("Last character:", text[-1])