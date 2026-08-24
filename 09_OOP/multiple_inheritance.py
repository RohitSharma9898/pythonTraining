"""
MULTIPLE INHERITANCE

One child class inherits from
multiple parent classes.
"""


class Father:

    def father_property(self):

        print("Father property")


class Mother:

    def mother_property(self):

        print("Mother property")


class Child(Father, Mother):

    def child_property(self):

        print("Child property")


child = Child()

child.father_property()
child.mother_property()
child.child_property()