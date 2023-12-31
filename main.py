from kepler_452b import kepler_452b, kepler_checked
from proxima_centauri_b import proxima_centauri_b, proxima_checked
from trappist_1f import trappist_1f, trappist1fAliens, trappist1fLand
from LHS_1140b import lhs_1140b, LHSAliens, LHSLand
import variables, os

variables.sPrint("You were sent here from earth to collect information about these planets.\nYou need to examine the life forms that live or lived there and the landscape.")
input("continue <ENTER>")

def main():
    vExit = False
    while vExit == False:
        v = ''
        if kepler_checked == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] and proxima_checked == [1, 1, 1, 1] and trappist1fAliens == [1, 1, 1] and trappist1fLand == [1, 1, 1, 1, 1] and LHSAliens == [1, 1, 1, 1, 1, 1, 1, 1, 1] and LHSLand == [1, 1, 1, 1]:
            while v != '1' and v != '2' and v != '3' and v !='4' and v != 'exit' and v != 'end':
                os.system("cls")
                variables.sPrint("You're in outer space.")
                print("\n\t1. Go to Proxima Centauri b")
                print("\t2. Go to Trappist-1f")
                print("\t3. Go to Kepler-452b")
                print("\t4. Go to LHS_1140b")
                print("\tend. Finish game")
                print("\texit. Exit game")
                v = input("choice: ")
        else:
            while v != '1' and v != '2' and v != '3' and v !='4' and v != 'exit':
                os.system("cls")
                variables.sPrint("You're in outer space.")
                print("\n\t1. Go to Proxima Centauri b")
                print("\t2. Go to Trappist-1f")
                print("\t3. Go to Kepler-452b")
                print("\t4. Go to LHS_1140b")
                print("\texit. Exit game")
                v = input("choice: ")

        variables.hp = 100
        variables.rad = 0
        variables.O2 = 100

        match v:
            case '1':
                proxima_centauri_b()
            case '2':
                trappist_1f()
            case '3':
                kepler_452b()
            case '4':
                lhs_1140b()
            case 'exit':
                variables.sPrint("Thanks you for playing!")
                vExit = True
            case 'end':
                variables.sPrint("Congratulations! You have beaten the game.")
                print(f"You died {variables.deaths} times.")

main()