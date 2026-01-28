statlist = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
stattotal = ["10", "10", "10", "10", "10", "10"]
skills = set({("Fireball", "you cast fireball. 6d6 fire damage"), ("mage hand", "you cast mage hand. a spectral floating hand appears, controllable by you.")})
def EditSkills():
        action = input("Would you like to add or remove a skill? ").lower().strip()
        if action == "add":
            skillname = input("Enter the name of the skill you want to add: ").strip().capitalize()
            skilldesc = input("Enter a description for the skill: ").strip()
            skills.add((skillname, skilldesc))
            print(f"Skill '{skillname}' has been added.")
                
        elif action == "remove":
            for i in skills:
                print(f"- {i[0]}")
            skillToRemove = input("Enter the name of the skill you want to remove: ").strip().capitalize()
            skill_to_remove = next((skill for skill in skills if skill[0] == skillToRemove), None)
            if skill_to_remove:
                skills.remove(skill_to_remove)
                print(f"Skill '{skillToRemove}' has been removed.")
            else:
                print(f"Skill '{skillToRemove}' not found in your skills.")
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
            print ("Inventory editing is not yet implemented.")
            # Jaxon, you can implement inventory editing here in the future.
        else:
            break