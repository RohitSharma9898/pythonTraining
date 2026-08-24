"""
NESTED LOOP

A loop inside another loop
is called a nested loop.
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

for i in range(1, 4):

    for j in range(1, 4):
        print("i =", i, "j =", j)


# ==========================================
# STAR PATTERN
# ==========================================

for i in range(1, 6):

    for j in range(i):
        print("*", end="")

    print()


# ==========================================
# NUMBER PATTERN
# ==========================================

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    print()


# ==========================================
# MULTIPLICATION TABLES
# ==========================================

for i in range(1, 6):

    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()


# ==========================================
# LIST INSIDE LIST
# ==========================================

students = [
    ["Rohit", 90],
    ["Rahul", 85],
    ["Aman", 95]
]

for student in students:

    for value in student:
        print(value)

    print()