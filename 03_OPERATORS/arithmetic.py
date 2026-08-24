"""
ARITHMETIC OPERATORS IN PYTHON

Used to perform mathematical operations.

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Exponentiation
"""

a = 20
b = 6

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Floor Division
print("Floor Division:", a // b)

# Modulus - remainder
print("Modulus:", a % b)

# Exponentiation
print("Power:", a ** b)


# ==========================================
# INTEGER DIVISION VS FLOAT DIVISION
# ==========================================

print(10 / 3)
print(10 // 3)


# ==========================================
# NEGATIVE FLOOR DIVISION
# ==========================================

print(-10 // 3)

# Floor division rounds towards negative infinity.


# ==========================================
# OPERATOR PRECEDENCE
# ==========================================

result = 10 + 5 * 2

print("Result:", result)

# Multiplication happens before addition.


# Using parentheses

result = (10 + 5) * 2

print("Result:", result)


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================

price = 500
quantity = 3

total = price * quantity

print("Total price:", total)


# ==========================================
# SIMPLE INTEREST
# ==========================================

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)