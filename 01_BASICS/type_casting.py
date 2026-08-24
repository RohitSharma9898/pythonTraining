"""
Type Casting

Type casting means converting one data type into another.
"""

# String to integer
age = "21"

print(age)
print(type(age))

age = int(age)

print(age)
print(type(age))


# Integer to float
number = 10

result = float(number)

print(result)
print(type(result))


# Integer to string
number = 100

text = str(number)

print(text)
print(type(text))


# Float to integer
price = 99.99

value = int(price)

print(value)
print(type(value))


# String to float
number = "25.5"

number = float(number)

print(number)
print(type(number))


# Integer to boolean
print(bool(0))
print(bool(1))
print(bool(10))


# String to boolean
print(bool(""))
print(bool("Hello"))


# Important example with input

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert strings to integers
num1 = int(num1)
num2 = int(num2)

print("Sum:", num1 + num2)