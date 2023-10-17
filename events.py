import time

year = 2018
month = 0
money = 1000
pos = 'v'
date = ""
energy = 100
sus = 0

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