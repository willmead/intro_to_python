"""
Collatz Conjecture
Date: 02/04/20
Author: Will

A function to visualise the Collatz Conjecture.
Good Numbers include: 9, 12, 19, 27, 97, 871

Steps not necessary upon first write up.
"""

import time

def collatz_steps(number):
    steps = 0

    while number != 1:
        steps += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        print("=" * int(number))
        time.sleep(0.1)

    print(f"Steps: {steps}")

collatz_steps(97)
