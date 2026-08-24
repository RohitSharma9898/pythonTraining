"""
Dictionary Data Type

A dictionary stores data in:
KEY : VALUE

Dictionary is:
- Mutable
- Ordered (Python 3.7+)
- Keys must be unique
- Keys must be hashable
"""

# Creating dictionary

student = {
    "name": "Rohit",
    "age": 21,
    "course": "Python",
    "marks": 90
}

print(student)
print(type(student))


# ==============================
# ACCESSING VALUES
# ==============================

print(student["name"])
print(student["age"])


# get() method

print(student.get("name"))

print(student.get("city"))

# No error if key doesn't exist


# ==============================
# ADDING DATA
# ==============================

student["city"] = "Vadodara"

print(student)


# ==============================
# MODIFYING DATA
# ==============================

student["marks"] = 95

print(student)


# ==============================
# REMOVING DATA
# ==============================

student.pop("city")

print(student)


# ==============================
# DICTIONARY METHODS
# ==============================

print(student.keys())

print(student.values())

print(student.items())


# ==============================
# LOOP THROUGH DICTIONARY
# ==============================

for key in student:
    print(key)


for value in student.values():
    print(value)


for key, value in student.items():
    print(key, ":", value)


# ==============================
# NESTED DICTIONARY
# ==============================

students = {
    "student1": {
        "name": "Rohit",
        "marks": 90
    },

    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students)

print(students["student1"]["name"])
print(students["student1"]["marks"])


# ==============================
# CHECK KEY
# ==============================

print("name" in student)
print("city" in student)