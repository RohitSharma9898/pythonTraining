"""
STRING FORMATTING

Different ways to insert values into strings.

1. Concatenation
2. % formatting
3. format()
4. f-string
"""

name = "Rohit"
age = 21
marks = 90.5


# ==========================================
# 1. CONCATENATION
# ==========================================

message = "My name is " + name + " and I am " + str(age) + " years old."

print(message)


# ==========================================
# 2. % FORMATTING
# ==========================================

message = "My name is %s and I am %d years old."

print(message % (name, age))


# Float

print("My marks are %.2f" % marks)


# ==========================================
# 3. format() METHOD
# ==========================================

message = "My name is {} and I am {} years old."

print(message.format(name, age))


# Positional placeholders

message = "{} scored {} marks."

print(message.format(name, marks))


# ==========================================
# INDEXED PLACEHOLDERS
# ==========================================

message = "{0} scored {1} marks."

print(message.format(name, marks))


# Change order

message = "{1} marks were scored by {0}."

print(message.format(name, marks))


# ==========================================
# NAMED PLACEHOLDERS
# ==========================================

message = "Name: {name}, Age: {age}"

print(message.format(name=name, age=age))


# ==========================================
# NUMBER FORMATTING
# ==========================================

price = 1234567.456

print("{:.2f}".format(price))


# Comma formatting

number = 1000000

print("{:,}".format(number))


# Percentage

percentage = 0.75

print("{:.2%}".format(percentage))