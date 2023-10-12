import os

def header(money, date, energy, sus):
    print("------------------------------------------")
    print(f"Pénz: {money}€\t\tDátum: {date}")
    print(f"Energia: {energy}%\t\tGyanú: {sus}%")
    print("------------------------------------------")

def menuHouse():
    v = ''
    while v != '1' and v != '7' and v != '8' and v != '9':
        print("1... Térkép")
        v = input("Választás: ")
    return v

def map(pos, money, date, energy, sus):
    v=''

    while v != '1' and v != '2' and v != '3' and v != '4' and v != '5' and v != '6' and v != '7' and v != '8' and v != '9' and v != '10' and v != '11' and v != 'f' and v != 'b' and v != 'a' and v != 't' and v != '0':
        os.system("cls")
        header(1000, date, 100, 0)
        print("1... 1.es föld", end = '\t\t')
        print("2... 2.es föld")
        print("3... 3.es föld", end = '\t\t')
        print("4... 4.es föld")
        print("5... 5.es föld", end = '\t\t')
        print("6... 6.es föld")
        print("7... 7.es föld", end = '\t\t')
        print("8... 8.es föld")
        print("9... 9.es föld", end = '\t\t')
        print("10.. 10.es föld")
        print("11.. 11.es föld")
        print("\nf... Örökölt föld", end = '\t')
        print("b... Bank")
        print("a... Áruház", end = '\t\t')
        print("t... Terület vétel")
        print("\n0... Vissza")

        v = input("\n\nVálasszon: ")
    return v