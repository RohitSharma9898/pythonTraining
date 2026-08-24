"""
====================================================
                    functools.wraps
====================================================

When we decorate a function, Python can lose
some information about the original function.

functools.wraps helps preserve it.
"""

from functools import wraps


def my_decorator(function):


    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result


    return wrapper


@my_decorator
def greet(name):

    """
    Greets a user.
    """

    print("Hello", name)


greet("Rohit")


print("Function name:", greet.__name__)

print("Documentation:", greet.__doc__)