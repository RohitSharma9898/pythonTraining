"""
RANDOM MODULE

Used to generate random values.
"""

import random


# Random integer

number = random.randint(1, 10)

print("Random number:", number)


# Random choice

names = [
    "Rohit",
    "Rahul",
    "Aman",
    "Priya"
]

student = random.choice(names)

print("Selected student:", student)


# Shuffle a list

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print("Shuffled list:", numbers)