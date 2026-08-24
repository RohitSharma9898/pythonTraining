"""
String Data Type

A string is a sequence of characters.

Strings can be created using:
- Single quotes
- Double quotes
- Triple quotes
"""

# Single quotes

name = 'Rohit'

print(name)
print(type(name))


# Double quotes

language = "Python"

print(language)


# Triple quotes

message = """
Python is easy to learn.
Python is powerful.
Python is widely used.
"""

print(message)


# String with numbers

value = "12345"

print(value)
print(type(value))


# ==============================
# INDEXING
# ==============================

word = "Python"

print(word[0])
print(word[1])
print(word[2])

# Negative indexing

print(word[-1])
print(word[-2])


# ==============================
# SLICING
# ==============================

print(word[0:3])
print(word[2:6])
print(word[:4])
print(word[2:])
print(word[:])

# Reverse

print(word[::-1])


# ==============================
# STRING LENGTH
# ==============================

print(len(word))


# ==============================
# STRING METHODS
# ==============================

text = "python programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

print(text.replace("python", "Java"))

print(text.startswith("python"))
print(text.endswith("ing"))

print(text.count("p"))

print(text.find("programming"))


# ==============================
# STRING CONCATENATION
# ==============================

first_name = "Rohit"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)


# ==============================
# STRING REPETITION
# ==============================

print("Python " * 3)


# ==============================
# MEMBERSHIP
# ==============================

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)


# ==============================
# STRING FORMATTING
# ==============================

name = "Rohit"
age = 21

print("My name is {} and I am {} years old.".format(name, age))

print(f"My name is {name} and I am {age} years old.")