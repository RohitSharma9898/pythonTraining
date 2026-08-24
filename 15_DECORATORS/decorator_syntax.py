"""
====================================================
              DECORATOR SYNTAX
====================================================

Instead of writing:

greet = my_decorator(greet)

Python allows:

@my_decorator
def greet():
    ...
"""


def my_decorator(function):


    def wrapper():

        print("Before function")

        function()

        print("After function")


    return wrapper


@my_decorator
def greet():

    print("Hello, Python!")


greet()


"""
These two are equivalent:

@my_decorator
def greet():
    ...


AND:


def greet():
    ...

greet = my_decorator(greet)
"""