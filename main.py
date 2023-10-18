import menu, events

events.updateDate()

while events.money > 0:
    events.isEnergyLow()
    match events.pos:
        case 'h':
            match menu.menuHouse():
                case '1': 
                    menu.map() 

                case 'a':
                    events.updateDate()
                    energy = 100
            