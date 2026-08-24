"""
LIST COMPREHENSION

List comprehension is a short way to create a list.

Normal approach:

numbers = []

for i in range(1, 6):
    numbers.append(i)

List comprehension:

numbers = [i for i in range(1, 6)]
"""


# ==========================================
# NORMAL FOR LOOP
# ==========================================

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)


# ==========================================
# LIST COMPREHENSION
# ==========================================

numbers = [i for i in range(1, 6)]

print(numbers)


# ==========================================
# SQUARES
# ==========================================

squares = [i * i for i in range(1, 6)]

print(squares)


# ==========================================
# CUBES
# ==========================================

cubes = [i ** 3 for i in range(1, 6)]

print(cubes)


# ==========================================
# CHARACTERS FROM STRING
# ==========================================

word = "Python"

characters = [char for char in word]

print(characters)


# ==========================================
# MULTIPLY EACH NUMBER
# ==========================================

numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

print(result)