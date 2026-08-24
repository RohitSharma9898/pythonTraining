"""
RETURN STATEMENT

return sends a value back from a function.

The returned value can be stored in a variable
and used later.
"""


# ==========================================
# BASIC RETURN
# ==========================================

def add(a, b):

    return a + b


result = add(10, 20)

print(result)


# ==========================================
# RETURN MULTIPLICATION
# ==========================================

def multiply(a, b):

    return a * b


result = multiply(5, 4)

print("Result:", result)


# ==========================================
# RETURN SQUARE
# ==========================================

def square(number):

    return number * number


result = square(6)

print("Square:", result)


# ==========================================
# RETURN AND USE IN EXPRESSION
# ==========================================

def add(a, b):

    return a + b


result = add(10, 20) * 2

print(result)


# ==========================================
# MULTIPLE RETURN VALUES
# ==========================================

def calculate(a, b):

    total = a + b
    difference = a - b

    return total, difference


sum_result, difference_result = calculate(20, 10)

print("Sum:", sum_result)
print("Difference:", difference_result)


# ==========================================
# RETURN STOPS FUNCTION
# ==========================================

def check_number(number):

    if number > 0:
        return "Positive"

    return "Zero or Negative"


print(check_number(10))
print(check_number(-5))