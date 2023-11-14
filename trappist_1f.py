import variables, os, time
from variables import sPrint, userInterface
#sea shore air, cloud sample, ice sample, water sample, bottom oceans
trappist1fLand = [0, 0, 0, 0, 0]
#plants, photo, bottom oceans
trappist1fAliens = [0, 0, 0]

trappistRad = 4

def trappistLandBar():
    x = 0
    for i in range(len(trappist1fLand)):
        if trappist1fLand[i] == 1:
            x += 20
    print(f"Land examination = {x}%")

def trappistAlienBar():
    x = 0
    for i in range(len(trappist1fAliens)):
        if trappist1fAliens == [1, 1, 1]:
            x = 100
        elif trappist1fAliens[i] == 1:
            x += 100/3
    print(f"Alien examination = {x}%")

def trappist_1f():
    global trappist1fLand, trappist1fAliens
    os.system("cls")
    sPrint("You succesfully landed on Trappist-1f.")
    input("continue <ENTER>")
    if sea_shore() == "dead":
        os.system("cls")
        userInterface()
        trappist1fLand = [0, 0, 0, 0, 0]
        trappist1fAliens = [0, 0, 0]
        sPrint("You died.")
        sPrint("You lose all your progress on this planet and return to orbit.")
        input("continue <ENTER>")
        return 0
    

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
                return 0
            case '1':
                trappist1fLand[0] = 1
                trappistLandBar()
                sPrint("The air seems to contain a lot of oxygen.")
                input("continue <ENTER>")
                v = ''
                while v != 'y' and v != 'n':
                    sPrint("Do you want to take off your helmet?(y/n)")
                    v = input("choice: ")
                if v == 'y':
                    variables.hp -= 5
                    sPrint("You take a deep breath.\nThe air is thick with steam.\nIt almost burns your face so you put back your helmet.")
                    input("continue <ENTER>")
            case '2':
                if flat_fields() == "dead":
                    return 0
                if variables.statUpdate(trappistRad) == "dead":
                    return "dead"
            case '3':
                if bottom_mountain() == "dead":
                    return "dead"
                if variables.statUpdate(trappistRad) == "dead":
                    return "dead"
            case '0':
                variables.restock()


def flat_fields():
    if variables.statUpdate(trappistRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in the middle of the sea of ice.")
            print("\n\t1. Collect ice sample")
            print("\t2. Scan your surroundings")
            print("\t3. Crack the ice")
            print("\t0. Go to the sea shore")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                trappist1fLand[2] = 1
                trappistLandBar()
                sPrint("The ice has a loose structure.")
                input("continue<ENTER>")
            case '2':
                sPrint("The ice is thinner here.")
                input("continue<ENTER>")
            case '3':
                sPrint("You successfully created a hole.")
                v = ''
                while v != 'y' and v != 'n':
                    sPrint("Do you want to jump in?(y/n)")
                    v = input("choice: ")
                if v == 'y':
                    if starting_water() == "dead":
                        return "dead"
                    if variables.statUpdate(trappistRad) == "dead":
                        return "dead"

def starting_water():
    if variables.statUpdate(trappistRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in upper waters.")
            print("\n\t1. Collect water sample")
            print("\t2. Go under the mountain")
            print("\t3. Go deeper down")
            print("\t0. Go up to the sea of ice")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                trappist1fLand[3] = 1
                trappistLandBar()
                sPrint("The water is oxigen deprived.")
                input("continue<ENTER>")
            case '2':
                sPrint("As you swim down you notice something moving.")
                sPrint("You try to swim closer, but suddenly you feel a shock running trough you and you black out.")
                sPrint("After you regain consciousness you realize that whatever was there it is gone.")
                input("continue<ENTER>")
            case '3':
                if deep_waters() == "dead":
                    return "dead"
                if variables.statUpdate(trappistRad) == "dead":
                    return "dead"

def deep_waters():
    if variables.statUpdate(trappistRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in deep waters.")
            print("\n\t1. Collect sample from the bottom floor")
            print("\t2. Swim further away")
            print("\t0. Go up")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                trappist1fLand[4] = 1
                trappist1fAliens[2] = 1
                trappistLandBar()
                trappistAlienBar()
                sPrint("You find rich soil and alien bones.")
                input("continue<ENTER>")
            case '2':
                if far_away_waters() == "dead":
                    return "dead"
                if variables.statUpdate(trappistRad) == "dead":
                    return "dead"

def far_away_waters():
    if variables.statUpdate(trappistRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in far away waters.")
            print("\n\t1. Collect plants")
            print("\t2. Do a scan")
            print("\t0. Go up")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                trappist1fAliens[1] = 1
                trappistAlienBar()
                sPrint("These plants have been chewed.")
                input("continue<ENTER>")
            case '2':
                sPrint("You do a scan and notice a school of eel like creatures.")
                v = ''
                while v != 'y' and v != 'n':
                    sPrint("Take a photo(y/n)")
                    v = input("choice: ")
                if v == 'y':
                    return swim_away()

def swim_away():
    global trappist1fAliens, trappist1fLand
    os.system("cls")
    trappist1fAliens[0] = 1
    trappistAlienBar()
    sPrint("As you take the photo the aliens start swimming straight at you.")
    sPrint("You need to get away fast.")
    sPrint("To do that you need to spam <ENTER>.")
    time.sleep(2)
    print("GO")
    startTime = time.time()
    score = 0
    while time.time() - startTime < 5:
        input()
        score += 1
    if score >= 20:
        sPrint("You managed to get away.")
        return 0
    else:
        sPrint("You got caught.")
        sPrint("The aliens shocked you to death.")
        return "dead"

def bottom_mountain():
    if variables.statUpdate(trappistRad) == "dead":
        return "dead"
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
                if top_mountain() == "dead":
                    return "dead"
                if variables.statUpdate(trappistRad) == "dead":
                    return "dead"

def top_mountain():
    if variables.statUpdate(trappistRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're at the top of the mountain.")
            print("\n\t1. Shout")
            print("\t2. Take sample from the cloud")
            print("\t3. Climb higher up the mountain")
            print("\t0. Climb down")
            v = input("choice: ")

        match v :
            case '0':
                return 0
            case '1':
                shout = input("What do you want to shout: ")
                for i in range(4):
                    echo = ''
                    for j in range(len(shout)-int(len(shout)/((5.5-i)/2)+0.5)):
                        echo += shout[len(shout)-j-1]
                    echo = echo[::-1]
                    print(echo)
                input("continue<ENTER>")
            case '2':
                trappist1fLand[1] = 1
                trappistLandBar()
                sPrint("The cloud is made out of thick water with a lot of dust.")
                input("continue<ENTER>")
            case '3':
                sPrint("As you try to climb higher you slip and fall down the mountain")
                sPrint("You wake up 4 hours later")
                variables.hp -= 70
                variables.statUpdate(40, 50)
                input("continue<ENTER>")
                return 0