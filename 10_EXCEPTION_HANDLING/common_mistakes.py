"""
COMMON EXCEPTION HANDLING MISTAKES
"""


# ==========================================
# MISTAKE 1
# ==========================================

"""
Do not blindly use:

except:

It hides the actual error.
"""


# Bad:

try:

    number = 10 / 0

except:

    print("Error")


# Better:

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")


# ==========================================
# MISTAKE 2
# ==========================================

"""
Do not put unnecessary code inside try.
"""


# Better:

try:

    number = int(input("Enter number: "))

except ValueError:

    print("Invalid number")


# ==========================================
# MISTAKE 3
# ==========================================

"""
Do not use exceptions for normal program flow
when a simple condition is better.
"""