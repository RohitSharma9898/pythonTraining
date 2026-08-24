"""
NESTED LIST COMPREHENSION

A list comprehension inside another
list comprehension.
"""


# ==========================================
# NORMAL NESTED LOOP
# ==========================================

result = []

for i in range(1, 4):

    for j in range(1, 4):

        result.append((i, j))

print(result)


# ==========================================
# NESTED LIST COMPREHENSION
# ==========================================

result = [
    (i, j)
    for i in range(1, 4)
    for j in range(1, 4)
]

print(result)


# ==========================================
# MULTIPLICATION TABLE
# ==========================================

table = [
    number * 2
    for number in range(1, 11)
]

print(table)


# ==========================================
# FLATTEN A NESTED LIST
# ==========================================

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    number
    for row in numbers
    for number in row
]

print(result)


# ==========================================
# MATRIX
# ==========================================

matrix = [
    [1, 2],
    [3, 4]
]

result = [
    number * 2
    for row in matrix
    for number in row
]

print(result)