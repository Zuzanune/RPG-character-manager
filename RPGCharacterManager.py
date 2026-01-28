from Editing_function import editing

database = {
    "test": {
        "simpleinfo": ["human", "wizard", "3"],
        "inventory": {"Itemslot": ["item name", "values", "class needed"]},
        "skills": {("Fireball", "you cast fireball. 6d6 fire damage"), ("mage hand", "you cast mage hand. a spectral floating hand appears, controllable by you.")},
        "attributes": [["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"], ["10", "10", "10", "10", "10", "10"]],
        "Items_Dictionary": {"Weapon":["Sword","Weapon","none"],"Armor":["Iron armor","Armor","none"],"Inventory":["daggers","Weapon","Rogue","staff","Weapon","None"]}
    }
}

editing(database, "test")