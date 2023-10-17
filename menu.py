import os, events

def header():
    print("------------------------------------------")
    print(f"Pénz: {events.money}€\t\tDátum:", events.date)
    print(f"Energia: {events.energy}%\t\tGyanú: {events.sus}%")
    print("------------------------------------------")

def menuHouse():
    v = ''
    while v != '1' and v != 'a':
        os.system("cls")
        header()
        print("1\t Térkép")
        print("a\t Alvás")
        v = input("Választás: ")
    return v

def map():
    v=''

    while v != '1' and v != '2' and v != '3' and v != '4' and v != '5' and v != '6' and v != '7' and v != '8' and v != '9' and v != '10' and v != '11' and v != 'f' and v != 'b' and v != 'a' and v != 't' and v != '0':
        os.system("cls")
        header()
        print("1\t 1.es föld", end = '\t\t')
        print("2\t 2.es föld")
        print("3\t 3.es föld", end = '\t\t')
        print("4\t 4.es föld")
        print("5\t 5.es föld", end = '\t\t')
        print("6\t 6.es föld")
        print("7\t 7.es föld", end = '\t\t')
        print("8\t 8.es föld")
        print("9\t 9.es föld", end = '\t\t')
        print("10\t 10.es föld")
        print("11.. 11.es föld")
        print("\nt\t Örökölt föld", end = '\t')
        print("b\t Bank")
        print("a\t Áruház", end = '\t\t')
        print("t\t Terület vétel")
        print("\n0\t Vissza")

        v = input("\n\nVálasszon: ")
    return v