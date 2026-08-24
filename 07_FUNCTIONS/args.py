"""
*args

*args allows a function to accept
any number of positional arguments.

The arguments are received as a tuple.
"""


# ==========================================
# BASIC EXAMPLE
# ==========================================

def add(*numbers):

    print(numbers)


add(10, 20)

add(10, 20, 30)

add(1, 2, 3, 4, 5)


# ==========================================
# SUM USING *args
# ==========================================

def add_numbers(*numbers):

    total = 0

    for number in numbers:
        total = total + number

    return total


print(add_numbers(10, 20))

print(add_numbers(10, 20, 30))

print(add_numbers(1, 2, 3, 4, 5))


# ==========================================
# *args IS A TUPLE
# ==========================================

def show(*values):

    print(values)
    print(type(values))


show(10, 20, 30)