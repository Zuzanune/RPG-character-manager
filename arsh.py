# AC 2nd Arsh RPG Character Manager

# libraries
import random

# intro
def intro():
    print("Welcome to your RPG Character Manager\nView and modify all your characters' information, skills and attributes\nTo choose what you want to do, type the corresponding number on the menus\n")

# 3 premade characters
database = {
    "Zarkon":{"simpleinfo":["Dragonborn", "Fighter", 8], "inventory": {"Weapons": ["Shortsword", "3"]}, "skills":({"Fireball":"A bright streak flashes from the caster to a point within 150 feet, erupting into a 20-foot-radius sphere of fire!"}, ), "attributes": [["strength"],[random.randint(8, 18)]][["dexterity"],[random.randint(8, 18)]][["intelligence"],[random.randint(8, 18)]][["wisdom"],[random.randint(8, 18)]][["constitution"],[random.randint(8, 18)]][["health"],[random.randint(8, 15)]][["armor class"],[random.randint(10, 17)]][["charisma"],[random.randint(8, 18)]]},

    "Gulnum":{"simpleinfo":["Gnome", "Sorcerer", 4], "inventory": {"Weapons": ["Mace", "5"]}, "skills":({"SKILL_PLACEHOLDER":"SKILL PLACEHOLDER DESCRIPTION"}, ), "attributes": [["strength"],[random.randint(8, 18)]][["dexterity"],[random.randint(8, 18)]][["intelligence"],[random.randint(8, 18)]][["wisdom"],[random.randint(8, 18)]][["constitution"],[random.randint(8, 18)]][["health"],[random.randint(8, 15)]][["armor class"],[random.randint(10, 17)]][["charisma"],[random.randint(8, 18)]]},

    "Zylvina":{"simpleinfo":["Elf", "Cleric", 13], "inventory": {"Weapons": ["Whip", "3"]}, "skills":({"SKILL_PLACEHOLDER":"SKILL PLACEHOLDER DESCRIPTION"}, ), "attributes": [["strength"],[random.randint(8, 18)]][["dexterity"],[random.randint(8, 18)]][["intelligence"],[random.randint(8, 18)]][["wisdom"],[random.randint(8, 18)]][["constitution"],[random.randint(8, 18)]][["health"],[random.randint(8, 15)]][["armor class"],[random.randint(10, 17)]][["charisma"],[random.randint(8, 18)]]}
}