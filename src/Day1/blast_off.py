"""
Blast Off
Author: Will M
Date: 18.06.20

Use informations to create a warning system for a launching rocket.
"""

thrust = 7
temperature = 100
fuel = 4
direction = 90
acceleration = 10

if thrust > 7:
    print("Too Fast!")
elif thrust < 4:
    print("Too Slow!")
else:
    print("Thrust Good.")

if temperature > 200:
    print("Too Hot!")
elif temperature < 50:
    print("Too Cold!")
else:
    print("Temperature Good.")

if fuel > 5:
    print("Fuel Good")
else:
    print("Not Enough Fuel.")

if direction > 110:
    print("Leaning right!")
elif direction < 70:
    print("Leaning left!")
else:
    print("Direction Good.")

if acceleration > 6:
    print("Too Much Acceleration")
else:
    print("Acceleration Good.")
