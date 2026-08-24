"""
Frozenset

A frozenset is an immutable version of a set.

It:
- Does not allow duplicate values
- Is unordered
- Cannot be modified
"""

# Creating frozenset

numbers = frozenset([10, 20, 30, 40])

print(numbers)
print(type(numbers))


# Duplicate values

numbers = frozenset([10, 20, 10, 30, 20])

print(numbers)


# ==============================
# SET OPERATIONS
# ==============================

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)


# Membership

print(2 in A)


# ==============================
# IMMUTABILITY
# ==============================

# These operations are NOT allowed:

# A.add(5)
# A.remove(2)

# They will cause AttributeError.


# ==============================
# Why use frozenset?
# ==============================

# A frozenset can be used as a dictionary key.

data = {
    frozenset([1, 2]): "Group A"
}

print(data)
