"""
GENERATOR EXPRESSION

Similar to list comprehension,
but uses parentheses instead of
square brackets.
"""


# LIST COMPREHENSION

numbers = [x * x for x in range(5)]

print(numbers)


# GENERATOR EXPRESSION

numbers = (x * x for x in range(5))

print(numbers)


# Get values one by one

print(next(numbers))

print(next(numbers))

print(next(numbers))