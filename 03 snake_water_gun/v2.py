'''some updations and code refactoring'''
from random import randint

options=['gun','snake','water']

[print(i, "-", options[i]) for i in range(3)]


def takeinp():
    personChoice = int(
        input("Enter the index of your choice from above options: "))
    if personChoice not in range(3):
        print("Please choose correct option")
        takeinp()
    else:
        return personChoice

personChoice = takeinp()

computerChoice = randint(0, 2)

winCases={(0,2),(1,0),(2,1)} # c,p

def checkWin(cChoice,pChoice):
    # gun -> snake -> water -> gun
    if cChoice==pChoice:
        print('The game is draw')
    
    elif (cChoice,pChoice) in winCases:
        print("You won")
    
    else:
        print('You lost to computer')