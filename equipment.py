from enum import Enum
import json

class EquipmentType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    POTION = "potion"

class Equipment:
    def __init__(self, name, type, stat, rarity):
        self.name = name
        self.type = type # e.g., "weapon", "armor", "potion"
        self.stat = stat
        self.rarity = rarity

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return f"{self.name}: {self.type.value}, Strength: {self.strength}, Rarity: {self.rarity}"
    
    def get_name(self):
        return self.name
    
    def get_stat(self):
        return self.stat
    
    def get_rarity(self):
        return self.rarity
    
    def get_type(self):
        return self.type
    
# Define some equipment with their attributes
with open("equipment.json") as file:
    equipment_data = json.load(file)

equipmentList = []

for item in equipment_data:
    name = item["name"]
    equipment_type = EquipmentType[item["type"]]
    stat = item["stat"]
    rarity = item["rarity"]

    equipment = Equipment(name, equipment_type, stat, rarity)
    equipmentList.append(equipment)