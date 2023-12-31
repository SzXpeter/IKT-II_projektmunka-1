import variables, os, time
from variables import sPrint, userInterface
#ocean sample, ocean bottom sample, swamp plant sample, swamp scan
LHSLand = [0, 0, 0, 0]
#sea serpent photo, amphitere scan, hydra scan, hydra photo, hydra egg scan, hydra egg photo, dragon egg scan, dragon egg photo, dragon scan, dragon photo
LHSAliens = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

LHSRad = 3

def LHSLandBar():
    x = 0
    for i in range(len(LHSLand)):
        if LHSLand[i] == 1:
            x += 25
    print(f"Land examination = {x:.2f}%")

def LHSAlienBar():
    x = 0
    for i in range(len(LHSAliens)):
        if LHSAliens[i] == 1:
            x += 10
    print(f"Alien examination = {x:.2f}%")

def lhs_1140b():
    global LHSLand, LHSAliens
    os.system("cls")
    sPrint("You succesfully landed on LHS 1140b.")
    input("continue <ENTER>")
    if sea_shore() == "dead":
        LHSLand = [0, 0, 0, 0]
        LHSAliens = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sPrint("You died.")
        sPrint("You lose all your progress on this planet and return to orbit.")
        input("continue <ENTER>")
        return 0
    
def sea_shore():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0' and v != 'leave':
            os.system("cls")
            userInterface()
            sPrint("You're at the sea shore.")
            print("\n\t1. Go into the water")
            print("\t2. Go into the swamp")
            print("\t3. Go towards the mountain")
            print("\t0. Repair and restock equipment")
            print("\tleave. Leave planet")
            v = input("choice: ")

        match v:
            case 'leave':
                sPrint("You left planet Trappist-1f.")
                input("continue <ENTER>")
                return 0
            case '1':
                if shallow_water() == "dead":
                    return "dead"
                if variables.statUpdate(LHSRad) == "dead":
                    return "dead"
            case '2':
                if outer_swamp() == "dead":
                    return "dead"
                if variables.statUpdate(LHSRad) == "dead":
                    return "dead"
            case '3':
                if bottom_mountain() == "dead":
                    return "dead"
                if variables.statUpdate(LHSRad) == "dead":
                    return "dead"
            case '0':
                variables.restock()

def shallow_water():
    global LHSLand
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in shallow water.")
            print("\n\t1. Take water sample")
            print("\t2. Take sample from the bottom")
            print("\t3. Go deeper")
            print("\t0. Go to the sea shore")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                LHSLand[0] = 1
                LHSLandBar()
                sPrint("The water seems to contain a lot of microorganisms.")
                input("continue<ENTER>")
            case '2':
                LHSLand[1] = 1
                LHSLandBar()
                sPrint("The bottom of the ocean is made up of a lot of clay.")
                input("continue<ENTER>")
            case '3':
                if deep_water() == "dead":
                    return "dead"
                if variables.statUpdate(LHSRad) == "dead":
                    return "dead"
                
def deep_water():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in deep water.")
            print("\n\t1. Do a scan")
            print("\t2. Turn on lights")
            print("\t0. Go back to shallow water")
            v = input("choice: ")

        match v :
            case '0':
                return 0
            case '1':
                sPrint("The scanner doesn't show anything interesting.")
                input("continue<ENTER>")
            case '2':
                sPrint("You turn on the lights.")
                sPrint("As you turn around you see a giant snake like creature with teeth looking straight at you.")
                input("continue<ENTER>")
                v = ''
                while v != '1' and v != '2' and v != '3':
                    print("\n\t1. Take photo")
                    print("\t2. Swim up")
                    print("\t3. Swim down")
                    v = input("choice: ")
                    
                match v :
                    case '1':
                        sPrint("As you try to take out your camera the serpent launches at you.")
                        return "dead"
                    case '2':
                        return swim_away()
                    case '3':
                        sPrint("You swim as fast as you can but an even bigger serpent appears below you and eats you alive.")
                        return "dead"
                
def swim_away():
    global LHSAliens
    os.system("cls")
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
        sPrint("You look back and see that the serpent has stopped chasing you.")
        input("continue <ENTER>")
        v = ''
        while v != 'y' and v != 'n':
            sPrint("Take photo?(y/n)")
            v = input("choice: ")
        if v == 'y':
            LHSAliens[0] = 1
            LHSAlienBar()
            sPrint("You take a photo and swim back to shallow water.")
            input("continue <ENTER>")
        return 0
    else:
        sPrint("You got caught.")
        sPrint("The serpent snapped you in half.")
        return "dead"

