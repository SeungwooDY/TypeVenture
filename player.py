import random as rdm

locations = ["castle", "cave", "woods", "village", "mountain", "forest"]

level_up_threshold = 100

class Player:
    def __init__(self, name):
        self.name = name
        self.location = "castle"
        self.inventory = []
        self.lives = 3
        self.experience = 0
        self.strength = 10

    def move(self, direction):
        if direction == "north":
            self.location = "forest"
        elif direction == "south":
            self.location = "village"
        elif direction == "east":
            self.location = "mountain"
        elif direction == "west":
            self.location = "river"
        else:
            print("\nInvalid direction!")

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"\nYou picked up ({item}).")

    def show_inventory(self):
        return self.inventory
    
    def get_strength(self):
        return self.strength
    
    def get_location(self):
        return self.location
    
    def get_name(self):
        return self.name
    
    def lose_life(self):
        self.lives -= 1
        print(f"\nYou lost a life! Lives remaining: {self.lives}")
        if self.lives <= 0:
            print("\nGame Over! You have no lives left.")
            exit()
    
    def use_potion(self):
        if "potion" in self.inventory:
            self.lives += 1
            self.inventory.remove("potion")
            print("\nYou used a potion and gained a life!")
        else:
            print("\nYou don't have a potion to use.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"\nYou gained {amount} experience points! Experience left to level up: {100 - self.experience}")
    
    def level_up(self):
        if self.experience >= level_up_threshold:
            self.experience -= level_up_threshold
            print(f"\nCongratulations {self.name}! You leveled up!")
            level_up_threshold *= 1.5
            self.lives += 1
            self.strength += 5
            print("\nCongratulations! You leveled up and gained an extra life!")
            print(f"\nYou not have {self.lives} lives and {self.strength} strength.")
        else:
            print("\nNot enough experience to level up.")