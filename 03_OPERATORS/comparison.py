"""
COMPARISON OPERATORS

Comparison operators compare two values.

They always return:
True
or
False

Operators:

==   Equal to
!=   Not equal to
>    Greater than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
"""

a = 10
b = 20

# Equal to
print("a == b:", a == b)

# Not equal to
print("a != b:", a != b)

# Greater than
print("a > b:", a > b)

# Less than
print("a < b:", a < b)

# Greater than or equal to
print("a >= b:", a >= b)

# Less than or equal to
print("a <= b:", a <= b)


# ==========================================
# COMPARING EQUAL VALUES
# ==========================================

x = 10
y = 10

print(x == y)
print(x != y)


# ==========================================
# STRINGS
# ==========================================

name1 = "Python"
name2 = "Python"

print(name1 == name2)

print("Python" == "python")


# ==========================================
# LISTS
# ==========================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================

age = 21

print("Eligible:", age >= 18)


# Marks example

marks = 75

print("Passed:", marks >= 40)