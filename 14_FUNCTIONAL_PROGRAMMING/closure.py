"""
====================================================
                    CLOSURE
====================================================

A closure occurs when an inner function
remembers values from its outer function
even after the outer function has finished.
"""


def create_multiplier(number):

    def multiply(value):

        return value * number

    return multiply


double = create_multiplier(2)

triple = create_multiplier(3)


print(double(5))

print(triple(5))


"""
double remembers:

    number = 2


triple remembers:

    number = 3
"""