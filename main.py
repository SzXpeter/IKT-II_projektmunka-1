from menu import *
from events import *
import os
money = 1000
pos = 'h'

gyomlalas()

while money > 0:
    os.system("cls")
    date = updateDate()
    header(money, date, 100, 0)
    match menuHouse():
        case '1': 
            map(pos, 1000, date, 100, 0) 

        case 'a':
            pass