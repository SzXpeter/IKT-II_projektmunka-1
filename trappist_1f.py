import variables, os
from variables import sPrint, userInterface
#sea shore air, cloud sample, ice sample, water sample, bottom oceans
trappist1fLandExamination = [0, 0, 0, 0, 0]
#plants, photo, bottom oceans
trappist1fAliens = [0, 0]

def trappistLandBar():
    x = 0
    for i in range(len(trappist1fLandExamination)):
        if trappist1fLandExamination[i] == 1:
            x += 20
    print(f"Land examination = {x}%")

def trappistAlienBar():
    x = 0
    for i in range(len(trappist1fAliens)):
        if trappist1fAliens[i] == 1:
            x += 50
    print(f"Alien examination = {x}%")

def trappist_1f():
    os.system("cls")
    sPrint("You succesfully landed on Trappist-1f.")
    input("continue <ENTER>")
    sea_shore()
    

def sea_shore():
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0' and v != 'leave':
            os.system("cls")
            userInterface()
            sPrint("You're at the sea shore.")
            print("\n\t1. Examine air")
            print("\t2. Go ot into the flat fields")
            print("\t3. Go towards the ice mountains")
            print("\t0. Repair and restock equipment")
            print("\tleave. Leave planet")
            v = input("choice: ")

        match v:
            case 'leave':
                sPrint("You left planet Trappist-1f.")
                input("continue <ENTER>")
                Exit = True
            case '1':
                if trappist1fLandExamination[0] == 0:
                    os.system("cls")
                    userInterface()
                    trappist1fLandExamination[0] = 1
                    trappistLandBar()
                    sPrint("The air seems to contain a lot of oxygen.")
                    input("continue <ENTER>")
                    v = ''
                    while v != 'y' and v != 'n':
                        os.system("cls")
                        userInterface()
                        sPrint("Do you want to take off your helmet?(y/n)")
                        v = input("choice: ")
                    if v == 'y':
                        os.system("cls")
                        variables.hp -= 5
                        userInterface()
                        sPrint("You take a deep breath.\nThe air is thick with steam.\nIt almost burns your face so you put back your helmet.")
                        input("continue <ENTER>")
                else:
                    sPrint("You already examined the air.")
                    input("continue <ENTER>")
            case '2':
                flat_fields()
            case '3':
                bottom_mountain()
            case '0':
                variables.restock()
        v = ''
    return 0


def flat_fields():
    pass

def bottom_mountain():
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're at the bottom of the mountain.")
            print("\n\t1. Scan your surroundings")
            print("\t2. Try to crack the ice in the mountain")
            print("\t3. Climb up the mountain")
            print("\t0. Go to the sea shore")
            v = input("choice: ")

        match v :
            case '0':
                return 0
            case '1':
                sPrint("You can't see anything interesting")
                input("continue<ENTER>")
            case '2':
                sPrint("You tried to break the ice but it seems to be too thick.")
                input("continue<ENTER>")
            case '3':
                top_mountain()

def top_mountain():
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're at the bottom of the mountain.")
            print("\n\t1. Shout")
            print("\t2. Take sample from the cloud")
            print("\t3. Climb higher up the mountain")
            print("\t0. Climb down")
            v = input("choice: ")

        match v :
            case '0':
                return 0
            case '1':
                sPrint("You can't see anything interesting")
                input("continue<ENTER>")
            case '2':
                os.system("cls")
                trappist1fLandExamination[1] = 1
                trappistLandBar()
                sPrint("The cloud is made out of thick water with a lot of dust.")
                input("continue<ENTER>")
            case '3':
                sPrint("As you try to climb higher you slip and fall down the mountain")
                sPrint("You wake up 4 hours later")
                variables.hp -= 50
                return 0


trappist_1f()