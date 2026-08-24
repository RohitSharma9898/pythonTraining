"""
SET COMPREHENSION

Set comprehension creates a set
using a compact syntax.

Syntax:

{expression for item in iterable}
"""


# ==========================================
# BASIC EXAMPLE
# ==========================================

numbers = [1, 2, 3, 4, 5]

squares = {
    number * number
    for number in numbers
}

print(squares)


# ==========================================
# REMOVE DUPLICATES
# ==========================================

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique_numbers = {
    number
    for number in numbers
}

print(unique_numbers)


# ==========================================
# EVEN NUMBERS
# ==========================================

numbers = range(1, 11)

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)


# ==========================================
# FIRST LETTERS
# ==========================================

words = ["Python", "Java", "C++", "SQL"]

first_letters = {
    word[0]
    for word in words
}

print(first_letters)