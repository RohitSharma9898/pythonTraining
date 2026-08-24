"""
GENERATOR FUNCTION

A function containing yield becomes
a generator function.
"""


def count():

    yield 1

    yield 2

    yield 3

    yield 4

    yield 5


numbers = count()


for number in numbers:

    print(number)