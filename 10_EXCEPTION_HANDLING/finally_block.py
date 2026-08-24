"""
FINALLY

finally always executes,
whether an exception occurs or not.

It is commonly used for cleanup.
"""


# ==========================================
# EXCEPTION OCCURS
# ==========================================

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("Finally block executed")


# ==========================================
# NO EXCEPTION
# ==========================================

try:

    number = 10 / 2

    print(number)

except:

    print("Error")

finally:

    print("Program finished")