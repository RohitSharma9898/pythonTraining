"""
====================================================
             *args AND **kwargs
====================================================

Using *args and **kwargs allows our decorator
to work with functions having different
numbers of arguments.
"""


def my_decorator(function):


    def wrapper(*args, **kwargs):

        print("Function is starting...")


        result = function(*args, **kwargs)


        print("Function is finished.")


        return result


    return wrapper


# ==================================================
# FUNCTION 1
# ==================================================

@my_decorator
def greet(name):

    print("Hello", name)


greet("Rohit")


# ==================================================
# FUNCTION 2
# ==================================================

@my_decorator
def add(a, b):

    return a + b


result = add(10, 20)


print("Result:", result)


"""
The same decorator works with:

greet(name)

and:

add(a, b)
"""