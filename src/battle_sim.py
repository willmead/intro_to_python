"""
RPG Battle Engine
Date: 28/03/20
Author: Will

A battle engine for a text based rpg
"""
import random

class Character():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.alive = True
        self.damage = 20

    def status(self):
        print(f"{self.name}: ")
        print(f"Health: {self.health}")
        if self.health <= 0:
            player.alive = False

    def attack(self, target):
        print(f"{self.name} attacks!")

        random_num = random.randint(1,6)
        if random_num == 1:
            print("It's a critical hit!")
            target.health -= self.damage * 2
        elif random_num == 2:
            print("Oh no, they miss!")
        else:
            target.health -= self.damage

    def drink_potion(self):
        print(f"{self.name} drinks a potion and is healed by 10hp.")
        self.health += 10


# Creating Characters
player = Character('Elgar')
enemy = Character('Drobwyn')

# Main Game Loop
while player.alive and enemy.alive:

    # Player's Turn
    action = input(f"Does {player.name} ATTACK or drink a POTION? ")
    if action == "ATTACK":
        player.attack(enemy)
    elif action == "POTION":
        player.drink_potion()
    else:
        print(f"{player.name} can't do that!")

    # Enemy's Turn
    if enemy.health < 30:
        enemy.drink_potion()
    else:
        enemy.attack(player)

    # Summarise
    player.status()
    enemy.status()

# After Battle
if player.alive:
    winner = player
else:
    winner = enemy

print(f"The battle is over. {winner.name} won.")
