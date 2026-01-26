statlist = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
stattotal = ["10", "10", "10", "10", "10", "10"]
def editing():
    editC = input("Are you editing Stats, Skills, or Inventory? ").lower().strip()
    if editC == "stats":
        changableStats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma", "str", "dex", "con", "int", "wis", "cha"]
        statToEdit = input("Which stat would you like to edit? ").lower().strip()
        if statToEdit in changableStats:
            newStatValue = input(f"What would you like to change {statToEdit} to? ").strip()

            match statToEdit:
                case "strength" | "str":
                    stattotal[0] = newStatValue
                case "dexterity" | "dex":
                    stattotal[1] = newStatValue
                case "constitution" | "con":
                    stattotal[2] = newStatValue
                case "intelligence" | "int":
                    stattotal[3] = newStatValue
                case "wisdom" | "wis":
                    stattotal[4] = newStatValue
                case "charisma" | "cha":
                    stattotal[5] = newStatValue

            print(f"{statToEdit.capitalize()} has been updated to {newStatValue}.")
        else:
            print("Invalid stat name. Please try again.")
    elif editC == "skills":