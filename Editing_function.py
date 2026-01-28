statlist = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
stattotal = ["10", "10", "10", "10", "10", "10"]
skills = set({("Fireball", "you cast fireball. 6d6 fire damage"), ("mage hand", "you cast mage hand. a spectral floating hand appears, controllable by you.")})
Items_Dictonaties = {"Weapon":["Sword","Weapon","none"],"Armor":["Iron armor","Armor","none"],"Inventory":["daggers","Weapon","Rouge","staff","Weapon","None"]}
def EditSkills():
        action = input("Would you like to add or remove a skill? ").lower().strip()
        if action == "add":
            skillname = input("Enter the name of the skill you want to add: ").capitalize().strip()
            skilldesc = input("Enter a description for the skill: ").strip()
            skills.add((skillname, skilldesc))
            print(f"Skill '{skillname}' has been added.")
                
        elif action == "remove":
            for i in skills:
                print(f"- {i[0]}")
            skillToRemove = input("Enter the name of the skill you want to remove: ").capitalize().strip()
            skill_to_remove = next((skill for skill in skills if skill[0] == skillToRemove), None)
            if skill_to_remove:
                skills.remove(skill_to_remove)
                print(f"Skill '{skillToRemove}' has been removed.")
            else:
                print(f"Skill '{skillToRemove}' not found in your skills.")


def inventory_management(Items_Dictonaties,player_class):
    print(f"Your charaters weapon is a {Items_Dictonaties["Weapon"][0]}")
    print(f"Your charaters is wearing {Items_Dictonaties["Armor"][0]} ")
    print(f"This is your inventory:")
    val = 0
    for x in Items_Dictonaties["Inventory"]:
        val += 1
        if val == 1:
            print(x)
        if val == 3:
            val = 0
    Player_answer = input("Would you like to Edit you inventory(1.Yes 2.No):").capitalize().strip()
    if Player_answer == "1" or Player_answer == "Yes":
        asking = True
        while asking:
            players_selected_action = input("Would you like to (1.edit your inventory 2.Add a item to your inventory 3.To exit):").capitalize().strip()
            if players_selected_action == "1":
                answering = True
                while answering:
                    for x in Items_Dictonaties["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
                    Edit_item = input("What item in your inventory do you want to edit:").capitalize().strip()
                    if Edit_item in Items_Dictonaties["Inventory"]:
                        Item_index = Items_Dictonaties["Inventory"].index(Edit_item)
                        Item_slot = Items_Dictonaties["Inventory"][Item_index + 1]
                        Item_class = Items_Dictonaties["Inventory"][Item_index + 2]
                        if Item_class == player_class or Item_class == "None":
                            for x in range(0,3):
                                    Items_Dictonaties["Inventory"].pop(Item_index) 
                            for x in range(0,3):
                                if Items_Dictonaties[Item_slot][0] != "None":
                                    Items_Dictonaties["Inventory"].append(Items_Dictonaties[Item_slot][x]) 
                            Items_Dictonaties[Item_slot] = [Edit_item,Item_slot,Item_class]
                            print(f"Your charaters weapon is a {Items_Dictonaties["Weapon"][0]}")
                            print(f"Your charaters is wearing {Items_Dictonaties["Armor"][0]} ")
                            print(f"This is your inventory:")
                            val = 0
                            for x in Items_Dictonaties["Inventory"]:
                                val += 1
                                if val == 1:
                                    print(f"- {x}")
                                if val == 3:
                                    val = 0
                            answering = False
                        else:
                            print(f"Your charater class is incorect. you need to be a {Item_class}, but you are a {player_class}")
                    else:
                        print("that is not an item in your inventory")
            if players_selected_action == "2":
                player_item_name = input("What is the name of the item:").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_name)
                player_item_slot = input("What is the slot of the item(Inventory,Weapon,Armor):").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_slot)
                player_item_class = input("What is the required class of the item(If no required one then type None):").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_class)
                for x in Items_Dictonaties["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
            if players_selected_action == "3":
                asking = False
            


def editing():


    def displaystat(num):
        oldstat = stattotal[num]
        stattotal[num] = newStatValue
        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")

    while True:
        editC = input("Are you editing  1. Stats, 2. Skills, or 3. Inventory, or do you want to  4. quit:  ").lower().strip()
        if editC == "stats" or editC == "1":
            changableStats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            print("available stats are as follows")
            for x in changableStats:
                print (f" - {x}")
            statToEdit = input("Which stat would you like to edit? ").lower().strip()
            if statToEdit in changableStats or statToEdit in [s[:3] for s in changableStats]:
                newStatValue = input(f"What would you like to change {statToEdit} to? ").strip()

                    
                match statToEdit:
                    case "strength" | "str":
                        displaystat(0)
                    case "dexterity" | "dex":
                        displaystat(1)
                    case "constitution" | "con":
                        displaystat(2)
                    case "intelligence" | "int":
                        displaystat(3)
                    case "wisdom" | "wis":
                        displaystat(4)
                    case "charisma" | "cha":
                        displaystat(5)
            else:
                print("Invalid stat name. Please try again.")


        elif editC == "skills" or editC == "2":
            EditSkills()
        elif editC == "inventory" or editC == "3":
            inventory_management(Items_Dictonaties,"None")
        else:
            break

editing()