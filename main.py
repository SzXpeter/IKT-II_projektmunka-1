import menu, events

events.updateDate()

while events.money > 0:
    events.isEnergyLow()
    match events.pos:
        case 'h':
            match menu.menuHouse():
                case '1': 
<<<<<<< HEAD
                    valasztas = menu.map()
                    
                    match valasztas:
                        case '1':
                            events.isFarmSold(events.fold1)
                        case '2':
                            events.isFarmSold(events.fold2)
                        case '3':
                            events.isFarmSold(events.fold3)
                        case '4':
                            events.isFarmSold(events.fold4)
                        case '5':
                            events.isFarmSold(events.fold5)
                        case '6':
                            events.isFarmSold(events.fold6)
                        case '7':
                            events.isFarmSold(events.fold7)
                        case '8':
                            events.isFarmSold(events.fold8)
                        case '9':
                            events.isFarmSold(events.fold9)
                        case '10':
                            events.isFarmSold(events.fold10)
                        case '11':
                            events.isFarmSold(events.fold11)
                        case 't':
                            events.isFarmSold(events.foldOrokolt)

                    

        case 'a':
            events.updateDate()
            energy = 100
=======
                    menu.map() 
                case 'a':
                    events.updateDate()
                    energy = 100
>>>>>>> 4c7bc3912b9b0aa318c9d116fbf3b8dd1aedeb39
            
        case 'i':
            events.listInventory()
            
