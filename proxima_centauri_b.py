import variables
from variables import sPrint
import os
from random import randint

# 0: fieldGroundSample, 1: fieldAirQuality, 2: mountainWallSample, 3: mountainDrawings
proxima_checked = [0, 0, 0, 0]

def proxima_centauri_b():
    cls()
    choice1 = ''
    while choice1 != 'exit':
        choice1 = mountainOrField()

        match choice1:
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
                                input("\ncontinue <ENTER>")
                            else:
                                sPrint("You've already did a air quality check.")
                                input("\ncontinue <ENTER>")
                        case '3':
                            cls()
                            sPrint("As you digged deeper, you felt wind coming out from the wall.")



def mountainOrField():
    sPrint("You succesfully landed at the Proxima Centauri b.\n")

    print('exit - Exit from this planet')
    print('1 - Go to a open field')
    print('2 - Cave in the mountain near to you')

    return(input('Please choose a location: '))

def fieldChoice():
    sPrint("You arrived at the open field.\n")

    print('1 - Collect ground sample')
    print('2 - Examine the air quality')

    return(input('Please choose: '))

def mountainChoice():
    sPrint("You've caved the mountains's surface.\n")

    print('1 - Collect sample from the wall')
    print('2 - Examine drawings on the wall')
    print('3 - Dig deeper')

    return(input('Please choose: '))

def cls():
    os.system('cls')