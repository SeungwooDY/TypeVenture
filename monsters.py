import random
import json

class Monster:
    def __init__(self, name, strength, lives, exp):
        self.name = name
        self.strength = strength
        self.lives = lives
        self.exp = exp
    
    def get_name(self):
        return self.name
    
    def get_strength(self):
        return self.strength
    
    def get_lives(self):
        return self.lives
    
    def get_exp(self):
        return self.exp
    
    def attack(self):
        return random.randint(1, self.strength)


# Define some monsters with their attributes
with open ("monster.json") as file:
    monsters_data = json.load(file)

monsterList = []

for item in monsters_data:
    name = item["name"]
    strength = item["strength"]
    lives = item["lives"]
    exp = item["exp"]

    monster = Monster(name, strength, lives, exp)
    monsterList.append(monster)
