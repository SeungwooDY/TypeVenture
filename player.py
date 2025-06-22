import random as rdm
import json
import equipment

locations = ["castle", "cave", "woods", "village", "mountain", "forest"]

class Player:
    def __init__(self, name):
        self.name = name
        self.location = "castle"
        self.inventory = []
        self.lives = 3
        self.max_lives = 3
        self.experience = 0
        self.strength = 10
        self.player_level = 1
        self.level_up_threshold = 100

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
        if not self.inventory:
            print("\nYour inventory is empty.")
        else:
            print("\nYour inventory contains:")
            for item in self.inventory:
                print(f"\n- {item}")

    def get_inventory(self):
        return self.inventory
    
    def get_lives(self):
        return self.lives
    
    def get_experience(self):
        return self.experience
    
    def get_strength(self):
        return self.strength
    
    def get_level_up_threshold(self):
        return self.level_up_threshold
    
    def get_level(self):
        return self.player_level
    
    def lose_life(self):
        self.lives -= 1
        print(f"\nYou lost a life! Lives remaining: {self.lives}")
        if self.lives <= 0:
            print("\nGame Over! You have no lives left.")
            exit()

    def use_potion(self):
        for item in self.inventory:
            if item.get_type() == equipment.EquipmentType.POTION:
                self.inventory.remove(item)
                self.lives += item.get_stat()
                print(f"\nYou used a potion and gained {item.get_stat()} lives!")
                return
        print("\nYou don't have a potion to use.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"\nYou gained {amount} experience points! Experience left to level up: {100 - self.experience}")
    
    def level_up(self):
        if self.experience >= self.level_up_threshold:
            self.experience = self.experience - self.level_up_threshold
            print(f"\nCongratulations {self.name}! You leveled up!")
            self.level_up_threshold *= 1.5
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
        if item.get_type() == equipment.EquipmentType.WEAPON:
            self.strength += item.get_stat()
            self.inventory.remove(item)
            print(f"\nYou equipped a {item}. Strength increased by {item.get_stat()}.")
        elif item.get_type() == equipment.EquipmentType.ARMOR:
            self.lives += item.get_stat()
            self.inventory.remove(item)
            print(f"\nYou equipped a {item}. Lives increased by {item.get_stat()}")
        elif item.get_type() == equipment.EquipmentType.POTION:
            self.inventory.append("potion")
            print("\nYou equipped a potion. You can use it to restore a life.")
        else:
            print("can't identify item type")
            print("DEBUG:", item, type(item))
            print("item type:", item.get_type())

        return
    
    def upgrade_item(self, item):
        if self.inventory.count(item) >= 3:
            self.inventory.remove(item)
            upgraded_item = "upgraded " + item
            self.inventory.append(upgraded_item)
            print(f"\nYou upgraded your {item} to {upgraded_item}.")