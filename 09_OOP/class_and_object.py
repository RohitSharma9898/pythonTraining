"""
CLASS AND OBJECT

Class:
    A blueprint for creating objects.

Object:
    An instance of a class.
"""


# ==========================================
# CREATING A CLASS
# ==========================================

class Student:

    def study(self):
        print("Student is studying")


# ==========================================
# CREATING OBJECT
# ==========================================

student1 = Student()

student1.study()


# ==========================================
# MULTIPLE OBJECTS
# ==========================================

student2 = Student()
student3 = Student()

student2.study()
student3.study()


# ==========================================
# SIMPLE REAL-LIFE EXAMPLE
# ==========================================

class Car:

    def drive(self):
        print("Car is driving")

    def stop(self):
        print("Car stopped")


car1 = Car()

car1.drive()
car1.stop()