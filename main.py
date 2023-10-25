from kepler_452b import *
from lhs_1140b import *
from proxima_centauri_b import *
from trappist_1f import trappist_1f
import variables, os, sys

variables.sPrint("You were sent here from earth to collect information about these planets.\nYou need to examine the life forms that live or lived there and the landscape.")
input("continue <ENTER>")

def main():
    vExit = False
    while vExit == False:
        v = ''
        while v != '1' and v != '2' and v != '3' and v !='4' and v != 'exit':
            os.system("cls")
            variables.sPrint("You're in outer space.")
            print("\n\t1. Go to Proxima Centauri b")
            print("\t2. Go to Trappist-1f")
            print("\t3. Go to Kepler-452b")
            print("\t4. Go to LHS_1140b")
            print("\texit. Exit game")
            v = input("choice: ")

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
            case _:
                pass

main()