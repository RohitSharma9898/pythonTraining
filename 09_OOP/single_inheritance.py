"""
SINGLE INHERITANCE

One parent class
        ↓
One child class
"""


class Parent:

    def show_parent(self):

        print("Parent class")


class Child(Parent):

    def show_child(self):

        print("Child class")


child = Child()

child.show_parent()
child.show_child()