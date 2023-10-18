import menu, events

events.updateDate()

while events.money > 0:
    match menu.menuHouse():
        case '1': 
            menu.map() 

        case 'a':
            events.updateDate()
            
        case 'i':
            events.listInventory()