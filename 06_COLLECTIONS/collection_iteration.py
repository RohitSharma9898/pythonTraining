"""
ITERATING THROUGH COLLECTIONS
"""

# ==========================================
# LIST
# ==========================================

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ==========================================
# TUPLE
# ==========================================

numbers = (10, 20, 30)

for number in numbers:
    print(number)


# ==========================================
# SET
# ==========================================

numbers = {10, 20, 30}

for number in numbers:
    print(number)


# ==========================================
# DICTIONARY - KEYS
# ==========================================

student = {
    "name": "Rohit",
    "age": 21,
    "marks": 90
}

for key in student:
    print(key)


# ==========================================
# DICTIONARY - VALUES
# ==========================================

for value in student.values():
    print(value)


# ==========================================
# DICTIONARY - KEY AND VALUE
# ==========================================

for key, value in student.items():
    print(key, ":", value)


# ==========================================
# LIST WITH INDEX
# ==========================================

students = ["Rohit", "Rahul", "Aman"]

for index, name in enumerate(students):
    print(index, name)