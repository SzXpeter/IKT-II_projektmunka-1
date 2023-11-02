import variables
from variables import sPrint
import os
from random import randint

# 0: water sample top, 1: sample sea bottom, 2: sea life, 3: abandoned house material, 4: kitchen's technology, 5: living room furniture, 6: living room tech, 7: explosion hole, 8: explosion hole measurement, 9: search remains, 10: shadow
kepler_checked = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
                input("\ncontinue <ENTER>")
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
                                kepler_note += 'The top of the sea water on this planet is highly radioactive; '
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
                                            kepler_note += 'the sample from the bottom of the sea did not came back as radioactive; '
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
                                            kepler_note += 'in the sea there is life in the form of microorganisms; '
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
                                            kepler_note += 'there are signs of aliens in the abandoned house at the outer city area; '
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
                                            kepler_note += 'found the sticker with the year 1999 on it; '
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
                                                        kepler_note += 'more stickers from 1991, 1999 and 2001; '
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
                                        kepler_note += 'an explosion hole found in the city; '
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
                                                        kepler_note += 'the explosion hole depth: 15 meters, radius: 200 meters, it was an atomic bomb; '
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
                                                            kepler_note += 'you have found some highly injured being, probably aliens; '
                                                        else:
                                                            sPrint("You've found nothing.")
                                                            kepler_note += 'no signs of survivors; '
                                                        input("\ncontinue <ENTER>")
                                    case '2':
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
                                                            sPrint("You are going down to the basement.")
                                                            sPrint("You hear some weird noise, and you see some shadows moving to the opposite direction.")
                                                            sPrint("When you got down to the basement, everything disappeared, you found nothing.")
                                                            kepler_note += 'in a high building basement found nothing; '
                                                            input("\ncontinue <ENTER>")
                                                    
                                                    
                                if kepler_checked[7] == 1:
                                    cls()
                                    choice8 = ''
                                    while choice8 != '0':
                                        choice8 = city6_innerCityShadow()

                                        match choice8:
                                            case '1':
                                                cls()
                                                sPrint("As you go closer to the wall some Aliens running away.")
                                                kepler_note += 'there is a big chance of aliens are still lives here; '
                                                input("\ncontinue <ENTER>")
                                            case '2':
                                                cls()
                                                sPrint("As you turned back an Alien attacked you.")
                                                kepler_note += 'there is still aliens alive, and they could be agressive; '
                                                input("\ncontinue <ENTER>")     
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
    print('1 - Examine the furniture')
    print("2 - Examine the living room's technology")

    return(input('Please choose: '))

def city4_innerCity():
    cls()
    sPrint("You are in the Inner City.\n")

    print('0 - Go back to the outer city')
    print('1 - Examine a explosion hole')
    print("2 - Go to the other side of the city")

    return(input('Please choose: '))

def city5_innerCity():
    cls()
    sPrint("You are at the explosion hole.\n")

    print('0 - Go back')
    print('1 - Measure the hole')
    print("2 - Search for remain lifes")

    return(input('Please choose: '))

def city6_innerCityShadow():
    cls()
    sPrint("You see a strange shadow on the wall infront of you.")

    print('1 - Go see the shadow')
    print("2 - Move on")

    return(input('Please choose: '))

def city7_otherSide():
    cls()
    sPrint("You are at the other side of the city.")

    print('0 - Go back')
    print('1 - Investigate the high building')
    print("2 - Investigate the flat building")

    return(input('Please choose: '))

def city8_highBuilding():
    cls()
    sPrint("You are in the high building.")

    print('0 - Go back')
    print('1 - Check basement')
    print("2 - Check 1st floor")

    return(input('Please choose: '))

def cls():
    os.system('cls')

kepler_452b()