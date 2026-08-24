"""
====================================================
             MULTIPLE DECORATORS
====================================================

A function can have more than one decorator.
"""


def first(function):


    def wrapper():

        print("First decorator - before")

        function()

        print("First decorator - after")


    return wrapper


def second(function):


    def wrapper():

        print("Second decorator - before")

        function()

        print("Second decorator - after")


    return wrapper


@first
@second
def greet():

    print("Hello!")


greet()


"""
Execution:

first
  ↓
second
  ↓
greet()
"""