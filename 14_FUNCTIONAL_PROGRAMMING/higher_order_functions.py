"""
====================================================
             HIGHER-ORDER FUNCTIONS
====================================================

A higher-order function is a function that:

    1. Takes another function as an argument

OR

    2. Returns another function
"""


# ==================================================
# FUNCTION AS ARGUMENT
# ==================================================

def square(number):

    return number * number


def calculate(function, number):

    return function(number)


print(calculate(square, 5))


# ==================================================
# FUNCTION RETURNING FUNCTION
# ==================================================

def create_multiplier(number):

    def multiply(value):

        return value * number

    return multiply


double = create_multiplier(2)

triple = create_multiplier(3)


print(double(10))

print(triple(10))