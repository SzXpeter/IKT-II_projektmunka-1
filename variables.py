from time import sleep

def sPrint(text, wps = 1000):
    for i in range(len(text)):
        print(text[i], end = "")
        sleep(1/wps)
    print()

def userInterface():
    global rad, O2, hp
    for i in range(50):
        print('-', end='')
    print(f"\nHealth: {hp}%\tOxygen: {O2}%\tRadiation: {rad}%")
    for i in range(50):
        print('-', end='')
    print("\n")

def restock():
    global rad, O2, hp
    sPrint("You succesfully restocked")
    rad = 0
    O2 = 100
    hp = 100
    input("continue<ENTER>")

rad = 0
O2 = 100
hp = 100