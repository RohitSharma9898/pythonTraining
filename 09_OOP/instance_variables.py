"""
INSTANCE VARIABLES

Instance variables belong to individual objects.

Usually created using self.
"""


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student1 = Student("Rohit", 21)

student2 = Student("Rahul", 22)


print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# Each object has its own values.

student1.age = 25

print(student1.age)
print(student2.age)