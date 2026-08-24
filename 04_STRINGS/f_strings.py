"""
F-STRINGS

F-strings provide a simple way to format strings.

Syntax:

f"Text {variable}"
"""

name = "Rohit"
age = 21
course = "Python"


# ==========================================
# BASIC F-STRING
# ==========================================

print(f"My name is {name}.")

print(f"I am {age} years old.")

print(f"I am learning {course}.")


# Multiple variables

print(f"My name is {name}, I am {age} years old and I am learning {course}.")


# ==========================================
# EXPRESSIONS INSIDE F-STRING
# ==========================================

a = 10
b = 20

print(f"Sum = {a + b}")

print(f"Product = {a * b}")


# ==========================================
# FUNCTION CALL
# ==========================================

name = "rohit"

print(f"Uppercase name: {name.upper()}")


# ==========================================
# FORMATTING DECIMAL VALUES
# ==========================================

price = 99.9999

print(f"Price: {price:.2f}")


# ==========================================
# PERCENTAGE
# ==========================================

percentage = 0.8567

print(f"Percentage: {percentage:.2%}")


# ==========================================
# ALIGNMENT
# ==========================================

name = "Python"

print(f"{name:<20}")

print(f"{name:>20}")

print(f"{name:^20}")


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================

student = "Rohit"
maths = 90
python_marks = 95
english = 85

total = maths + python_marks + english
average = total / 3

print(f"""
Student: {student}
Maths: {maths}
Python: {python_marks}
English: {english}
Total: {total}
Average: {average:.2f}
""")