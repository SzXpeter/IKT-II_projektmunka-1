import variables
from variables import sPrint
import os
from random import randint

# 0: water sample top, 1: sample sea bottom, 2: sea life, 3: abandoned house material, 4: kitchen's technology, 5: living room furniture, 6: living room tech, 7: explosion hole
# 8: explosion hole measurement, 9: search remains, 10: shadow
# 11: high b. basement, 12:high b.r1bath,13: high b.r1liv,14:high b.r2
kepler_checked = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def KeplerPlanetBar():
    x = 0
    for i in range(len(kepler_checked)):
        if kepler_checked == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            x = 100
        elif kepler_checked[i] == 1:
            x += 100/15
    print(f"Planet examination = {x:.2f}%")

def kepler_452b():
    global kepler_checked
    if planet() == "dead":
        kepler_checked = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sPrint("You died.")
        sPrint("You lose all your progress on this planet and return to orbit.")
        input("continue <ENTER>")
        return 0
    
keplerRad = 6

def planet():
    choice1 = ''
    while choice1 !='exit':
        choice1 = seaOrCityMenu()
        match choice1:
            case '0':
                variables.hp = 100
                variables.O2 = 100
                variables.rad = 0
                sPrint("You successfully restocked")
            case '1':
                choice2 = ''
                while choice2 != '0':
                    choice2 = sea1_water()

                    match choice2:
                        case '1':
                            if kepler_checked[0] == 0:
                                cls()
                                sPrint("You took 1 liter sample from the sea.")
                                sPrint("You went for a fast check with your gadget.")
                                sPrint("You went for a fast check with your gadget.")
                                sPrint("The sample results: THE WATER IS HIGHLY RADIOACTIVE", 25)
                                kepler_checked[0] = 1
                                KeplerPlanetBar()
                                input("\ncontinue <ENTER>")
                                
                            else:
                                cls()
                                print("You've already did a top water sample check.")
                                input("\ncontinue <ENTER>")
                        case '2':
                            choice3 = ''
                            while choice3 != '0':
                                choice3 = sea2_water()
                                
                                match choice3:
                                    case '1':
                                        if kepler_checked[1] == 0:
                                            cls()
                                            sPrint("You collected some sand and rock from the bottom of the sea.")
                                            sPrint("These samples aren't radioactive.")
                                            kepler_checked[1] = 1
                                            KeplerPlanetBar()
                                            input("\ncontinue <ENTER>")
                                        else:
                                            cls()
                                            print("You've already did a bottom sample check.")
                                            input("\ncontinue <ENTER>")
                                    case '2':
                                        if kepler_checked[2] == 0:
                                            cls()
                                            sPrint("You're scanning for sea life.")
                                            sPrint("The scan results are showing microorganisms.")
                                            kepler_checked[2] = 1
                                            KeplerPlanetBar()
                                            input("\ncontinue <ENTER>")
                                        else:
                                            cls()
                                            print("You've already did a sea life scan.")
                                            input("\ncontinue <ENTER>")
            case '2':
                choice3 = ''
                while choice3 != '0':
                    choice3 = city1_choice()

                    match choice3:
                        case '1':
                            choice4 = ''
                            while choice4 != '0':
                                choice4 = city2_choice()
                                
                                match choice4:
                                    case '1':
                                        if kepler_checked[3] == 0:
                                            cls()
                                            sPrint("You are scratching down some material from the wall.")
                                            sPrint("You put it in a vacuum technology examine system.")
                                            sPrint("The results: SOME ALIENS WERE HERE")
                                            kepler_checked[3] = 1
                                            KeplerPlanetBar()
                                            input("\ncontinue <ENTER>")
                                        else:
                                            cls()
                                            print("You've already examined the house material.")
                                            input("\ncontinue <ENTER>")
                                    case '2':
                                        if kepler_checked[4] == 0:
                                            cls()
                                            sPrint("You are trying to examine the kitchen's appliances.")
                                            sPrint("You found a sticker with the year of 1999")
                                            kepler_checked[4] = 1
                                            KeplerPlanetBar()
                                            input("\ncontinue <ENTER>")
                                        else:
                                            cls()
                                            print("You've already examined the house material.")
                                            input("\ncontinue <ENTER>")
                                    case '3':
                                        choice5 = ''
                                        while choice5 != '0':
                                            choice5 = city3_livingRoom()

                                            match choice5:
                                                case '1':
                                                    if kepler_checked[5] == 0:
                                                        cls()
                                                        sPrint("You are looking over all the furnitures left here.")
                                                        kepler_checked[5] = 1
                                                        sPrint("You didn't find anything.")
                                                        KeplerPlanetBar()
                                                        input("\ncontinue <ENTER>")
                                                    else:
                                                        cls()
                                                        print("You've already examined the living room's furnitures.")
                                                        input("\ncontinue <ENTER>")
                                                case '2':
                                                    if kepler_checked[6] == 0:
                                                        cls()
                                                        sPrint("You are looking for electronics to examine them.")
                                                        sPrint("You found a telephone, an old light bulb, and a clock.")
                                                        sPrint("You found stickers from 1991, 1999 and 2001")
                                                        kepler_checked[6] = 1
                                                        KeplerPlanetBar()
                                                        input("\ncontinue <ENTER>")
                                                    else:
                                                        cls()
                                                        print("You've already examined the living room's technology.")
                                                        input("\ncontinue <ENTER>")
                        case '2':
                            choice6 = ''
                            while choice6 != '0':
                                choice6 = city4_innerCity()

                                match choice6:
                                    case '1':
                                        cls()
                                        sPrint("You've found an explosion hole.")
                                        kepler_checked[7] = 1
                                        KeplerPlanetBar()
                                        input("\ncontinue <ENTER>")

                                        choice7 = ''
                                        while choice7 != '0':
                                            choice7 = city5_innerCity()

                                            match choice7:
                                                case '1':
                                                    if kepler_checked[8] == 0:
                                                        cls()
                                                        sPrint("You're measuring the explosion hole.")
                                                        sPrint("The explosion hole's depth: 15 meters")
                                                        sPrint("The explosion hole's radius: 200 meters")
                                                        sPrint("The explosion type: ATOMIC BOMB", 70)
                                                        kepler_checked[8] = 1
                                                        KeplerPlanetBar()
                                                        input("\ncontinue <ENTER>")
                                                    else:
                                                        cls()
                                                        print("You've already measured the explosion hole.")
                                                        input("\ncontinue <ENTER>")
                                                case '2':
                                                    if kepler_checked[9] == 0:
                                                        cls()
                                                        sPrint("You're searching for survivors.")
                                                        sPrint("Since this was an atomic bomb, the probability is very low.")
                                                        percentageSurvivors = randint(0,100)
                                                        if percentageSurvivors > 90:
                                                            sPrint("You've found some highly injured, no signs of human being.")
                                                        else:
                                                            sPrint("You've found nothing.")
                                                        kepler_checked[9] = 1
                                                        KeplerPlanetBar()
                                                        input("\ncontinue <ENTER>")
                                                    else:
                                                        sPrint("You've already checked for survivors.")
                                                        input("\ncontinue <ENTER>")
                                    case '2':
                                        cls()
                                        choice9 = ''
                                        while choice9 != '0':
                                            choice9 = city7_otherSide()

                                            match choice9:
                                                case '1':
                                                    choice10 = ''
                                                    while choice10 != '0':
                                                        choice10 = city8_highBuilding()

                                                    match choice10:
                                                        case '1':
                                                            cls()
                                                            if kepler_checked[11] == 0:
                                                                sPrint("You are going down to the basement.")
                                                                sPrint("You hear some weird noise, and you see some shadows moving to the opposite direction.")
                                                                sPrint("When you got down to the basement, everything disappeared, you found nothing.")
                                                                kepler_checked[11] = 1
                                                                KeplerPlanetBar()
                                                                input("\ncontinue <ENTER>")
                                                            else:
                                                                sPrint("You've already checked the basement.")
                                                                input("\ncontinue <ENTER>")
                                                        case '2':
                                                            cls()
                                                            choice11 = ''
                                                            while choice11 != '0':
                                                                choice11 = city9_highFloor()

                                                                match choice11:
                                                                    case '1':
                                                                        cls()
                                                                        choice12 = ''
                                                                        while choice12 != '0':
                                                                            choice12 = city10_highRoom1()

                                                                            match choice12:
                                                                                case '1':
                                                                                    cls()
                                                                                    if kepler_checked[12] == 0:
                                                                                        sPrint("You found a lot of acid, and a dead Alien.")
                                                                                        kepler_checked[12] = 1
                                                                                        KeplerPlanetBar()
                                                                                        input("\ncontinue <ENTER>")
                                                                                    else:
                                                                                        sPrint("You've already checked the bathroom.")
                                                                                        input("\ncontinue <ENTER>")
                                                                                case '2':
                                                                                    cls()
                                                                                    if kepler_checked[13] == 0:
                                                                                        sPrint("There is a lot of blood on the bed.")
                                                                                        kepler_checked[13] = 1
                                                                                        KeplerPlanetBar()
                                                                                        input("\ncontinue <ENTER>")
                                                                                    else:
                                                                                        sPrint("You've already checked the living room.")
                                                                                        input("\ncontinue <ENTER>")
                                                                    case '2':
                                                                        cls()
                                                                        if kepler_checked[14] == 0:
                                                                            sPrint("In the second romm the bathroom's door was jammed.")
                                                                            sPrint("For your own safety you left the room.")
                                                                            kepler_checked[14] = 1
                                                                            KeplerPlanetBar()
                                                                            input("\ncontinue <ENTER>")
                                                                        else:
                                                                            sPrint("You've already checked this room.")
                                                case '2':
                                                    cls()
                                                    choice13 = ''
                                                    while choice13 != '0':
                                                        choice13 = city11_flatRooms()

                                                        match choice13:
                                                            case '1':
                                                                cls()
                                                                sPrint("You checked the bed and a desk.")
                                                                sPrint("You've found nothing interesting.")
                                                                input("\ncontinue <ENTER>")
                                                            case '2':
                                                                cls()
                                                                sPrint("This is an empty room, with a lot of scrap.")
                                                                input("\ncontinue <ENTER>")
                                                                
                                if kepler_checked[7] == 1 and kepler_checked[10] == 0:
                                    cls()
                                    choice8 = ''
                                    if choice8 != '1' or choice8 != '2':
                                        choice8 = city6_innerCityShadow()

                                        match choice8:
                                            case '1':
                                                cls()
                                                sPrint("As you go closer to the wall some Aliens running away.")
                                                kepler_checked[10] = 1
                                                KeplerPlanetBar()
                                                input("\ncontinue <ENTER>")
                                            case '2':
                                                cls()
                                                sPrint("As you turned back an Alien attacked you.")
                                                kepler_checked[10] = 1
                                                KeplerPlanetBar()
                                                input("\ncontinue <ENTER>")     
