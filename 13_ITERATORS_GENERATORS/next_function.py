"""
next()

next() gets the next value from
an iterator.
"""


numbers = [10, 20, 30, 40]


iterator = iter(numbers)


print(next(iterator))

print(next(iterator))

print(next(iterator))

print(next(iterator))


"""
Output:

10
20
30
40
"""


# ==========================================
# NO MORE VALUES
# ==========================================

"""
If we call next() again:

next(iterator)

Python raises:

StopIteration

because there are no more values.
"""


try:

    print(next(iterator))

except StopIteration:

    print("No more values.")