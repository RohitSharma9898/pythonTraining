"""
super()

super() is used to access methods
or attributes of the parent class.
"""


class Parent:

    def __init__(self, name):

        self.name = name

    def show(self):

        print("Parent method")


class Child(Parent):

    def __init__(self, name, age):

        super().__init__(name)

        self.age = age

    def show(self):

        super().show()

        print("Child method")


child = Child("Rohit", 21)

print(child.name)
print(child.age)

child.show()