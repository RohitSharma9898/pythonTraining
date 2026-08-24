"""
METHOD OVERLOADING

Python does not support traditional
method overloading like Java.

We can achieve similar behavior using
default arguments or *args.
"""


class Calculator:

    def add(self, a=0, b=0, c=0):

        return a + b + c


calculator = Calculator()

print(calculator.add(10, 20))

print(calculator.add(10, 20, 30))


# ==========================================
# USING *args
# ==========================================

class Calculator2:

    def add(self, *numbers):

        total = 0

        for number in numbers:

            total += number

        return total


calculator = Calculator2()

print(calculator.add(10, 20))

print(calculator.add(10, 20, 30, 40))