"""
LIST OPERATIONS

A list is:
- Ordered
- Mutable
- Allows duplicate values
- Allows different data types
"""

# ==========================================
# CREATING A LIST
# ==========================================

numbers = [10, 20, 30, 40, 50]

print(numbers)


# ==========================================
# ACCESSING ELEMENTS
# ==========================================

print(numbers[0])
print(numbers[2])
print(numbers[-1])


# ==========================================
# SLICING
# ==========================================

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# ==========================================
# MODIFYING ELEMENT
# ==========================================

numbers[0] = 100

print(numbers)


# ==========================================
# CONCATENATING LISTS
# ==========================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)


# ==========================================
# REPEATING LIST
# ==========================================

numbers = [1, 2, 3]

print(numbers * 3)


# ==========================================
# MEMBERSHIP
# ==========================================

numbers = [10, 20, 30]

print(20 in numbers)
print(50 in numbers)

print(50 not in numbers)


# ==========================================
# LENGTH
# ==========================================

print(len(numbers))