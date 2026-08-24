"""
VARIABLE SCOPE

Scope tells us where a variable can be accessed.

Main scopes:

1. Local
2. Global
"""


# ==========================================
# GLOBAL VARIABLE
# ==========================================

name = "Rohit"


def show_name():

    print(name)


show_name()

print(name)


# ==========================================
# LOCAL VARIABLE
# ==========================================

def student():

    age = 21

    print(age)


student()


# This will cause an error:

# print(age)

# Because age exists only inside the function.


# ==========================================
# SAME VARIABLE NAME
# ==========================================

x = 10


def example():

    x = 20

    print("Inside:", x)


example()

print("Outside:", x)