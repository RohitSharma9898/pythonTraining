"""
====================================================
        DECORATOR WITH FUNCTION ARGUMENTS
====================================================
"""


def my_decorator(function):


    def wrapper(name):

        print("Before function")

        function(name)

        print("After function")


    return wrapper


@my_decorator
def greet(name):

    print("Hello", name)


greet("Rohit")