"""
====================================================
          FUNCTION AS AN ARGUMENT
====================================================

A decorator works because Python allows us
to pass a function to another function.
"""


def greet():

    print("Hello!")


def execute(function):

    print("Before function")

    function()

    print("After function")


execute(greet)


"""
Flow:

execute(greet)
      ↓
function = greet
      ↓
print Before
      ↓
greet()
      ↓
print After
"""