"""
====================================================
                   RECURSION
====================================================

Recursion means a function calls itself.

A recursive function needs:

    1. Base condition
    2. Recursive call
"""


# ==================================================
# COUNTDOWN
# ==================================================

def countdown(number):

    # Base condition

    if number == 0:

        print("Done!")

        return


    print(number)


    # Recursive call

    countdown(number - 1)


countdown(5)


"""
Flow:

countdown(5)
    ↓
countdown(4)
    ↓
countdown(3)
    ↓
countdown(2)
    ↓
countdown(1)
    ↓
countdown(0)
    ↓
Done!
"""


# ==================================================
# FACTORIAL
# ==================================================

def factorial(number):

    if number == 0:

        return 1

    return number * factorial(number - 1)


print(factorial(5))