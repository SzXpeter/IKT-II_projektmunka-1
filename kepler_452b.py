import variables
from variables import sPrint
import os

# 0: water sample top, 1: sample sea bottom, 2: sea life, 3: abandoned house material, 4: kitchen's technology
kepler_checked = [0, 0, 0, 0]
kepler_note = ''

def kepler_452b():
    global kepler_note

    choice1 = ''
    while choice1 !='0':
        choice1 = seaOrCityMenu()

        match choice1:
            case 'n':
                cls()
                print("The notes from this planet: \n")
                sPrint(kepler_note, 80)
                input('\nPress ENTER to continue...')
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
                                kepler_note += 'The water on this planet is highly radioactive, '
                                input('\nPress ENTER to continue...')
                                
                            else:
                                cls()
                                print("You've already did a top water sample check.")
                                input('\nPress ENTER to continue...')
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
                                            kepler_note += 'the sample from the bottom of the sea did not came back as radioactive, '
                                            input('\nPress ENTER to continue...')
                                        else:
                                            cls()
                                            print("You've already did a bottom sample check.")
                                            input('\nPress ENTER to continue...')
                                    case '2':
                                        if kepler_checked[2] == 0:
                                            cls()
                                            sPrint("You're scanning for sea life.")
                                            sPrint("The scan results are showing microorganisms.")
                                            kepler_checked[2] = 1
                                            kepler_note += 'in the sea there is life in the from of microorganisms, '
                                            input('\nPress ENTER to continue...')
                                        else:
                                            cls()
                                            print("You've already did a sea life scan.")
                                            input('\nPress ENTER to continue...')
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
                                            sPrint("The results: Some aliens were here.")
                                            kepler_checked[3] = 1
                                            kepler_note += 'there are signs of aliens in the abandoned house at the outer city area, '
                                            input('\nPress ENTER to continue...')
                                        else:
                                            cls()
                                            print("You've already examined the house material.")
                                            input('\nPress ENTER to continue...')
                                    case '2':
                                        if kepler_checked[4] == 0:
                                            cls()
                                            sPrint("You are trying to examine the kitchen's appliances.")
                                            sPrint("You found a sticker with the year of 1999")
                                            kepler_checked[4] = 1
                                            kepler_note += 'found the sticker with the year 1999 on it, '
                                            input('\nPress ENTER to continue...')
                                        else:
                                            cls()
                                            print("You've already examined the house material.")
                                            input('\nPress ENTER to continue...')
                                    case '3':
                                        choice5 = ''
                                        while choice5 != '0':
                                            choice5 = city3_livingRoom()
                                            

def seaOrCityMenu():
    cls()
    sPrint("You succesfully landed at the Kepler-452b landing site.\n")

    print('1 - Go to the sea shore')
    print('2 - Go into the city')
    print('n - Notes from the planet')

    return(input('Please choose a location: '))

def sea1_water():
    cls()
    sPrint("You are at the sea shore.\n")

    print('0 - Go back to the landing site')
    print('1 - Take water sample from the top')
    print('2 - Go into the water')

    return(input('Please choose: '))

def sea2_water():
    cls()
    sPrint("You are in the water.\n")

    print('0 - Go back to the shore')
    print('1 - Collect sample from the sea bottom')
    print('2 - Scan for sea life')

    return(input('Please choose: '))

def city1_choice():
    cls()
    sPrint("You are at the outer city.\n")

    print('0 - Go back to the landing site')
    print('1 - Go to the abandoned house')
    print('2 - Go further in the city')

    return(input('Please choose: '))

def city2_choice():
    cls()
    sPrint("You are in the abandoned house.\n")

    print('0 - Go out')
    print('1 - Examine the house material')
    print("2 - Examine the kitchen's technology")
    print("3 - Go to the living room")

    return(input('Please choose: '))

def city3_livingRoom():
    cls()
    sPrint("You are in the abandoned house.\n")

    print('0 - Go out')
    print('1 - Examine the house material')
    print("2 - Examine the kitchen's technology")
    print("3 - Go to the living room")

    return(input('Please choose: '))

def cls():
    os.system('cls')

kepler_452b()