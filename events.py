import time

year = 2018
month = 0
money = 1000
pos = 'h'
date = ""
energy = 100
sus = 0
inventory = []

# megvan, mennyibe kerül, mérete(Ár), mi terem rajta, állapota (0 = nincs ültetve, 1 = Növekedik, 2 = Gyomlálni/öntözni kell, 3 = Kész), növekedés állapota
# 1 = répa, 2 = krumpli, 3 = fű, 0 = még semmi
# 1 Ár = 150 €

foldOrokolt = [True, 0, 3, 0, 0, 0]
fold1 = [False, 30000, 200, 0, 0, 0]
fold2 = [False, 67500, 450, 0, 0, 0]
fold3 = [False, 30000, 200, 800, 0, 0]
fold4 = [False, 3000, 20, 0, 0, 0]
fold5 = [False, 45000, 300, 0, 0, 0]
fold6 = [False, 15000, 100, 0, 0, 0]
fold7 = [False, 97500, 650, 0, 0, 0]
fold8 = [False, 1500, 10, 0, 0, 0]
fold9 = [False, 7500, 50, 0, 0, 0]
fold10 = [False, 5250, 35, 0, 0, 0]
fold11 = [False, 1500, 10, 0, 0, 0]

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
    global energy, money
    if energy <= 0:
        energy = 50
        money -= money*0.15

def isFarmSold(telek):
    print(telek[0])
    if telek[0] == False:
        megveszed = input(f'Ez a telek még nem a tiéd, szeretnéd megvenni {telek[1]}€ -ért (i/n): ')
        if megveszed == 'i':
            if money >= telek[1]:
                print('Sikeresen megvetted a telket.')
                telek[0] = True
                input('\nNyomj ENTER -t a folytatáshoz...')
            else:
                print('Nincs elég pénzed.')
                input('\nNyomj ENTER -t a folytatáshoz...')
    else:
        print('Ez a te telked.')
        input('\nNyomj ENTER -t a folytatáshoz...')