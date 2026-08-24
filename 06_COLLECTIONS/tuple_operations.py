"""
TUPLE OPERATIONS

Tuple is immutable.
"""

numbers = (10, 20, 30, 40, 50)

# ==========================================
# ACCESS
# ==========================================

print(numbers[0])
print(numbers[-1])


# ==========================================
# SLICING
# ==========================================

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# ==========================================
# CONCATENATION
# ==========================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)


# ==========================================
# REPETITION
# ==========================================

print(tuple1 * 3)


# ==========================================
# MEMBERSHIP
# ==========================================

print(20 in numbers)

print(100 not in numbers)


# ==========================================
# LENGTH
# ==========================================

print(len(numbers))


# ==========================================
# IMMUTABILITY
# ==========================================

# numbers[0] = 100

# This causes TypeError because
# tuples cannot be modified.