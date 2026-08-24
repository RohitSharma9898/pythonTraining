"""
CUSTOM ITERATOR USING A CLASS

Example:

Create an iterator that returns
numbers from start to end.
"""


class NumberIterator:

    def __init__(self, start, end):

        self.current = start
        self.end = end


    def __iter__(self):

        return self


    def __next__(self):

        if self.current <= self.end:

            number = self.current

            self.current += 1

            return number

        raise StopIteration


numbers = NumberIterator(1, 5)


for number in numbers:

    print(number)