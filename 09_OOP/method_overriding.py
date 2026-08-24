"""
METHOD OVERRIDING

When a child class provides its own
implementation of a parent method.
"""


class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        print("Dog barks")


animal = Animal()

animal.sound()


dog = Dog()

dog.sound()