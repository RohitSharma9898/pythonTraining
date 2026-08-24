"""
Mutable vs Immutable Objects

Mutable:
    Object can be changed after creation.

Immutable:
    Object cannot be changed after creation.

Mutable:
- list
- dictionary
- set

Immutable:
- int
- float
- bool
- string
- tuple
- frozenset
"""


# ==========================================
# IMMUTABLE EXAMPLE - INTEGER
# ==========================================

x = 10

print("Before:", x)
print("ID:", id(x))

x = 20

print("After:", x)
print("ID:", id(x))


# A new integer object is created.


# ==========================================
# IMMUTABLE EXAMPLE - STRING
# ==========================================

name = "Rohit"

print(name)
print(id(name))

# This creates a new string

name = name + " Sharma"

print(name)
print(id(name))


# ==========================================
# MUTABLE EXAMPLE - LIST
# ==========================================

numbers = [10, 20, 30]

print("Before:", numbers)
print("ID:", id(numbers))

numbers.append(40)

print("After:", numbers)
print("ID:", id(numbers))


# Same list object was modified.


# ==========================================
# MUTABLE EXAMPLE - DICTIONARY
# ==========================================

student = {
    "name": "Rohit",
    "marks": 90
}

print(student)
print(id(student))

student["marks"] = 95

print(student)
print(id(student))


# ==========================================
# MUTABLE EXAMPLE - SET
# ==========================================

numbers = {1, 2, 3}

print(numbers)
print(id(numbers))

numbers.add(4)

print(numbers)
print(id(numbers))


# ==========================================
# TUPLE
# ==========================================

data = (10, 20, 30)

print(data)

# This is not allowed:

# data[0] = 100


# ==========================================
# QUICK SUMMARY
# ==========================================

"""
Immutable:
int
float
bool
str
tuple
frozenset

Mutable:
list
dict
set
"""