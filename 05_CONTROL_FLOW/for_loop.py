"""
FOR LOOP

A for loop is used to repeat a block of code
for each item in a sequence or iterable.

Syntax:

for variable in sequence:
    statement
"""

# ==========================================
# BASIC LOOP
# ==========================================

for i in range(5):
    print(i)


# ==========================================
# PRINT 1 TO 10
# ==========================================

for i in range(1, 11):
    print(i)


# ==========================================
# PRINT EVEN NUMBERS
# ==========================================

for i in range(2, 11, 2):
    print(i)


# ==========================================
# PRINT ODD NUMBERS
# ==========================================

for i in range(1, 11, 2):
    print(i)


# ==========================================
# LOOP THROUGH STRING
# ==========================================

name = "Python"

for character in name:
    print(character)


# ==========================================
# LOOP THROUGH LIST
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# ==========================================
# SUM OF NUMBERS
# ==========================================

total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)


# ==========================================
# MULTIPLICATION TABLE
# ==========================================

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
