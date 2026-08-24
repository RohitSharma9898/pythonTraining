"""
GENERATOR EXPRESSION

Generator expressions look similar to
list comprehensions.

Difference:

List comprehension:
    Creates the complete list immediately.

Generator expression:
    Produces values one by one when needed.

Syntax:

(expression for item in iterable)
"""


# ==========================================
# LIST COMPREHENSION
# ==========================================

numbers = [number * 2 for number in range(1, 6)]

print(numbers)


# ==========================================
# GENERATOR EXPRESSION
# ==========================================

numbers = (
    number * 2
    for number in range(1, 6)
)

print(numbers)


# ==========================================
# GET VALUES USING LOOP
# ==========================================

for number in numbers:
    print(number)


# ==========================================
# USING next()
# ==========================================

numbers = (
    number * 2
    for number in range(1, 6)
)

print(next(numbers))
print(next(numbers))
print(next(numbers))


# ==========================================
# CHECK TYPE
# ==========================================

numbers = (
    number * 2
    for number in range(1, 6)
)

print(type(numbers))