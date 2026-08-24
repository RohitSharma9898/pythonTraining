"""
INHERITANCE

Inheritance allows one class to acquire
properties and methods of another class.
"""


class Animal:

    def eat(self):

        print("Animal is eating")


class Dog(Animal):

    def bark(self):

        print("Dog is barking")


dog = Dog()

dog.eat()

dog.bark()