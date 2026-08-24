"""
HIGHER-ORDER FUNCTION

A function that:
- takes another function as an argument
OR
- returns another function

is called a higher-order function.
"""


# ==========================================
# FUNCTION AS ARGUMENT
# ==========================================

def square(number):

    return number * number


def calculate(function, number):

    return function(number)


result = calculate(square, 5)

print(result)


# ==========================================
# USING LAMBDA
# ==========================================

result = calculate(
    lambda x: x * 2,
    10
)

print(result)


# ==========================================
# RETURNING A FUNCTION
# ==========================================

def create_greeting():

    def greeting():

        print("Hello Python!")

    return greeting


message = create_greeting()

message()