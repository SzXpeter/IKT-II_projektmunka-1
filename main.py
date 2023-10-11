from menu import *
from events import updateDate

year = 2018
month = 4
day = 7
money = 1000

while money > 0:
    date = updateDate(year, month, day)
    header(1000, date, 100, 0)
    menuHouse()