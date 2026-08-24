"""
RECURSION

A function calling itself is called recursion.

A recursive function should have
a stopping condition.
"""


# ==========================================
# COUNTDOWN
# ==========================================

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)


# ==========================================
# FACTORIAL
# ==========================================

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))


# ==========================================
# SUM OF NUMBERS
# ==========================================

def sum_numbers(number):

    if number == 0:
        return 0

    return number + sum_numbers(number - 1)


print(sum_numbers(5))