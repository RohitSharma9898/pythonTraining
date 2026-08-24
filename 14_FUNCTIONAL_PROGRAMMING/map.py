"""
====================================================
                     map()
====================================================

map() applies a function to every item
of an iterable.

Syntax:

map(function, iterable)
"""


numbers = [1, 2, 3, 4, 5]


# ==================================================
# WITHOUT map()
# ==================================================

squares = []

for number in numbers:

    squares.append(number * number)


print(squares)


# ==================================================
# WITH map()
# ==================================================

def square(number):

    return number * number


result = map(square, numbers)


print(list(result))


# ==================================================
# USING LAMBDA
# ==================================================

numbers = [1, 2, 3, 4, 5]


squares = map(
    lambda number: number * number,
    numbers
)


print(list(squares))