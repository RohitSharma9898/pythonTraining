"""
IMPORTANT LIST METHODS
"""

numbers = [10, 20, 30]

# ==========================================
# append()
# ==========================================

numbers.append(40)

print(numbers)


# ==========================================
# insert()
# ==========================================

numbers.insert(1, 15)

print(numbers)


# ==========================================
# extend()
# ==========================================

numbers.extend([50, 60])

print(numbers)


# ==========================================
# remove()
# ==========================================

numbers.remove(15)

print(numbers)


# ==========================================
# pop()
# ==========================================

removed = numbers.pop()

print("Removed:", removed)
print(numbers)


# Pop using index

removed = numbers.pop(0)

print("Removed:", removed)
print(numbers)


# ==========================================
# clear()
# ==========================================

numbers.clear()

print(numbers)


# ==========================================
# COPY
# ==========================================

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(new_numbers)


# ==========================================
# COUNT
# ==========================================

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))


# ==========================================
# INDEX
# ==========================================

print(numbers.index(20))


# ==========================================
# SORT
# ==========================================

numbers = [5, 2, 8, 1, 9]

numbers.sort()

print(numbers)


# Descending order

numbers.sort(reverse=True)

print(numbers)


# ==========================================
# REVERSE
# ==========================================

numbers.reverse()

print(numbers)