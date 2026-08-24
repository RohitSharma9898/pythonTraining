"""
FUNCTION BASICS

A function is a reusable block of code.

We create a function using the def keyword.

Syntax:

def function_name():
    statements

To execute the function:

function_name()
"""


# ==========================================
# SIMPLE FUNCTION
# ==========================================

def greet():
    print("Hello, welcome to Python!")


greet()


# ==========================================
# FUNCTION CALLED MULTIPLE TIMES
# ==========================================

def welcome():
    print("Welcome to the class!")


welcome()
welcome()
welcome()


# ==========================================
# FUNCTION WITH MULTIPLE STATEMENTS
# ==========================================

def introduction():
    print("My name is Rohit.")
    print("I am learning Python.")
    print("Python is easy to learn.")


introduction()


# ==========================================
# FUNCTION WITH ONE PARAMETER
# ==========================================

def greet_student(name):
    print("Hello", name)


greet_student("Rohit")
greet_student("Rahul")


# ==========================================
# FUNCTION WITH TWO PARAMETERS
# ==========================================

def add(a, b):
    print("Sum:", a + b)


add(10, 20)
add(50, 30)


# ==========================================
# FUNCTION WITH USER INPUT
# ==========================================

def square(number):
    print("Square:", number * number)


number = int(input("Enter a number: "))

square(number)