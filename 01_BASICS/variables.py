"""
Variables in Python

A variable is a name used to store a value.

Python does not require us to declare the data type
of a variable explicitly.
"""

# Creating variables
name = "Rohit"
age = 21
height = 5.11
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# Checking the type
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# Assigning a new value
age = 22
print("Updated age:", age)


# Multiple assignment
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)


# Same value to multiple variables
x = y = z = 100

print(x, y, z)


# Variable naming examples
student_name = "Rahul"
student_age = 20

print(student_name)
print(student_age)


# Case-sensitive variables
name = "Rohit"
Name = "Rahul"

print(name)
print(Name)