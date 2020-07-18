import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()

first_letter = random.choice(alphabet)
second_letter = random.choice(alphabet)
number = random.randint(100, 999)

print(f"{first_letter}{second_letter}{number}")
