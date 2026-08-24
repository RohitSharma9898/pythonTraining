"""
NESTED COLLECTIONS

A collection inside another collection.
"""

# ==========================================
# LIST INSIDE LIST
# ==========================================

students = [
    ["Rohit", 90],
    ["Rahul", 85],
    ["Aman", 95]
]

print(students)

print(students[0])

print(students[0][0])

print(students[0][1])


# ==========================================
# DICTIONARY INSIDE LIST
# ==========================================

students = [
    {
        "name": "Rohit",
        "marks": 90
    },
    {
        "name": "Rahul",
        "marks": 85
    },
    {
        "name": "Aman",
        "marks": 95
    }
]

print(students)

print(students[0]["name"])
print(students[0]["marks"])


# ==========================================
# LIST INSIDE DICTIONARY
# ==========================================

student = {
    "name": "Rohit",
    "subjects": ["Python", "Java", "SQL"]
}

print(student)

print(student["subjects"])

print(student["subjects"][0])


# ==========================================
# DICTIONARY INSIDE DICTIONARY
# ==========================================

college = {
    "student1": {
        "name": "Rohit",
        "marks": 90
    },

    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(college)

print(college["student1"]["name"])
print(college["student2"]["marks"])