def outer_swamp():
    global LHSLand
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in outer swamp.")
            print("\n\t1. Scan the area")
            print("\t2. Collect plant sample")
            print("\t3. Go deeper into the swamp")
            print("\t0. Go to the sea shore")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                LHSLand[2] = 1
                LHSLandBar()
                sPrint("The swamp is dense with trees and the gound is loose.")
                input("continue<ENTER>")
            case '2':
                LHSLand[3] = 1
                LHSLandBar()
                sPrint("These plants are similar to earths.")
                input("continue<ENTER>")
            case '3':
                if inner_swamp() == "dead":
                    return "dead"
                if variables.statUpdate(LHSRad) == "dead":
                    return "dead"

def inner_swamp():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in inner swamp. And you come around a lake.")
            print("\n\t1. Go around it")
            print("\t2. Go across using the rocks")
            print("\t3. Go across using the logs")
            print("\t0. Go back to the outer swamps")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                sPrint("You go around the lake safely and quickly.")
                sPrint("You look back and see two eyes looking at you from between the logs.")
                input("continue <ENTER>")
                if amphitere() == "dead":
                    return "dead"
            case '2':
                if math_rocks() == "dead":
                    return "dead"
                sPrint("You get across the lake safely and quickly.")
                sPrint("You look back and see two eyes looking at you from between the logs.")
                if amphitere() == "dead":
                    return "dead"
                else:
                    if variables.statUpdate(LHSRad) == "dead":
                        return "dead"
                    return 0
            case '3':
                sPrint("As you jump across the lake log to log, one of them moves out of you and rips you to pieces.")
                return "dead"
            
def math_rocks():
    math_questions = ["log2(64) * 6 = ", "9^150/300", "x^2 + 10x = -25, x=?", "x√256 = 4, x = ?", "2 ^ x = 32 768, x = ?"]
    math_answers = ["36", "3", "-5", "4", "15"]
    os.system("cls")
    sPrint("What are the answers: ")
    for i in range(5):
        print(math_questions[i])
        if input() == math_answers[i]:
            print("Correct!")
        else:
            sPrint("You slipped and fell into the water and you broke your neck.")
            return "dead"
    sPrint("You successfully got across the water.")
    input("continue<ENTER>")

def amphitere():
    global LHSAliens
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're in the inner swamp. And you are looking at a beast.")
            print("\n\t1. Take photo")
            print("\t2. Scan it")
            print("\t0. Go back to the outer swamps")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                sPrint("As the flash flashes it launches at you.")
                return "dead"
            case '2':
                sPrint("It looks like some type of amphitere.")
                LHSAliens[1] = 1
                LHSAlienBar()
                sPrint("It starts sliding towards you.")
                input("continue<ENTER>")
                v = ''
                while v != '1' and v != '2' and v != '3':
                    os.system("cls")
                    userInterface()
                    sPrint("You're in the inner swamp. And you are looking at an amphitere.")
                    print("\n\t1. Run into the fields")
                    print("\t2. Stand still")
                    print("\t3. Run into the woods")
                    v = input("choice: ")
                    match v :
                        case '1':
                            sPrint("You try to run into the fields.")
                            sPrint("But the thing starts flying and it easily catches up to you.")
                            return "dead"
                        case '2':
                            sPrint("You stand still and the thing slides closer and launches at you.")
                            return "dead"
                        case '3':
                            sPrint("You run into the woods and thing starts flying and chasing you.")
                            sPrint("You keep on running until you hear a clashing sound above you.")
                            sPrint("You return to the sea shore.")
                            input("continue<ENTER>")
                            return 0

def bottom_mountain():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're at the bottom of the mountain.")
            print("\n\t1. Climb up the mountain.")
            print("\t2. Go around the mountain")
            print("\t0. Go to the sea shore")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                sPrint("As you go higher you notice something fly by.")
                input("continue<ENTER>")
                if upper_mountain() == "dead":
                    return "dead"
                else:
                    if variables.statUpdate(LHSRad) == "dead":
                        return "dead"
                    return 0
            case '2':
                if cave_entrance() == "dead":
                    return "dead"
                if variables.statUpdate(LHSRad) == "dead":
                    return "dead"
                
