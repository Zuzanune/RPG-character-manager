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
Items_Dictonaties = {"Weapon":["Sword","Weapon","none"],"Armor":["Iron armor","Armor"],"Inventory":["daggers","Weapon","None","staff","Weapon","Rouge"]}

def inventory_management(Items_Dictonaties):
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
    Player_answer = input("Would you like to Edit you inventory(1.Yes 2.No)")
    if Player_answer == "1" or Player_answer == "yes":
        answering = True
        while answering:
            Edit_item = input("What item in your inventory do you want to edit")
            if Edit_item in Items_Dictonaties["Inventory"]:
                answering = False
                Item_index = Items_Dictonaties["Inventory"][Edit_item]
                Item_slot = Items_Dictonaties["Inventory"][Item_index + 1]
                Item_class = Items_Dictonaties["Inventory"][Item_index + 2]
                Items_Dictonaties[Item_slot] = [Edit_item,Item_slot,Item_class]
                
                


        



inventory_management(Items_Dictonaties)