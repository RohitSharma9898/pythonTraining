"""
BASIC PYTHON PROBLEMS

Level 1: Beginner
"""

# --------------------------------------------------
# Problem 1
# Print "Hello Python"
# --------------------------------------------------

print("Hello Python")


# --------------------------------------------------
# Problem 2
# Store your name, age and city in variables
# and print them.
# --------------------------------------------------

name = "Rohit"
age = 21
city = "Vadodara"

print("Name:", name)
print("Age:", age)
print("City:", city)


# --------------------------------------------------
# Problem 3
# Take two numbers from the user and print their sum.
# --------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)


# --------------------------------------------------
# Problem 4
# Take length and width of a rectangle
# and calculate its area.
# --------------------------------------------------

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area:", area)


# --------------------------------------------------
# Problem 5
# Take a number and print its square and cube.
# --------------------------------------------------

number = int(input("Enter a number: "))

print("Square:", number ** 2)
print("Cube:", number ** 3)


# --------------------------------------------------
# Problem 6
# Take student's name and marks in three subjects.
# Calculate total and average.
# --------------------------------------------------

student_name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + python + english
average = total / 3

print("Student:", student_name)
print("Total:", total)
print("Average:", average)


# --------------------------------------------------
# Problem 7
# Convert Celsius temperature to Fahrenheit.
#
# Formula:
# Fahrenheit = (Celsius * 9/5) + 32
# --------------------------------------------------

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# --------------------------------------------------
# Problem 8
# Swap two numbers.
# --------------------------------------------------

a = 10
b = 20

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)


# --------------------------------------------------
# Problem 9
# Calculate simple interest.
#
# SI = (P * R * T) / 100
# --------------------------------------------------

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# --------------------------------------------------
# Problem 10
# Take user's name and age and print a sentence.
# --------------------------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")