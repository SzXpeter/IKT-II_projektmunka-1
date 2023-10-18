import time

year = 2018
month = 0
money = 1000
pos = 'h'
date = ""
energy = 0
sus = 0
<<<<<<< HEAD
inventory = []

=======
>>>>>>> 9e5dcc9b3dcd0ce608714a9841b7d3ebd6df5ea6
def updateDate():
    global year, month, date
    month += 6

    if month > 12:
        year += 1
        month -= 12

    date = str(year)

    if month < 10:
        date += '.0'
        date += str(month)
    else:
        date = date + '.' + str(month)


def gyomlalas():
    max_time = 3
    print(f"Spamelj bármilyen billentyűt {max_time} másodpercen belűl...")
    time.sleep(2)
    count = input("GO! ------> ")
    start_time = time.time()

    if time.time() - start_time < max_time:
        if len(count) >= 30:
            print("Siker!")
        else:
            print("Sikertelen próbálkozás.")
    else:
        print("Sikertelen próbálkozás.")

    input()

def listInventory():
    print('Az inventoryd tartalma: ', end='')
    for i in range(len(inventory)):
        if i == len(inventory) - 1:
            print(inventory[i])
        else:
            print(inventory[i], end=', ')

    input('\nNyomj ENTER -t a folytatáshoz...')

def addInventory(item):
    inventory.append(item)
    print(f'{item} sikeresen hozzáadva az Inventorydhoz.')

def removeInventory(item):
    inventory.remove(item)
    print(f'{item} sikeresen eltávolítva az Inventorydból.')

def isEnergyLow():
    if energy <= 0:
        energy = 50
        money -= money*0.15