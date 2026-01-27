# AC 2nd Arsh RPG Character Manager

# libraries
import random

# intro
def intro():
    print("Welcome to your RPG Character Manager\nView and modify all your characters' information, skills and attributes\nTo choose what you want to do, type the corresponding number on the menus\n")

# attribute assigner
def attribute_assigner(attribute, random_num1, random_num2):
    attribute = random.randint(random_num1, random_num2)
    return attribute

first_premade_character = {
    "info": {
        "name": "Zarkon",
        "race": "Dragonborn",
        "class": "Fighter",
        "level": 4,
    },
    "inventory": {
        "item name": "value"
    },
    "skills": {
        "strength": attribute_assigner("Strength", 8, 18),
        "dexterity": attribute_assigner("Dexterity", 8, 18),
        "intelligence": attribute_assigner("Intelligence", 8, 18),
        "wisdom": attribute_assigner("Wisdom", 8, 18),
        "constitution": attribute_assigner("Constitution", 8, 18),
        "health": attribute_assigner("Health", 8, 15),
        "armor_class": attribute_assigner("Armor Class", 10, 17),
        "charisma": attribute_assigner("Charisma", 8, 18),
    },
    "attributes": {
        "attributes": "values"
    }
}

"""database = {"name":{"simpleinfo":["Name", "race", "class", "level"], "inventory":{Itemslot:["item name", ”values”]}, "skills":({skillname:skilldesc}, ), "attributes":[["attributes"], ["values"]]},
            "second character":{"info":"placeholder"}
            }"""
