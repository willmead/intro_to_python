"""
Character Creator 2.0
Date: 28/03/20
Author: Will
"""

class Character():

    def __init__(self, name, health, experience):
        self.name = name
        self.health = health
        self.experience = experience

    def status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Experience: {self.experience} ")


player1 = Character('Grog', 100, 50)
player2 = Character('Melissa', 75, 1000)
player1.status()
print() # To space out the output
player2.status()
