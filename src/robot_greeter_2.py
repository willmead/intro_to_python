"""
Robot Greeter 2.0
Date: 28/03/20
Author: Will

The Robot Greeter 2.0 will ask questions of the user
and react differently depending on the response it receives.
"""

print("I am a Personal Robot Greeter 2.0")

# Name
name = input("What is your name?")
print(f"Hello {name}, have a great day!")

# Age
age = int(input(f"How old are you {name}?"))
if age > 10:
    print(f"You are {age}, that means you're old!")
else:
    print(f"You are {age}, that is quite young!")

# Happy or Sad
mood = input(f"{name}, are you happy or sad at the moment?")
if mood == "happy":
    print("Great! I am happy too!")
else:
    print("Oh dear, I hope you feel better soon!")

# Coffee?
coffee = input(f"Would you like some coffee, {name}?")
if coffee == "yes":
    print("Coming right up!")
elif coffee == "no":
    print("Eurgh, coffee is for grown ups.")
else:
    print("I'm sorry I didn't quite get that.")
