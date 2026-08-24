"""
iter()

iter() converts an iterable into
an iterator.
"""


numbers = [10, 20, 30]


print("List:", numbers)


iterator = iter(numbers)


print("Iterator:", iterator)


# Now the iterator can give us
# values one by one.