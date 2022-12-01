import json,colorama
from colorama import Fore,Back,Style
from pprint import pprint
colorama.init()
Gspaceing = 10
def LJspace(string):
    spaceAdd = Gspaceing - len(string)
    if (spaceAdd > 0):
        lJust = string+(" "*spaceAdd)
        return lJust 
    return string

def centerSpace(string):
    centerSpaceing = 6
    CJust = str(string).center(Gspaceing+centerSpaceing)
    return CJust

def read(usrInput:str='None' ) -> dict: #returns data base
    with open ('database.json', 'r') as filee:
        if usrInput != 'None':
            temp = [i[usrInput] for i in (json.load(filee))]
        else:temp = json.load(filee)
    return temp

def printData(userImp:str='None'):
    currentDB = read()
    everyKeys = [key for key,value in currentDB[0].items()] # assume all keys are the same --> pull keys from first item of database
#check what the user wants to check/read  : IE certain dicts or certain values of dicts
    if userImp in everyKeys:lookingKey = True
    elif isinstance(userImp,int): lookingKey = False
    else:lookingKey = None
        
    for index in range(len((currentDB[0]))):
        currentKey = everyKeys[index]
        everyItemOfKey = [i[currentKey] for i in currentDB]  # gets every item in the WHOLE database with the CURRENT key
#user wants a certain key/information highlighed
        if lookingKey and currentKey == userImp:
            print(f" {Fore.CYAN}[{str(index).center(2)}] {LJspace(everyKeys[index])} : {' | '.join([centerSpace(i) for i in map(str,everyItemOfKey)])}{Fore.RESET}") 
        elif lookingKey:
            print(f" [{str(index).center(2)}] {LJspace(everyKeys[index])} : {' | '.join([centerSpace(i) for i in map(str,everyItemOfKey)])} ") 

#user wants a certain row highlighted
        if lookingKey == False:
            print(f" [{str(index).center(2)}] {LJspace(everyKeys[index])} : ",end="")#print keys / num
    #list data part print section
            for index,value in enumerate(everyItemOfKey):
                if index == userImp:
                    print(f"{Fore.CYAN}{centerSpace(value)}{Fore.RESET}",end="")
                else:
                    print(f"{centerSpace(value)}",end="")
                print(" | ",end="")
            print()

#user wants it just printed normally nothing highlighed
        else:
            print(f" [{str(index).center(2)}] {LJspace(everyKeys[index])} : {' | '.join([centerSpace(i) for i in map(str,everyItemOfKey)])} ") 

#TODO UPDATE
def update():
 
    currentDB = read()
    with open ('database.json', 'r') as filee:
        x = input('which number item would you like to change > ')


#TODO CREATE

#TODO DELETE


#--init--#
printData(3)
