# FB 1st Character manager
import sys

def validate_input(text, kind='int'):
    s = str(text).strip().capitalize()
    if kind == 'int':
        try:
            int(s)
            return True
        except ValueError:
            return False
    elif kind == 'float':
        try:
            float(s)
            return True
        except ValueError:
            return False
    elif kind == 'alpha':
        return s.isalpha()
    else:
        return False
    
def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n").strip().capitalize()
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
            
    return choicevar


def viewchars(data):
    characterkeys = database.keys()
    characternameandlistnum = {}

    count = 1
    for character in characterkeys:
        characternameandlistnum[count] = character

        print(f"{count}. {character} : {database[character]["info"][0]}, {database[character]["info"][1]}, {database[character]["info"][2]}")
        count += 1

    print("Would you like to:\n1. Select\n2. Sort\n3. Main menu")

    choice = inputchecker(3)
    
    match choice:
        case 1:
            select(data,characternameandlistnum)
        case 2:
            sort(data)
        case 3:
            mainmenu(data)

def select(data, selectionmenu):
    print("Which character do you want to select? (Refer to the list above)")

    characternum = inputchecker(len(selectionmenu))
    character = selectionmenu[characternum]

    print(f"{character} : {database[character]["info"][0]}, {database[character]["info"][1]}, {database[character]["info"][2]}")

    for itemslot in data[character]["inventory"].keys():

        item = data[character]["inventory"][itemslot]
        print(f"{itemslot} : {item[0]} it {item[1]}, and only a {item[2]} can use it!")

    

def sort(data):
    pass

def createcharacters(data):
    pass
        

def mainmenu(database):
    while True:
        print("You may:\n1. View Characters\n2. Create Character\n3. Exit")

        functionchoice = inputchecker(3)
        if functionchoice == 1:
            print("\n")
            viewchars(database)
        elif functionchoice == 2:
            createcharacters(database)
        else:
            sys.exit()


print("Hello! This is a simple character management software")
                                            # item slot type, armor, weapon, misc, etc V
database = {"name":{"info":["race", "class", "level"], "inventory":{"weapon":["staff", "heals 5 HP", "Healer"]}, "skills":("skillname and desc"), "attributes":[["attributes"], ["values"]]},
            "Lopez":{"info":["dragon", "warrior", "19"]}
            }

mainmenu(database)