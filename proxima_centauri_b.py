import variables
from variables import sPrint
import os
from random import randint

# 0: fieldGroundSample, 1: fieldAirQuality, 2: mountainWallSample, 3: mountainDrawings
proxima_checked = [0, 0, 0, 0]
proximaRad = 8

def KeplerPlanetBar():
    x = 0
    for i in range(len(proxima_checked)):
        if proxima_checked[i] == 1:
            x += 25
    print(f"Planet examination = {x:.2f}%")

def proxima_centauri_b():
    global proxima_checked
    if planet() == "dead":
        proxima_checked = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sPrint("You died.")
        sPrint("You lose all your progress on this planet and return to orbit.")
        input("continue <ENTER>")
        return 0

def planet():
    cls()
    choice1 = ''
    while choice1 != 'exit':
        choice1 = mountainOrField()

        match choice1:
            case '0':
                variables.hp = 100
                variables.O2 = 100
                variables.rad = 0
                sPrint("You successfully restocked")
            case '1':
                cls()
                choice2 = ''
                while choice2 != '0':
                    choice2 = fieldChoice()

                    match choice2:
                        case '1':
                            cls()
                            if proxima_checked[0] == 0:
                                sPrint("In a small tester device you've put in same sand.")
                                sPrint("After you started it the results are came:")
                                sPrint("RADIOACTIVE MATERIAL.")
                                proxima_checked[0] = 1
                                KeplerPlanetBar()
                                input("\ncontinue <ENTER>")
                            else:
                                sPrint("You've already did a ground sample check.")
                                input("\ncontinue <ENTER>")
                        case '2':
                            cls()
                            if proxima_checked[1] == 0:
                                sPrint("You've started the air quality tester.")
                                sPrint("Result: THE AIR IS NOT RADIOACTIVE.")
                                proxima_checked[1] = 1
                                KeplerPlanetBar()
                                input("\ncontinue <ENTER>")
                            else:
                                sPrint("You've already did a air quality check.")
                                input("\ncontinue <ENTER>")
            case '2':
                cls()
                choice3 = ''
                while choice3 != '0':
                    choice3 = mountainChoice()

                    match choice3:
                        case '1':
                            cls()
                            if proxima_checked[2] == 0:
                                sPrint("You've collected some sample from the wall.")
                                sPrint("You've putted it in a evidence bag.")
                                proxima_checked[2] = 1
                                KeplerPlanetBar()
                                input("\ncontinue <ENTER>")
                            else:
                                sPrint("You've already collected sample from the wall.")
                                input("\ncontinue <ENTER>")
                        case '2':
                            cls()
                            if proxima_checked[3] == 0:
                                sPrint("You started to examine the drawings.")
                                sPrint("You took a picture of every drawing.")
                                sPrint("You uploaded it to the evidence searching app.")
                                sPrint("There are no matchings.")
                                proxima_checked[3] = 1
                                KeplerPlanetBar()
                                input("\ncontinue <ENTER>")
                            else:
                                sPrint("You've already did a air quality check.")
                                input("\ncontinue <ENTER>")
                        case '3':
                            cls()
                            sPrint("As you digged deeper, you felt wind coming out from the wall.")
                            input("\ncontinue <ENTER>")

                            choice4 = ''
                            while choice4 != '0':
                                choice4 = mountainWind()

                                match choice4:
                                    case '1':
                                        cls()
                                        sPrint("As you got closer you've started to see cracks in the wall.")
                                        sPrint("You decided to break down the wall.")
                                        sPrint("You broke through and saw skeletons.")
                                        input("\ncontinue <ENTER>")
                                    case '2':
                                        cls()
                                        sPrint("As you turn your back you can see a small stream of liquid.")
                                        sPrint("You digged deeper towards the leak.")
                                        sPrint("You found lava.")
                                        input("\ncontinue <ENTER>")

                                        choice5 = ''
                                        while choice5 != '0':
                                            choice5 = mountainLava()

                                            match choice5:
                                                case '1':
                                                    cls()
                                                    sPrint("As you got closer to the lava, you burned yourself.")
                                                    sPrint("You panicked, and your oxygen decreasing rapidly.")
                                                    input("\ncontinue <ENTER>")


def mountainOrField():
    cls()
    variables.userInterface()
    variables.statUpdate(proximaRad)
    sPrint("You succesfully landed at the Proxima Centauri b.\n")

    print('exit - Exit from this planet')
    print('1 - Go to a open field')
    print('2 - Cave in the mountain near to you')
    print('0 - restock')

    return(input('Please choose a location: '))

def fieldChoice():
    cls()
    variables.userInterface()
    variables.statUpdate(proximaRad)
    sPrint("You arrived at the open field.\n")

    print('0 - Go back')
    print('1 - Collect ground sample')
    print('2 - Examine the air quality')

    return(input('Please choose: '))

def mountainChoice():
    cls()
    variables.userInterface()
    variables.statUpdate(proximaRad)
    sPrint("You've caved the mountains's surface.\n")

    print('0 - Go back')
    print('1 - Collect sample from the wall')
    print('2 - Examine drawings on the wall')
    print('3 - Dig deeper')

    return(input('Please choose: '))

def mountainWind():
    cls()
    variables.userInterface()
    variables.statUpdate(proximaRad)
    sPrint("Do you want to examine it?\n")

    print('0 - Go back')
    print('1 - Yes')
    print('2 - Not yet')

    return(input('Please choose: '))

def mountainLava():
    cls()
    variables.userInterface()
    variables.statUpdate(proximaRad)
    sPrint("Do you want to examine it?\n")

    print('0 - No, go back')
    print('1 - Yes')

    return(input('Please choose: '))

def cls():
    os.system('cls')