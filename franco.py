# FB 1st Character manager
import sys

def validate_input(text, kind='int'):
    s = str(text).strip()
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
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n")
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
            sortchoice(data)
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
    
    for skill in data[character]["skills"]:
        print(f"{skill[0]} it {skill[1]}")
    
    count = 0
    for attribute in data[character]["attributes"][0]:
        print(f"{attribute} : {data[character]["attributes"][1][count]}")
        count += 1

    print("Would you like to:\n1. edit\n2. main menu?")

    answer = inputchecker(2)

    match answer:
        case 1:
            pass # call edit
        case 2:
            mainmenu(data)

def sortoptions(data, typeindex):
    characternames = data.keys()
    previoustypes = []
    typelist = {}

    count = 1
    for character in characternames:

        if data[character]["info"][typeindex] not in previoustypes:
            previoustypes.append(data[character]["info"][typeindex])
            print(f"{count}. {data[character]["info"][typeindex]}")
            typelist[count] = data[character]["info"][typeindex]
            count += 1
    
    return typelist

def sorter(data, choice, types):
    pass

def sortchoice(data):
    print("Will sort by:\n1. Class\n2. Race\n3. Level")

    sortchoice = inputchecker(3)

    match sortchoice:
        case 1:
            distinctclasses = sortoptions(data, 1)
            classchoice = inputchecker(len(distinctclasses))
        case 2:
            distinctraces = sortoptions(data, 0)
            racechoice = inputchecker(len(distinctraces))
        case 3:
            distinctlevels = sortoptions(data, 2)
            levelchoice = inputchecker(len(distinctraces))

def createcharacters(data):
    while True:
        charactername = input("What is the name of this character?")

        if charactername not in data.keys():
            break
    
    characterrace = input("What is the race of this character?")
    characterclass = input("What is the class of this character?")
    characterlevel = input("What is the level of the characters?")

    specificdata = {charactername:{"info":[characterrace, characterclass, characterlevel]}}

    # stats assigner call function

    data.update(specificdata)

    mainmenu(data)
        

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
database = {"name":{"info":["race", "class", "level"], "inventory":{"weapon":["staff", "heals 5 HP", "Healer"]}, "skills":set({("skillname", "desc")}), "attributes":[ ["attributes", "second"], ["values", "secvalue"] ]},
            "Lopez":{"info":["dragon", "warrior", "19"]}
            }

mainmenu(database)