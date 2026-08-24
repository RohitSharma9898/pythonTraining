"""
GENERATOR

A generator is a special type of iterator.

Generators are created using the
yield keyword.

The main advantage:

A generator produces values one at a time
instead of storing all values in memory.
"""


def numbers():

    yield 1

    yield 2

    yield 3


result = numbers()


print(result)


print(next(result))

print(next(result))

print(next(result))