"""
====================================================
             FIRST-CLASS FUNCTIONS
====================================================

Python treats functions like normal values.

A function can be:

    stored in a variable
    passed as an argument
    returned from another function
"""


def square(number):

    return number * number


def calculate(function, number):

    return function(number)


result = calculate(square, 5)


print(result)