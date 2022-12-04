import json,colorama,extrafunctions as eF
from colorama import Fore
colorama.init()
with open ('Databases/databaseV2.json', 'r') as filee:
    currentDB = json.load(filee)
everyKeys = [key[0] for key in currentDB[0].items()] # assume all keys are the same --> pull keys from first item of database


def read(ui:str=None) -> dict: #returns data base
    if ui == 'new':
        with open ('Databases/databaseV2.json', 'r') as filee:
            temp = json.load(filee)
    else:
        with open ('database.json', 'r') as filee:
            temp = json.load(filee)
    return temp

def printData(userImp:str='None',dataset:str=None): #print data formated by key and values (assume all keys are the same)
    currentDB = read('new')

#check what the user wants to check/read  : IE certain dicts or certain values of dicts

    if userImp in everyKeys:lookingKey = True  # ID,NAMES,CLASS
    elif len(userImp)==1 and userImp.isnumeric() and int(userImp) in range(len(everyKeys)) : # 1,2,3,4,5,6
        lookingKey = True ; userImp = everyKeys[int(userImp)] 
    elif ( len(userImp)==1 and ((len(currentDB))-((ord(userImp))-65) in range(1,len(currentDB)+1))) : # A,B,C,D,E,F
        lookingKey = False ; userImp = ord(userImp)-65
    else:lookingKey = None #NOTHING

    #x / y axis print statments
    print(f"{Fore.RED}{' '*6}X --> \n  Y ↓  {' '*20}{''.join(['['+(chr(i+65))+']'+' '*16 for i in range(len(currentDB))])}")
    print(f"{'─'*6}{chr(43)}{'─'*13}{'─'*19*len(currentDB)}")

    for index in range(len((currentDB[0]))):
        currentKey = everyKeys[index]
        everyItemOfKey = [i[currentKey] for i in currentDB]  # gets every item in the WHOLE database with the CURRENT key

#user wants a certain COLUMN / KEY INFORMATION highlighed
        if lookingKey and currentKey == userImp:
            print(f" {Fore.RED}[{str(index).center(2)}] | {Fore.CYAN} {eF.LJspace(everyKeys[index])}: {' | '.join([eF.centerSpace(i[:15]) for i in map(str,everyItemOfKey)])} |{Fore.RESET}") 

#user wants a certain ROW highlighted 
        elif lookingKey == False:
            print(f" {Fore.RED}[{str(index).center(2)}] │ {Fore.RESET}{eF.LJspace(everyKeys[index])} : ",end="")#print keys / num
    #list data part print section
            for index,value in enumerate(everyItemOfKey):
                if index == userImp:
                    print(f"{Fore.CYAN}{eF.centerSpace(value[:15])}{Fore.RESET}",end="")
                else:
                    print(f"{eF.centerSpace(value[:15])}",end="")
                print(" | ",end="")
            print()

#user wants it just printed normally nothing highlighed
        else: print(f" {Fore.RED}[{str(index).center(2)}] | {Fore.RESET} {eF.LJspace(everyKeys[index])}: {' | '.join([eF.centerSpace(i[:15]) for i in map(str,everyItemOfKey)])} |") 
#UPDATE/EDIT
def update():
    currentDB = read('new')

    printData('','v2')
    space = input('What position would you like to spot to change (IE: A15 / 15A)> ') #'D15' 
    newItem = input('Which would you to change this item to > ') 

    # COLLECT calculate which dataset / COLUMN to use
    yValue =int(''.join([ spot for spot in space if spot.isnumeric() ]))  
    yAxis = everyKeys[yValue]
    # COLLECT and calculate which dataset / ROW to use
    xAxis = int(ord(''.join([ spot for spot in space if spot.isalpha() ]))-65)

    if xAxis >= 0 and xAxis < len(currentDB[0]):
        currentDB[xAxis][yAxis] = newItem

    with open ('Databases/databaseV2.json', 'w') as filee:    
        json.dump(currentDB,filee,indent=4)
    printData('','v2')

#CREATE
def create():
    currentDB = read('new')
    newIValues = {i:input(f'What would you like to change {i} to > ') for i in everyKeys}
    currentDB.append(newIValues)
    with open ('Databases/databaseV2.json', 'w') as filee:   
        json.dump(currentDB,filee,indent=4)
    printData('','v2')

#DELETE
def delete():
    currentDB = read('new')
    removeValue = ord(input('Which Row do you want to remove > ').upper())-65
    currentDB.pop(removeValue)
    with open ('Databases/databaseV2.json', 'w') as filee:   
        json.dump(currentDB,filee,indent=4)
    printData('','v2')

#--init--#
while True:
    try:
        choice = int(input
    ("""[1] Print Data
[2] Update/Edit
[3] Create
[4] Delete
    >"""))
        if choice == 1:
            printData(input('highlight row/column >'),"v2")
        elif choice == 2:
            update()
        elif choice == 3:
            create()
        elif choice == 4:
            delete()
    except:pass