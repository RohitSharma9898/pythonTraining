"""
@property

@property allows us to access a method
like an attribute.
"""


class Student:

    def __init__(self, name, marks):

        self.name = name
        self._marks = marks

    @property
    def marks(self):

        return self._marks

    @marks.setter
    def marks(self, value):

        if value >= 0 and value <= 100:

            self._marks = value

        else:

            print("Invalid marks")


student = Student("Rohit", 90)

print(student.marks)


student.marks = 95

print(student.marks)


student.marks = 150