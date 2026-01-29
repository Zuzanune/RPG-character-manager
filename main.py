from Editing_function import *
import random
from franco import mainmenu
from arsh import intro

#The Database NEEDS to remain this way, otherwise the functions will not work correctly.
database = {
    "Zarkon":{"simpleinfo":["Dragonborn", "Fighter", 8], "Items_Dictionary": {"Weapon": ["Shortsword", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("Fireball","A bright streak flashes from the caster to a point within 150 feet, erupting into a 20-foot-radius sphere of fire!")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 15), random.randint(10, 17), random.randint(8, 18)]]},

    "Gulnum":{"simpleinfo":["Gnome", "Sorcerer", 4], "Items_Dictionary": {"Weapon": ["Mace", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("SKILL_PLACEHOLDER","SKILL PLACEHOLDER DESCRIPTION")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 15), random.randint(10, 17), random.randint(8, 18)]]},

    "Zylvina":{"simpleinfo":["Elf", "Cleric", 13], "Items_Dictionary": {"Weapon": ["Whip", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("SKILL_PLACEHOLDER","SKILL PLACEHOLDER DESCRIPTION")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 18), random.randint(8, 15), random.randint(10, 17), random.randint(8, 18)]]},

    "test":{"simpleinfo":["Human", "Rogue", 1], "Items_Dictionary": {"Weapon": ["Dagger", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []}, "skills":{("Stealth","The character can move silently and avoid detection")}, "attributes": [["strength", "dexterity", "intelligence", "wisdom", "constitution", "health", "armor class", "charisma"], [10, 10, 10, 10, 10, 10, 10, 10]]}}

if __name__ == "__main__":
    intro()
    mainmenu(database)