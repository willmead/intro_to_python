"""
Robot Greeter 1.0
Date: 28/03/20
Author: Will

The Robot Greeter ask questions of the
user and respond using the information
it receives.
"""

print("I am a Personal Robot Greeter")

name = input("What is your name?")
print(f"Hello {name}, have a great day!")

age = int(input("How old are you?"))
print(f"You are {age}, fantastic! Soon you will be {age + 1}.")

sport = input("What is your favourite sport?")
print(f"I like {sport} too!")
