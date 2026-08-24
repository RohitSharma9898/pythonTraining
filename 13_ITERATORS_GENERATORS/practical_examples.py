"""
PRACTICAL GENERATOR EXAMPLES
"""


# ==========================================
# EXAMPLE 1: EVEN NUMBERS
# ==========================================

def even_numbers(limit):

    for number in range(1, limit + 1):

        if number % 2 == 0:

            yield number


for number in even_numbers(10):

    print(number)


# ==========================================
# EXAMPLE 2: COUNTDOWN
# ==========================================

def countdown(number):

    while number > 0:

        yield number

        number -= 1


for number in countdown(5):

    print(number)


# ==========================================
# EXAMPLE 3: LARGE DATA
# ==========================================

def generate_numbers():

    number = 1

    while number <= 1000000:

        yield number

        number += 1


numbers = generate_numbers()


# We don't need to create a list
# containing one million numbers.

print(next(numbers))
print(next(numbers))
print(next(numbers))