"""
====================================================
                BASIC DECORATOR
====================================================

A decorator is a function that takes another
function and adds extra functionality to it.
"""


def my_decorator(function):


    def wrapper():

        print("Before function")


        function()


        print("After function")


    return wrapper


# ==================================================
# ORIGINAL FUNCTION
# ==================================================

def greet():

    print("Hello, Rohit!")


# Apply decorator manually

greet = my_decorator(greet)


# Call function

greet()


"""
OUTPUT:

Before function
Hello, Rohit!
After function
"""