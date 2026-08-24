"""
DICTIONARY COMPREHENSION

Dictionary comprehension is a short way
to create dictionaries.

Syntax:

{key: value for item in iterable}
"""


# ==========================================
# BASIC EXAMPLE
# ==========================================

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number * number
    for number in numbers
}

print(squares)


# ==========================================
# NUMBER : CUBE
# ==========================================

cubes = {
    number: number ** 3
    for number in range(1, 6)
}

print(cubes)


# ==========================================
# NUMBER : EVEN / ODD
# ==========================================

numbers = [1, 2, 3, 4, 5]

result = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print(result)


# ==========================================
# WORD : LENGTH
# ==========================================

words = ["Python", "Java", "SQL"]

result = {
    word: len(word)
    for word in words
}

print(result)
