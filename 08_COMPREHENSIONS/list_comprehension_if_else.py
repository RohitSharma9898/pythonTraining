"""
LIST COMPREHENSION WITH IF-ELSE

Syntax:

[expression_if_true if condition else expression_if_false
 for item in iterable]
"""


# ==========================================
# EVEN / ODD
# ==========================================

numbers = [1, 2, 3, 4, 5, 6]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)


# ==========================================
# PASS / FAIL
# ==========================================

marks = [90, 35, 78, 20, 60]

result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print(result)


# ==========================================
# POSITIVE / NEGATIVE
# ==========================================

numbers = [-5, 10, -3, 20, 0]

result = [
    "Positive" if number > 0 else "Not Positive"
    for number in numbers
]

print(result)


# ==========================================
# ADULT / MINOR
# ==========================================

ages = [12, 18, 25, 15, 30]

result = [
    "Adult" if age >= 18 else "Minor"
    for age in ages
]

print(result)