from enum import Enum
import json

class EquipmentType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    POTION = "potion"

class Equipment:
    def __init__(self, name, type, strength, rarity):
        self.name = name
        self.type = type # e.g., "weapon", "armor", "potion"
        self.strength = strength
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}: {self.type.value}, Strength: {self.strength}, Rarity: {self.rarity}"
    
    def get_name(self):
        return self.name
    
    def get_strength(self):
        return self.strength
    
    def get_rarity(self):
        return self.rarity
    
# Define some equipment with their attributes
with open("equipment.json") as file:
    equipment_data = json.load(file)

equipmentList = []

for item in equipment_data:
    name = item["name"]
    equipment_type = EquipmentType[item["type"]]
    strength = item["stat"]
    rarity = item["rarity"]

    equipment = Equipment(name, equipment_type, strength, rarity)
    equipmentList.append(equipment)