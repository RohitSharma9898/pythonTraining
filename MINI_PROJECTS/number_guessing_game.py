"""
====================================================
             NUMBER GUESSING GAME
====================================================

Concepts:

    random
    while loop
    if-elif-else
    input
"""


import random


secret_number = random.randint(1, 100)


attempts = 0


print("I have selected a number between 1 and 100.")


while True:

    guess = int(input("Guess the number: "))

    attempts += 1


    if guess < secret_number:

        print("Too low!")


    elif guess > secret_number:

        print("Too high!")


    else:

        print("Correct!")

        print("Attempts:", attempts)

        break