"""
CUSTOM ITERATOR

We can create our own iterator.

An iterator class should implement:

__iter__()
__next__()
"""


class Count:

    def __init__(self, maximum):

        self.current = 1
        self.maximum = maximum


    def __iter__(self):

        return self


    def __next__(self):

        if self.current <= self.maximum:

            value = self.current

            self.current += 1

            return value

        else:

            raise StopIteration


counter = Count(5)


for number in counter:

    print(number)