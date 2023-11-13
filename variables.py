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

def statUpdate(radUpdate, O2Update = 5):
    global rad, O2, hp
    if O2 <= 0:
        O2 = 0
        hp -= 10
    else:
        O2 -= O2Update
    if rad >= 100:
        rad = 100
        hp -= 10
    else:
        rad += radUpdate
    if hp <= 0:
        hp = 100
        O2 = 100
        rad = 0
        return "dead"


rad = 0
O2 = 100
hp = 100