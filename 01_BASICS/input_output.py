"""
Input and Output in Python

input()  -> takes input from the user
print()  -> displays output
"""

# Output
print("Hello World!")
print("Welcome to Python")


# Taking input
name = input("Enter your name: ")

print("Hello", name)


# Input always returns a string
age = input("Enter your age: ")

print("Age:", age)
print("Type:", type(age))


# Converting input into integer
age = int(input("Enter your age: "))

print("Your age is:", age)
print("Type:", type(age))


# Taking multiple inputs
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print("Full Name:", first_name, last_name)


# Taking numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)


# print() with separator
print("Python", "Java", "C++", sep=" | ")


# print() with end
print("Hello", end=" ")
print("World")


# Formatted output
name = "Rohit"
age = 21

print(f"My name is {name} and I am {age} years old.")