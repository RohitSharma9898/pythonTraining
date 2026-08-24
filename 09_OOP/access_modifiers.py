"""
ACCESS MODIFIERS

Python uses naming conventions:

public:
    variable

protected:
    _variable

private:
    __variable
"""


class Student:

    def __init__(self):

        self.name = "Rohit"        # Public
        self._age = 21             # Protected
        self.__marks = 90          # Private


student = Student()


# Public

print(student.name)


# Protected

print(student._age)


# Private

# print(student.__marks)

# This causes an AttributeError.


# Private data can be accessed through
# name mangling, but it is generally
# not recommended.

print(student._Student__marks)