"""
List Data Type

A list is:
- Ordered
- Mutable
- Allows duplicate values
- Can store different data types
"""

# Creating a list

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(type(numbers))


# Different data types

student = ["Rohit", 21, 75.5, True]

print(student)


# Duplicate values

numbers = [10, 20, 10, 30, 10]

print(numbers)


# ==============================
# INDEXING
# ==============================

names = ["Rohit", "Rahul", "Aman", "Vikas"]

print(names[0])
print(names[1])
print(names[-1])


# ==============================
# SLICING
# ==============================

print(names[0:2])
print(names[:3])
print(names[2:])
print(names[::-1])


# ==============================
# MODIFYING LIST
# ==============================

names[0] = "Arjun"

print(names)


# ==============================
# ADDING ELEMENTS
# ==============================

names.append("Ravi")

print(names)


names.insert(1, "Karan")

print(names)


names.extend(["Mohit", "Amit"])

print(names)


# ==============================
# REMOVING ELEMENTS
# ==============================

names.remove("Amit")

print(names)


names.pop()

print(names)


# ==============================
# LIST METHODS
# ==============================

numbers = [5, 2, 8, 1, 9]

numbers.sort()

print(numbers)

numbers.reverse()

print(numbers)


# Length

print(len(numbers))


# Membership

print(5 in numbers)
print(100 in numbers)


# ==============================
# NESTED LIST
# ==============================

students = [
    ["Rohit", 90],
    ["Rahul", 85],
    ["Aman", 95]
]

print(students)

print(students[0])
print(students[0][0])
print(students[0][1])