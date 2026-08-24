"""
Set Data Type

A set is:
- Unordered
- Mutable
- Does not allow duplicate values
- Does not support indexing
"""

# Creating a set

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))


# Duplicate values are automatically removed

numbers = {10, 20, 10, 30, 20}

print(numbers)


# ==============================
# ADD ELEMENT
# ==============================

numbers.add(50)

print(numbers)


# ==============================
# UPDATE
# ==============================

numbers.update([60, 70, 80])

print(numbers)


# ==============================
# REMOVE
# ==============================

numbers.remove(80)

print(numbers)


# discard() does not give an error
# if the element doesn't exist

numbers.discard(100)

print(numbers)


# ==============================
# SET OPERATIONS
# ==============================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


# Union

print("Union:", A | B)

# Intersection

print("Intersection:", A & B)

# Difference

print("A - B:", A - B)

print("B - A:", B - A)

# Symmetric difference

print("Symmetric Difference:", A ^ B)


# ==============================
# MEMBERSHIP
# ==============================

print(2 in A)
print(10 in A)


# ==============================
# IMPORTANT
# ==============================

# Empty set

empty_set = set()

print(type(empty_set))


# {} is NOT an empty set.
# It creates an empty dictionary.

empty = {}

print(type(empty))
