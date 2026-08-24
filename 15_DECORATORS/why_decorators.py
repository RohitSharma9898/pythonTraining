"""
====================================================
                  WHY DECORATORS?
====================================================

Suppose we already have a function:

    login()

Now we want to add extra functionality:

    - Check whether user is logged in
    - Print when the function starts
    - Print when the function finishes
    - Measure execution time
    - Check permissions

We could modify login() every time.

But this is not a good approach.

Instead, we can add extra functionality
WITHOUT changing the original function.

This is where DECORATORS are useful.
"""


# ==================================================
# ORIGINAL FUNCTION
# ==================================================

def greet():

    print("Hello, Rohit!")


# ==================================================
# EXTRA FUNCTIONALITY
# ==================================================

def before_greet():

    print("Checking user...")


# We would like to add before_greet()
# before greet().

before_greet()

greet()


"""
A decorator allows us to do this
automatically.
"""