def seaOrCityMenu():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You succesfully landed at the Kepler-452b landing site.\n")

    print('exit - Exit from this planet')
    print('1 - Go to the sea shore')
    print('2 - Go into the city')
    print('0 - restock')

    return(input('Please choose a location: '))

def sea1_water():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are at the sea shore.\n")

    print('0 - Go back to the landing site')
    print('1 - Take water sample from the top')
    print('2 - Go into the water')

    return(input('Please choose: '))

def sea2_water():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in the water.\n")

    print('0 - Go back to the shore')
    print('1 - Collect sample from the sea bottom')
    print('2 - Scan for sea life')

    return(input('Please choose: '))

def city1_choice():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are at the outer city.\n")

    print('0 - Go back to the landing site')
    print('1 - Go to the abandoned house')
    print('2 - Go further in the city')

    return(input('Please choose: '))

def city2_choice():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in the abandoned house.\n")

    print('0 - Go out')
    print('1 - Examine the house material')
    print("2 - Examine the kitchen's technology")
    print("3 - Go to the living room")

    return(input('Please choose: '))

def city3_livingRoom():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in the abandoned house.\n")

    print('0 - Go out')
    print('1 - Examine the furniture')
    print("2 - Examine the living room's technology")

    return(input('Please choose: '))

def city4_innerCity():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in the Inner City.\n")

    print('0 - Go back to the outer city')
    print('1 - Examine a explosion hole')
    print("2 - Go to the other side of the city")

    return(input('Please choose: '))

