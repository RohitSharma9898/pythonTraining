"""
ITERATOR VS GENERATOR
"""


# ==========================================
# ITERATOR
# ==========================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))

print(next(iterator))

print(next(iterator))


# ==========================================
# GENERATOR
# ==========================================

def generate_numbers():

    yield 10

    yield 20

    yield 30


generator = generate_numbers()

print(next(generator))

print(next(generator))

print(next(generator))


"""
Both can produce values one at a time.

Difference:

Iterator:
    Usually created from an iterable
    or implemented manually.

Generator:
    Easy way to create an iterator
    using yield.
"""