"""
ITERATOR WITH FOR LOOP
"""


numbers = [10, 20, 30]


iterator = iter(numbers)


for number in iterator:

    print(number)


"""
The for loop internally keeps calling
next() until StopIteration occurs.
"""