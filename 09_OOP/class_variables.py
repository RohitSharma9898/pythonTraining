"""
CLASS VARIABLE

A class variable is shared by all objects
of the class.
"""


class Student:

    college = "LTSU"

    def __init__(self, name):

        self.name = name


student1 = Student("Rohit")
student2 = Student("Rahul")


print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)


# Class variable can be accessed
# using the class name.

print(Student.college)