"""
====================================================
                    filter()
====================================================

filter() selects elements based on
a condition.

Syntax:

filter(function, iterable)

The function should return:

True  -> keep the value
False -> remove the value
"""


numbers = [1, 2, 3, 4, 5, 6]


# ==================================================
# WITHOUT filter()
# ==================================================

even_numbers = []

for number in numbers:

    if number % 2 == 0:

        even_numbers.append(number)


print(even_numbers)


# ==================================================
# WITH filter()
# ==================================================

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)


print(list(even_numbers))


# ==================================================
# FILTER PASSING STUDENTS
# ==================================================

marks = [35, 80, 45, 90, 25, 70]


passing_marks = filter(
    lambda mark: mark >= 40,
    marks
)


print(list(passing_marks))