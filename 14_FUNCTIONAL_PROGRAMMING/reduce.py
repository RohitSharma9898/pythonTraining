"""
====================================================
                    reduce()
====================================================

reduce() repeatedly combines values
until only one final value remains.

reduce() is available in functools.
"""

from functools import reduce


numbers = [1, 2, 3, 4, 5]


# ==================================================
# WITHOUT reduce()
# ==================================================

total = 0


for number in numbers:

    total = total + number


print(total)


# ==================================================
# WITH reduce()
# ==================================================

total = reduce(
    lambda a, b: a + b,
    numbers
)


print(total)


"""
Process:

1 + 2 = 3

3 + 3 = 6

6 + 4 = 10

10 + 5 = 15
"""


# ==================================================
# MULTIPLICATION
# ==================================================

numbers = [1, 2, 3, 4]


result = reduce(
    lambda a, b: a * b,
    numbers
)


print(result)