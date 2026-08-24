"""
LOCAL VARIABLES

A variable created inside a function
is normally a local variable.
"""


def student():

    name = "Rohit"
    age = 21

    print("Name:", name)
    print("Age:", age)


student()


# ==========================================
# LOCAL VARIABLE CANNOT BE USED OUTSIDE
# ==========================================

def calculate():

    result = 10 + 20

    print(result)


calculate()


# This would cause an error:

# print(result)


# ==========================================
# EACH FUNCTION HAS ITS OWN LOCAL SCOPE
# ==========================================

def first():

    number = 10
    print(number)


def second():

    number = 20
    print(number)


first()
second()