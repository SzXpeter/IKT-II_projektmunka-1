import time

year = 2018
month = 0

def updateDate():
    
    global year, month
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
    
    return date

def gyomlalas():
    max_time = 3
    print(f"Mash any key then hit ENTER within {max_time} seconds...")
    time.sleep(2)
    start_time = time.time()
    count = input("GO! ------> ")

    if time.time() - start_time < max_time:
        if len(count) >= 30:
            print("Success!")
        else:
            print("You failed.")
            print("Túl kevás")
    else:
        print("You failed.")

    input()