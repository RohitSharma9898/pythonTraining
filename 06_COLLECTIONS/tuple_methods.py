"""
TUPLE METHODS

Tuple has only two main built-in methods:

count()
index()
"""

numbers = (10, 20, 10, 30, 10)


# ==========================================
# count()
# ==========================================

print(numbers.count(10))

print(numbers.count(20))


# ==========================================
# index()
# ==========================================

print(numbers.index(20))

print(numbers.index(30))


# ==========================================
# TUPLE CONVERSION
# ==========================================

numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
print(type(numbers_tuple))


# Tuple to list

numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list)
print(type(numbers_list))