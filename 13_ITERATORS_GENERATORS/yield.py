"""
yield

yield returns a value from a generator
without completely ending the function.

When next() is called again,
the function continues from where
it stopped.
"""


def demo():

    print("First step")

    yield 10


    print("Second step")

    yield 20


    print("Third step")

    yield 30


generator = demo()


print(next(generator))

print(next(generator))

print(next(generator))