"""
ABSTRACT CLASS

Python provides abstraction using
the abc module.

ABC = Abstract Base Class
"""


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass


class Dog(Animal):

    def sound(self):

        print("Dog barks")


dog = Dog()

dog.sound()


# We cannot directly create an object
# of the abstract class.

# animal = Animal()