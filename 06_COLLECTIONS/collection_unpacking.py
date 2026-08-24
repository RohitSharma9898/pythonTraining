"""
COLLECTION UNPACKING

Unpacking means assigning collection elements
to individual variables.
"""

# ==========================================
# LIST UNPACKING
# ==========================================

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)


# ==========================================
# TUPLE UNPACKING
# ==========================================

student = ("Rohit", 21, "Python")

name, age, course = student

print(name)
print(age)
print(course)


# ==========================================
# SWAPPING VARIABLES
# ==========================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# ==========================================
# STAR UNPACKING
# ==========================================

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ==========================================
# DICTIONARY UNPACKING
# ==========================================

student = {
    "name": "Rohit",
    "age": 21
}

name = student["name"]
age = student["age"]

print(name)
print(age)