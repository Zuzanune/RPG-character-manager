# AC 2nd Arsh RPG Character Manager

# libraries
import random

# intro
def intro():
    print("Welcome to your RPG Character Manager\nView and modify all your characters' information, skills and attributes\nTo choose what you want to do, type the corresponding number on the menus\n")

# attribute assigner
def attribute_assigner(strength, dexterity, intelligence, wisdom, constitution, health, armor_class, charisma):
    strength = random.randint(8, 18)
    dexterity = random.randint(8, 18)
    intelligence = random.randint(8, 18)
    wisdom = random.randint(8, 18)
    constitution = random.randint(8, 18)
    health = random.randint(8, 15)
    armor_class = random.randint(10, 17)
    charisma = random.randint(8, 18)

    return strength, dexterity, intelligence, wisdom, constitution, health, armor_class, charisma