def upper_mountain():
    global LHSAliens
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're up the mountain. You see a nest.")
            print("\n\t1. Take photo")
            print("\t2. Scan it")
            print("\t3. Go closer")
            print("\t0. Climb down")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                sPrint("You take a photo of the eggs.")
                LHSAliens[7] = 1
                LHSAlienBar()
                input("continue<ENTER>")
            case '2':
                sPrint("You scan the eggs and see some smol creatures inside.")
                LHSAliens[6] = 1
                LHSAlienBar()
                input("continue<ENTER>")
            case '3':
                sPrint("You go closer to the eggs and suddenly a dragon lands before you.")
                input("continue<ENTER>")
                if dragon() == "dead":
                    return "dead"
                else:
                    return "dragon"
                
def dragon():
    global LHSAliens
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '2':
            os.system("cls")
            userInterface()
            sPrint("You're up the mountain face to face with a dragon.")
            print("\n\t1. Stand still")
            print("\t2. Run")
            v = input("choice: ")
        match v :
            case '1':
                sPrint("You stand still and the dragon slaps you off the mountain.")
                return "dead"
            case '2':
                sPrint("You start running down the mountain the dragon chasing right behind you.")
                v = ''
                while v != '1' and v != '2':
                    print("\n\t1. Run into the woods")
                    print("\t2. Run into the open fields")
                    v = input("choice: ")
                match v :
                    case '1':
                        v = ''
                        sPrint("You run into the woods.")
                        sPrint("The dragon tries to dive for you but it gets stuck on the trees.")
                        input("continue<ENTER>")
                        while v != '0':
                            v = ''
                            while v != '1' and v != '2' and v != '0':
                                os.system("cls")
                                userInterface()
                                sPrint("You're standing in front of the dragon.")
                                print("\n\t1. Take photo")
                                print("\t2. Scan it")
                                print("\t0. Leave")
                                v = input("choice: ")
                            match v :
                                case '0':
                                    return "dragon"
                                case '1':
                                    sPrint("You take a photo of the dragon.")
                                    LHSAliens[9] = 1
                                    LHSAlienBar()
                                    input("continue<ENTER>")
                                case '2':
                                    sPrint("You scan the dragon.")
                                    LHSAliens[8] = 1
                                    LHSAlienBar()
                                    input("continue<ENTER>")
                    case '2':
                        sPrint("You run into the open fields and the dragon torches you.")
                        return "dead"
                    
def cave_entrance():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're at the bottom of the mountain. You found a cave.")
            print("\n\t1. Go in")
            print("\t0. Go back around")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                cave()

def cave():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v !='2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're inside the cave.")
            print("\n\t1. Go into chamber 1")
            print("\n\t2. Go into chamber 2")
            print("\n\t3. Go into chamber 3")
            print("\t0. Go outside")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                hydra()
            case '2':
                hydra_eggs()
            case '3':
                sPrint("You see a bunch of thorn flesh.")
                input("continue<ENTER>")

def hydra():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v !='2' and v != '3' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're inside the cave. You see some white spots in the dark.")
            print("\n\t1. Do a scan")
            print("\n\t2. Take photo")
            print("\n\t3. Go closer")
            print("\t0. Go back")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                sPrint("The creature seems to be a hydra.")
                LHSAliens[2] = 1
                LHSAlienBar()
                input("continue<ENTER>")
            case '2':
                sPrint("You take a photo and th thing twitches but doesn't wake up.")
                LHSAliens[3] = 1
                LHSAlienBar()
                input("continue<ENTER>")
            case '3':
                sPrint("As you go closer the thing wakes up and thorns you to pieces.")
                return "dead"
            
def hydra_eggs():
    if variables.statUpdate(LHSRad) == "dead":
        return "dead"
    Exit = False
    while Exit == False:
        v = ''
        while v != '1' and v !='2' and v != '0':
            os.system("cls")
            userInterface()
            sPrint("You're inside the cave. You see eggs.")
            print("\n\t1. Do a scan")
            print("\n\t2. Take photo")
            print("\t0. Go back")
            v = input("choice: ")
        match v :
            case '0':
                return 0
            case '1':
                sPrint("There are smol three-headed cretures inside them.")
                LHSAliens[4] = 1
                LHSAlienBar()
                input("continue<ENTER>")
            case '2':
                sPrint("You take a photo of the eggs.")
                LHSAliens[5] = 1
                LHSAlienBar()
                input("continue<ENTER>")
