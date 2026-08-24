"""
Tuple Data Type

A tuple is:
- Ordered
- Immutable
- Allows duplicate values
- Can store different data types
"""

# Creating tuple

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))


# Single element tuple

value = (10,)

print(value)
print(type(value))


# Without comma it is an integer

value = (10)

print(value)
print(type(value))


# ==============================
# INDEXING
# ==============================

names = ("Rohit", "Rahul", "Aman", "Vikas")

print(names[0])
print(names[-1])


# ==============================
# SLICING
# ==============================

print(names[0:2])
print(names[:3])
print(names[2:])


# ==============================
# DUPLICATES
# ==============================

numbers = (10, 20, 10, 30, 10)

print(numbers)


# ==============================
# TUPLE METHODS
# ==============================

print(numbers.count(10))
print(numbers.index(20))


# ==============================
# IMMUTABILITY
# ==============================

# This will cause TypeError:

# names[0] = "Arjun"


# ==============================
# TUPLE UNPACKING
# ==============================

student = ("Rohit", 21, "Python")

name, age, course = student

print(name)
print(age)
print(course)