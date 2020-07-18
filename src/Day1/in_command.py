"""
In Command
Author: Will M
Date: 18.06.20

Use input() to take command of a new rocket.
"""

captain_name = input("What is your name? ")
mission_name = input("What is the mission called? ")
destination = input("What is our destination? ")
cargo = input("What is our cargo? ")
crew = input("How big is our crew? ")

print(f"Welcome aboard Captain {captain_name}.")
print(f"This is the H.M.S {mission_name} bound for {destination}.")
print(f"We are carrying {cargo} and have a crew of {crew}.")
print("Best of luck.")
