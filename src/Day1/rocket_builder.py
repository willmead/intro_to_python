"""
Rocket Builder
Author: Will M
Date: 18.06.20

Use variables to store information about a new rocket.
"""

height = 60
width = 10
weight = 1000
power = 10

name = "Explorer"
destination = "Jupiter"
material = "Metal"
fuel = "Hydrogen"

is_manned = False
has_experiments = True
will_return = False
is_due = True

print(f"Height: {height}m")
print(f"Width: {width}m")
print(f"Weight: {weight}kg")
print(f"Power: {power} / 10")

print()

print(f"Name: {name}")
print(f"Destination: {destination}")
print(f"Material: {material}")
print(f"Fuel: {fuel}")

print()

print(f"Is the ship manned? {is_manned}")
print(f"Does the ship contain experiments? {has_experiments}")
print(f"Will the ship return to earth? {will_return}")
print(f"Is the ship due to launch? {is_due}")
