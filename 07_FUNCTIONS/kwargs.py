"""
**kwargs

**kwargs allows a function to accept
any number of keyword arguments.

The arguments are received as a dictionary.
"""


# ==========================================
# BASIC EXAMPLE
# ==========================================

def student_details(**details):

    print(details)


student_details(
    name="Rohit",
    age=21,
    course="Python"
)


# ==========================================
# ACCESSING VALUES
# ==========================================

def student(**details):

    print("Name:", details.get("name"))
    print("Age:", details.get("age"))


student(name="Rohit", age=21)


# ==========================================
# LOOP THROUGH **kwargs
# ==========================================

def show_details(**details):

    for key, value in details.items():

        print(key, ":", value)


show_details(
    name="Rohit",
    age=21,
    city="Vadodara",
    course="Python"
)


# ==========================================
# **kwargs IS A DICTIONARY
# ==========================================

def show(**data):

    print(data)
    print(type(data))


show(name="Rohit", age=21)