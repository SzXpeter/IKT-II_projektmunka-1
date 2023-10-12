from menu import *
from events import updateDate
import os

year = 2018
month = 4
day = 7
money = 1000
pos = 'h'

while money > 0:
    os.system("cls")
    date = updateDate(year, month, day)
    header(1000, date, 100, 0)
    if menuHouse() == '1':
        map(pos, 1000, date, 100, 0) 