# ⚔️ RPG Weapon Generator

Forge a new weapon with a single command.

This lightweight Python project creates randomized RPG weapons, giving every drop its own weapon type, rarity, damage, durability, and chance of being magical.

## ✨ Features

- **10 weapon types** — swords, axes, daggers, bows, crossbows, and more
- **Melee and ranged weapons**
- **Five weighted rarity tiers** — Common, Uncommon, Rare, Epic, and Legendary
- **Randomized damage and durability** based on each weapon type
- **Rarity stat multipliers** that make valuable drops more powerful
- **Individual magic chances** for every weapon
- **Simple terminal output** with a quick power and magic classification

## 🎲 Example

```text
===== WEAPON =====
Name: Crossbow
Type: Ranged
Rarity: Epic
Damage: 107
Durability: 118
Magic: Yes
powerful weapon
magical weapon
```

Every run creates a different result.

## 🚀 Getting Started

### Requirements

- Python 3
- No external packages required

### Run the generator

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python rpg_weapon_generator.py
```

On some Windows systems, use:

```bash
py rpg_weapon_generator.py
```

## 🧙 How It Works

1. A weapon template is selected at random.
2. A rarity is rolled using weighted probabilities.
3. Damage and durability are generated from the weapon's stat ranges.
4. The rarity multiplier improves those stats.
5. A final roll decides whether the weapon is magical.

| Rarity | Stat multiplier | Weight |
|---|---:|---:|
| Common | 1.00× | 65 |
| Uncommon | 1.10× | 25 |
| Rare | 1.25× | 12 |
| Epic | 1.60× | 6 |
| Legendary | 2.00× | 2 |

## 🛠️ Ideas for Future Upgrades

- Fantasy weapon names and prefixes
- Elements, enchantments, and special effects
- Character levels and stat requirements
- Gold values and loot inventories
- Generate several weapons at once
- Save generated weapons to a file
- Add a graphical interface

## 📜 License

This project currently has no license. If you want others to reuse or modify it, consider adding one.

---

Made with Python, randomness, and a little dungeon magic. 🐉
