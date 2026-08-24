"""
Python Numeric Data Types

1. int      -> Integer numbers
2. float    -> Decimal numbers
3. complex  -> Complex numbers
"""

# ==============================
# 1. INTEGER (int)
# ==============================

age = 21
marks = 95
negative_number = -50

print(age)
print(type(age))

print(marks)
print(type(marks))

print(negative_number)
print(type(negative_number))


# Large integers are also supported
population = 1_400_000_000

print(population)
print(type(population))


# ==============================
# 2. FLOAT
# ==============================

height = 5.11
price = 99.99
temperature = -10.5

print(height)
print(type(height))

print(price)
print(type(price))

print(temperature)
print(type(temperature))


# Scientific notation
number = 2.5e3

print(number)
print(type(number))


# ==============================
# 3. COMPLEX
# ==============================

z = 3 + 4j

print(z)
print(type(z))

# Real part
print("Real part:", z.real)

# Imaginary part
print("Imaginary part:", z.imag)


# Complex number operations

z1 = 2 + 3j
z2 = 4 + 5j

print("Addition:", z1 + z2)
print("Subtraction:", z1 - z2)
print("Multiplication:", z1 * z2)


# ==============================
# TYPE CONVERSION
# ==============================

number = 10

print(float(number))

decimal = 10.5

print(int(decimal))

# Complex conversion
number = 5

print(complex(number))