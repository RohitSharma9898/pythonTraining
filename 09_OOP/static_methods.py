"""
STATIC METHOD

A static method does not depend on
object or class data.

Decorator:

@staticmethod
"""


class Calculator:

    @staticmethod
    def add(a, b):

        return a + b

    @staticmethod
    def multiply(a, b):

        return a * b


print(Calculator.add(10, 20))

print(Calculator.multiply(5, 4))