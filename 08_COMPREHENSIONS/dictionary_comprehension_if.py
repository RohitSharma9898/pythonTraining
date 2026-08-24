"""
DICTIONARY COMPREHENSION WITH IF
"""


# ==========================================
# EVEN NUMBERS ONLY
# ==========================================

numbers = range(1, 11)

result = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(result)


# ==========================================
# NUMBERS GREATER THAN 5
# ==========================================

numbers = range(1, 11)

result = {
    number: number * 10
    for number in numbers
    if number > 5
}

print(result)


# ==========================================
# STUDENTS WHO PASSED
# ==========================================

students = {
    "Rohit": 90,
    "Rahul": 35,
    "Aman": 80,
    "Vijay": 25
}

passed_students = {
    name: marks
    for name, marks in students.items()
    if marks >= 40
}

print(passed_students)


# ==========================================
# STUDENTS WITH MARKS >= 80
# ==========================================

top_students = {
    name: marks
    for name, marks in students.items()
    if marks >= 80
}

print(top_students)