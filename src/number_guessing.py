"""
Number Guessing Game
Date: 28/03/20
Author: Will

The computer chooses a random number and the
user has to guess it. They only have a certain
number of guesses!
"""

import random

# Computer chooses a random number
number = random.randint(1,100)

# The number of guesses the user can make
num_guesses = 7

# Introduction
print(f"I have chosen a number between 1 and 100.")
print(f"You have {num_guesses} chances to guess it.")

# Game Loop
for go in range(num_guesses):
    print(f"You have {num_guesses - go} guesses left.")

    guess = int(input('What is your guess? '))

    if guess > number:
        print("Too Big!")
    elif guess < number:
        print("Too Small!")
    else:
        print(f"That's right! The number was {number}!")
        break # If the user is correct we leave the loop
