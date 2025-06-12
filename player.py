import random as rdm

locations = ["castle", "cave", "woods", "village", "mountain", "forest"]

level_up_threshold = 100
player_level = 1

class Player:
    def __init__(self, name):
        self.name = name
        self.location = "castle"
        self.inventory = []
        self.lives = 3
        self.max_lives = 3
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

    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def show_inventory(self):
        return self.inventory
    
    def get_lives(self):
        return self.lives
    
    def get_experience(self):
        return self.experience
    
    def get_strength(self):
        return self.strength
    
    def get_level_up_threshold(self):
        return level_up_threshold
    
    def get_level(self):
        return player_level
    
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
            self.experience = self.experience - level_up_threshold
            print(f"\nCongratulations {self.name}! You leveled up!")
            level_up_threshold *= 1.5
            self.lives += 1
            self.strength += 5
            print("\nCongratulations! You leveled up and gained an extra life!")
            print(f"\nYou now have {self.lives} lives and {self.strength} strength.")
        else:
            print("\nNot enough experience to level up.")

    def pick_item(self, item):
        if len(self.inventory) > 10:
            print("\nYour inventory is full! You cannot pick up any more items.")
        else: 
            self.inventory.append(item)
            print(f"\nYou picked up ({item}).")
            equip = input(f"\nWould you like to equip this item? (yes/no)")
            if equip.strip().lower() == "yes":
                print(f"\nYou equipped the {item}.")
                self.equip(item)

    def equip(self, item):
        if item == "sword":
            self.strength += 5
            print("\nYou equipped a sword. Strength increased by 5.")
            self.inventory.remove("sword")
        elif item == "upgraded sword":
            self.strength += 20
            print("\nYou equipped an upgraded sword. Strength increased by 20.")
            self.inventory.remove("upgraded sword")
        elif item == "shield":
            self.max_lives += 1
            print("\nYou equipped a shield. Lives increased by 1.")
            self.inventory.remove("shield")
        elif item == "upgraded shield":
            self.max_lives += 5
            print("\nYou equipped an upgraded shield. Lives increased by 5.")
            self.inventory.remove("upgraded shield")
        elif item == "potion":
            self.inventory.append("potion")
            print("\nYou equipped a potion. You can use it to restore a life.")
        elif item == "upgraded potion":
            self.inventory.append("potion")
            print("\nYou equipped a potion. You can use it to restore a life.")
        else:
            print("\nUnknown item!")
    
    def upgrade_item(self, item):
        if self.inventory.count(item) >= 3:
            self.inventory.remove(item)
            upgraded_item = "upgraded " + item
            self.inventory.append(upgraded_item)
            print(f"\nYou upgraded your {item} to {upgraded_item}.")