"""
Function for inventory_management(Chardata):
Display inventory
Receive players input if they want to edit it
Yes:
	Get item player wants to edit
	Check if they can use that item(By using the information the item has)
	If they can swap out item if not then repeat until they chose to leave or  it works
	Ask if they want to edit more if not return inventory and exit
No:
	Exit the function


"""
#Example dictonary Items_Dictonaties = {"Weapon":[#item name,#Slot type.#class required,#Weight,],"Armor":[],"Inventory":{} }
Items_Dictonaties = {"Weapon":["Sword"],"Armor":["Iron armor"],"Inventory":{}}

def inventory_management(Items_Dictonaties):
    print(f"Your charaters weapon is a {Items_Dictonaties["Weapon"][0]}")
    print(f"Your charaters is wearing {Items_Dictonaties["Armor"][0]} ")
    print(f"In your inventory is {Items_Dictonaties["Inventory"]}")
    


inventory_management(Items_Dictonaties)