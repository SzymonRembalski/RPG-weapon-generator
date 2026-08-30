import random

rarity = [
    {
        "name": "Common",
        "multiplier": 1.0,
        "weight": 65
    },
    {
        "name": "Uncommon",
        "multiplier": 1.10,
        "weight": 25
    },
    {
        "name": "Rare",
        "multiplier": 1.25,
        "weight": 12
    },
    {
        "name": "Epic",
        "multiplier": 1.6,
        "weight": 6
    },
    {
        "name": "Legendary",
        "multiplier": 2.0,
        "weight": 2
    }
]

weapons = [     
                {
                    "name":"Sword",
                    "type":"Melee",
                    "damage_range": (40, 60),
                    "durability_range": (70, 100),
                    "magic_chance": 15
                },
                {
                    "name":"Axe",
                    "type":"Melee",
                    "damage_range": (55, 80),
                    "durability_range": (50, 80),
                    "magic_chance": 10
                },
                {
                    "name":"Dagger",
                    "type":"Melee",
                    "damage_range": (20, 40),
                    "durability_range": (80, 100),
                    "magic_chance": 25
                },
                {
                    "name":"Mace",
                    "type":"Melee",
                    "damage_range": (60, 90),
                    "durability_range": (40, 70),
                    "magic_chance": 10
                },
                {
                    "name":"Spear",
                    "type":"Melee",
                    "damage_range": (45, 70),
                    "durability_range": (60, 90),
                    "magic_chance": 15
                },
                {
                    "name":"Bow",
                    "type":"Ranged",
                    "damage_range": (35, 55),
                    "durability_range": (40, 70),
                    "magic_chance": 20
                },
                {
                    "name":"Crossbow",
                    "type":"Ranged",
                    "damage_range": (55, 75),
                    "durability_range": (60, 90),
                    "magic_chance": 15
                },
                {
                    "name":"Throwing Knife",
                    "type":"Ranged",
                    "damage_range": (15, 35),
                    "durability_range": (10, 30),
                    "magic_chance": 20
                },
                {
                    "name":"Sling",
                    "type":"Ranged",
                    "damage_range": (20, 40),
                    "durability_range": (90, 100),
                    "magic_chance": 5
                },
                {
                    "name":"Javelin",
                    "type":"Ranged",
                    "damage_range": (50, 70),
                    "durability_range": (20, 50),
                    "magic_chance": 10
                }
]

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
