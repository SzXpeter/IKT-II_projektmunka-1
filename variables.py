from time import sleep

def sPrint(text, wps = 30):
    for i in range(len(text)):
        print(text[i], end = "")
        sleep(1/wps)


