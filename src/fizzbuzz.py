"""
Fizz Buzz Game
Date: 28/03/20
Author: Will

A fizzbuzz game for learning how for loops work
in conjuction with conditional statements.
"""

for number in range(0, 100):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
