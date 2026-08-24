"""
====================================================
                 INNER FUNCTION
====================================================

A function can be created inside another function.
"""


def outer():

    print("Outer function")


    def inner():

        print("Inner function")


    inner()


outer()


"""
Decorators commonly use:

    Outer function
        ↓
    Inner function
        ↓
    Original function
"""