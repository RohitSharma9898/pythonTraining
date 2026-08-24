"""
LIST COMPREHENSION WITH IF

Syntax:

[expression for item in iterable if condition]
"""


# ==========================================
# EVEN NUMBERS
# ==========================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ==========================================
# ODD NUMBERS
# ==========================================

odd_numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print(odd_numbers)


# ==========================================
# POSITIVE NUMBERS
# ==========================================

numbers = [-5, 10, -2, 20, 30, -1]

positive_numbers = [
    number
    for number in numbers
    if number > 0
]

print(positive_numbers)


# ==========================================
# NUMBERS GREATER THAN 10
# ==========================================

numbers = [5, 12, 8, 20, 25, 3]

result = [
    number
    for number in numbers
    if number > 10
]

print(result)


# ==========================================
# WORDS WITH LENGTH > 5
# ==========================================

words = ["Python", "Java", "Programming", "SQL", "JavaScript"]

long_words = [
    word
    for word in words
    if len(word) > 5
]

print(long_words)