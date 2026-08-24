"""
DICTIONARY OPERATIONS

Dictionary stores data as:

key : value
"""

student = {
    "name": "Rohit",
    "age": 21,
    "marks": 90
}


# ==========================================
# ACCESSING VALUES
# ==========================================

print(student["name"])
print(student["marks"])


# ==========================================
# GET
# ==========================================

print(student.get("name"))

print(student.get("city"))

# No error if key doesn't exist.


# ==========================================
# ADDING KEY-VALUE
# ==========================================

student["city"] = "Vadodara"

print(student)


# ==========================================
# MODIFYING VALUE
# ==========================================

student["marks"] = 95

print(student)


# ==========================================
# DELETE
# ==========================================

del student["city"]

print(student)


# ==========================================
# MEMBERSHIP
# ==========================================

print("name" in student)

print("city" not in student)


# ==========================================
# LENGTH
# ==========================================

print(len(student))