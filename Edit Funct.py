statlist = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
stattotal = ["10", "10", "10", "10", "10", "10"]
skills = set({("Stealth", "Ability to move silently and unseen.")})
def editing():
    while True:
        editC = input("Are you editing  1. Stats, 2. Skills, or 3. Inventory, or do you want to  4. quit:  ").lower().strip()
        if editC == "stats" or editC == "1":
            changableStats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            print("available stats are as follows")
            for x in changableStats:
                print (x)
            statToEdit = input("Which stat would you like to edit? ").lower().strip()
            if statToEdit in changableStats or statToEdit in [s[:3] for s in changableStats]:
                newStatValue = input(f"What would you like to change {statToEdit} to? ").strip()

                match statToEdit:
                    case "strength" | "str":
                        oldstat = stattotal[0]
                        stattotal[0] = newStatValue
                        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")
                    case "dexterity" | "dex":
                        oldstat = stattotal[1]
                        stattotal[1] = newStatValue
                        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")
                    case "constitution" | "con":
                        oldstat = stattotal[2]
                        stattotal[2] = newStatValue
                        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")
                    case "intelligence" | "int":
                        oldstat = stattotal[3]
                        stattotal[3] = newStatValue
                        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")
                    case "wisdom" | "wis":
                        oldstat = stattotal[4]
                        stattotal[4] = newStatValue
                        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")
                    case "charisma" | "cha":
                        oldstat = stattotal[5]
                        stattotal[5] = newStatValue
                        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {newStatValue}.")
            else:
                print("Invalid stat name. Please try again.")
        elif editC == "skills" or editC == "2":
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
            else:
                print("Invalid action. Please choose 'add' or 'remove'.")
        elif editC == "inventory" or editC == "3":
            print ("Inventory editing is not yet implemented.")
            # Jaxon, you can implement inventory editing here in the future.
        else:
            break
editing()
print (skills)
for i in statlist:
    print (f"{i.capitalize()}: {stattotal[statlist.index(i)]}")
