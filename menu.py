def header(money, date, energy, sus):
    print("------------------------------------------")
    print(f"Pénz: {money}€\t\tDátum: {date}")
    print(f"Energia: {energy}%\t\tGyanú: {sus}%")
    print("------------------------------------------")

def menuHouse():
    v = ''
    while v != '1' and v != '7' and v != '8' and v != '9':
        print("1...Menjen ki az örökölt földre")
        print("7...Menjen el a Bankba")
        print("8...Menjen el az Áruházba")
        print("9...Menjen el földet venni")
        v = input("Választás: ")