"""
Dynamic Typing in Python

Python is dynamically typed.

This means:
- We don't need to declare a variable's type.
- The type is determined at runtime.
- A variable can refer to different types of values
  during the execution of a program.
"""


# Same variable with different data types

value = 10

print(value)
print(type(value))


value = "Python"

print(value)
print(type(value))


value = 10.5

print(value)
print(type(value))


value = True

print(value)
print(type(value))


# Another example

x = 100
print(x, type(x))

x = "Hello"
print(x, type(x))

x = [1, 2, 3]
print(x, type(x))


# Dynamic typing vs static typing

# Python:
x = 10
x = "Hello"

# This is allowed in Python.


# Note:
# Dynamic typing does NOT mean Python has no types.
# Python variables still refer to objects that have types.