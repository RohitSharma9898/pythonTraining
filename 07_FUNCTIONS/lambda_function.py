"""
LAMBDA FUNCTION

A lambda is a small anonymous function.

Syntax:

lambda arguments: expression
"""


# ==========================================
# NORMAL FUNCTION
# ==========================================

def square(number):

    return number * number


print(square(5))


# ==========================================
# SAME THING USING LAMBDA
# ==========================================

square = lambda number: number * number

print(square(5))


# ==========================================
# ADD TWO NUMBERS
# ==========================================

add = lambda a, b: a + b

print(add(10, 20))


# ==========================================
# EVEN OR ODD
# ==========================================

check_even = lambda number: number % 2 == 0

print(check_even(10))

print(check_even(7))


# ==========================================
# MULTIPLY
# ==========================================

multiply = lambda a, b: a * b

print(multiply(5, 6))