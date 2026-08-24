"""
====================================================
                     zip()
====================================================

zip() combines elements from multiple
iterables based on their positions.
"""


names = [
    "Rohit",
    "Rahul",
    "Aman"
]


marks = [
    85,
    90,
    75
]


students = zip(names, marks)


print(list(students))


"""
Output:

[
    ("Rohit", 85),
    ("Rahul", 90),
    ("Aman", 75)
]
"""


# ==================================================
# PRACTICAL EXAMPLE
# ==================================================

for name, mark in zip(names, marks):

    print(name, "scored", mark)