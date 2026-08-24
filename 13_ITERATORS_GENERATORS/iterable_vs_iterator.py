"""
ITERABLE VS ITERATOR
"""


# ==========================================
# ITERABLE
# ==========================================

numbers = [10, 20, 30, 40]

"""
A list is an iterable.

We can iterate over it using a for loop.
"""

for number in numbers:

    print(number)


# ==========================================
# CONVERT ITERABLE INTO ITERATOR
# ==========================================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)


print(type(numbers))

print(type(iterator))


"""
list       -> Iterable
iterator   -> Iterator
"""