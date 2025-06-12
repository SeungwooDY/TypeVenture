import random

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
wolf = Monster("Wolf", 5, 1, 10)
goblin = Monster("Goblin", 7, 2, 25)
dragon = Monster("Dragon", 15, 3, 50)

monsterList = [wolf, goblin, dragon]
