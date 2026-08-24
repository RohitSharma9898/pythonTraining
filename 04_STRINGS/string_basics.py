"""
STRING BASICS

A string is a sequence of characters.

Strings can be created using:
1. Single quotes
2. Double quotes
3. Triple quotes

Strings are:
- Ordered
- Immutable
- Iterable
"""

# ==========================================
# CREATING STRINGS
# ==========================================

name = 'Rohit'
language = "Python"

print(name)
print(language)


# Triple quotes

message = """
Welcome to Python Programming.
Python is easy to learn.
"""

print(message)


# ==========================================
# STRING TYPE
# ==========================================

text = "Python"

print(text)
print(type(text))


# ==========================================
# STRING WITH NUMBERS
# ==========================================

number = "12345"

print(number)
print(type(number))


# This is an integer, not a string

number = 12345

print(number)
print(type(number))


# ==========================================
# STRING LENGTH
# ==========================================

word = "Python"

print("Length:", len(word))


# ==========================================
# EMPTY STRING
# ==========================================

empty = ""

print(empty)
print(len(empty))


# ==========================================
# STRING CONCATENATION
# ==========================================

first_name = "Rohit"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)


# ==========================================
# STRING REPETITION
# ==========================================

print("Python " * 3)


# ==========================================
# MEMBERSHIP OPERATORS
# ==========================================

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)


# ==========================================
# STRINGS ARE IMMUTABLE
# ==========================================

word = "Python"

# This will cause TypeError:

# word[0] = "J"

# We cannot directly modify a character
# inside an existing string.


# Instead, create a new string

word = "J" + word[1:]

print(word)