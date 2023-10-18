import menu, events

events.updateDate()

while events.money > 0:
    events.isEnergyLow()
    match events.pos:
        case 'h':
            match menu.menuHouse():
                case '1': 
                    menu.map() 

<<<<<<< HEAD
        case 'a':
            events.updateDate()
            
        case 'i':
            events.listInventory()
=======
                case 'a':
                    events.updateDate()
                    energy = 100
            
>>>>>>> 9e5dcc9b3dcd0ce608714a9841b7d3ebd6df5ea6
