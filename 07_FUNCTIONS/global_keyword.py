"""
GLOBAL KEYWORD

global allows us to modify a global variable
inside a function.
"""


count = 0


def increase_count():

    global count

    count = count + 1


increase_count()
increase_count()
increase_count()

print(count)


# ==========================================
# WITHOUT GLOBAL
# ==========================================

number = 10


def change_number():

    # This creates a local variable
    # instead of modifying the global one.

    number = 20

    print("Inside:", number)


change_number()

print("Outside:", number)