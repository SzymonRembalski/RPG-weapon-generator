import json
import random
from pathlib import Path


DATA_FILE = Path(__file__).with_name("weapon_data.json")

with DATA_FILE.open(encoding="utf-8") as file:
    weapon_data = json.load(file)

rarity = weapon_data["rarities"]
weapons = weapon_data["weapons"]

class Weapon:
    def __init__(self, name, weapon_type, damage, durability, is_magic, rarity_name):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.durability = durability
        self.is_magic = is_magic
        self.rarity_name = rarity_name

    def display_info(self):
        print("===== WEAPON =====")
        print("Name:", self.name)
        print("Type:", self.weapon_type)
        print("Rarity:", self.rarity_name)
        print("Damage:", self.damage)
        print("Durability:", self.durability)
        print("Magic:", "Yes" if self.is_magic else "No")
        if self.damage > 50:
            print("powerful weapon")
        else:
            print("weak weapon")
        
        if self.is_magic:
            print("magical weapon")
        else:
            print("normal weapon")

def generate_random_weapon():
    template = random.choice(weapons)
    rareness_template = random.choices(rarity, weights=[r["weight"] for r in rarity], k=1)[0]
    weapon = Weapon(
        weapon_type = template["type"],
        damage = round(random.randint(*template["damage_range"]) * rareness_template["multiplier"]),
        durability = round(random.randint(*template["durability_range"]) * rareness_template["multiplier"]),
        is_magic = False,
        name = template["name"],
        rarity_name = rareness_template["name"]
        )
    is_magic_roll = random.randint(1, 100)
    if is_magic_roll <= (template["magic_chance"] * rareness_template["multiplier"]):
        weapon.is_magic = True
    return weapon

weapon = generate_random_weapon()
weapon.display_info()
