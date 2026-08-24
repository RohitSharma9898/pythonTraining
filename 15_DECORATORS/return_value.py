"""
====================================================
           DECORATOR WITH RETURN VALUE
====================================================
"""


def my_decorator(function):


    def wrapper(*args, **kwargs):

        print("Calling function...")


        result = function(*args, **kwargs)


        print("Function completed.")


        return result


    return wrapper


@my_decorator
def multiply(a, b):

    return a * b


result = multiply(5, 4)


print("Result:", result)