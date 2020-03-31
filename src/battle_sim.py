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
        self.damage = 20
        self.alive = True

    def status(self):
        if self.health < 1:
            player.alive = False
        print(f"{self.name}: {self.health}")

    def attack(self, target):
        random_num = random.randint(1,6)
        if random_num == 1:
            result = "It's a critical hit!"
            damage = self.damage * 2
        elif random_num == 2:
            result = "Oh no, they miss!"
            damage = 0
        else:
            result = "The strike lands hard."
            damage = self.damage
        target.health -= damage
        print(f"{self.name} attacks! {result}")

    def drink_potion(self):
        print(f"{self.name} drinks a potion and is healed by 10hp.")
        self.health += 10

    def choose_action(self, action, enemy):
        if action == "ATTACK":
            self.attack(enemy)
        elif action == "POTION":
            self.drink_potion()
        else:
            print(f"{self.name} can't do that!")


# Creating Characters
player = Character('Elgar')
enemy = Character('Drobwyn')

# Main Game Loop
while player.alive and enemy.alive:

    # Player's Turn
    player_action = input(f"Does {player.name} ATTACK or drink a POTION? ")
    player.choose_action(player_action, enemy)

    # Enemy's Turn
    enemy_action = random.choice(["ATTACK", "POTION"])
    enemy.choose_action()

    # Summarise
    player.status()
    enemy.status()

# After Battle
if player.alive:
    winner = player
else:
    winner = enemy

print(f"The battle is over. {winner.name} won.")