def city5_innerCity():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are at the explosion hole.\n")

    print('0 - Go back')
    print('1 - Measure the hole')
    print("2 - Search for remain lifes")

    return(input('Please choose: '))

def city6_innerCityShadow():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You see a strange shadow on the wall infront of you.")

    print('1 - Go and examine the shadow')
    print("2 - Move on")

    return(input('Please choose: '))

def city7_otherSide():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are at the other side of the city.")

    print('0 - Go back')
    print('1 - Investigate the high building')
    print("2 - Investigate the flat building")

    return(input('Please choose: '))

def city8_highBuilding():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in the high building.")

    print('0 - Go back')
    print('1 - Check basement')
    print("2 - Check 1st floor")

    return(input('Please choose: '))

def city9_highFloor():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are at the high building's first floor.")

    print('0 - Go back')
    print('1 - Check Room 1')
    print("2 - Check Room 2")

    return(input('Please choose: '))

def city10_highRoom1():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in Room 1.")

    print('0 - Go back')
    print('1 - Check bathroom')
    print("2 - Examine the living room")

    return(input('Please choose: '))

def city11_flatRooms():
    cls()
    variables.userInterface()
    variables.statUpdate(keplerRad)
    sPrint("You are in the flat building.")

    print('0 - Go back')
    print('1 - Check Room 1')
    print('2 - Check Room 2')

    return(input('Please choose: '))

def cls():
    os.system('cls')
