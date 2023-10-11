def updateDate(year, month, day):
    date = str(year)
    if month < 10:
        date += '.0'
        date += str(month)
    else:
        date = date + '.' + str(month)

    if day < 10:
        date += '.0'
        date += str(day)
    else:
        date = date + '.' + str(day)
    
    return date