"""
====================================================
                    SERIES
====================================================

A Series is a one-dimensional labeled data structure.

You can think of it as:

    A single column of data.
"""


import pandas as pd


# ==================================================
# CREATE SERIES
# ==================================================

marks = pd.Series(
    [85, 90, 75, 88]
)


print(marks)


# ==================================================
# ACCESS VALUES
# ==================================================

print(marks[0])

print(marks[2])


# ==================================================
# CUSTOM INDEX
# ==================================================

marks = pd.Series(
    [85, 90, 75],
    index=["Rohit", "Rahul", "Aman"]
)


print(marks)


print(marks["Rohit"])


# ==================================================
# SERIES FROM DICTIONARY
# ==================================================

student_marks = {

    "Rohit": 85,

    "Rahul": 90,

    "Aman": 75
}


marks = pd.Series(student_marks)


print(marks)