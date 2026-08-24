"""
CONTINUE STATEMENT

continue skips the current iteration
and moves to the next iteration.
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# 5 will not be printed.


# ==========================================
# PRINT ONLY ODD NUMBERS
# ==========================================

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)


# ==========================================
# SKIP NEGATIVE NUMBERS
# ==========================================

numbers = [10, -5, 20, -3, 30]

for number in numbers:

    if number < 0:
        continue

    print(number)


# ==========================================
# SKIP MULTIPLE OF 3
# ==========================================

for i in range(1, 21):

    if i % 3 == 0:
        continue

    print(i)