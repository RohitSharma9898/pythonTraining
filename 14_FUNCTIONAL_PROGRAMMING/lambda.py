"""
====================================================
                    LAMBDA
====================================================

A lambda is a small anonymous function.

Normal function:

def square(number):
    return number * number


Lambda:

lambda number: number * number
"""


# ==================================================
# NORMAL FUNCTION
# ==================================================

def square(number):

    return number * number


print(square(5))


# ==================================================
# LAMBDA
# ==================================================

square = lambda number: number * number


print(square(5))


# ==================================================
# TWO PARAMETERS
# ==================================================

add = lambda a, b: a + b


print(add(10, 20))


# ==================================================
# CHECK EVEN NUMBER
# ==================================================

is_even = lambda number: number % 2 == 0


print(is_even(10))

print(is_even(7))