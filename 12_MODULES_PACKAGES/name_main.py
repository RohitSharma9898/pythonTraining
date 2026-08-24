"""
__name__ AND __main__
"""


def greet():

    print("Hello, Python!")


print("Module name:", __name__)


if __name__ == "__main__":

    print("This file is being run directly.")

    greet()