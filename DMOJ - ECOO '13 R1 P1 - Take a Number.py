infoList = [0, 0, 0]
infoList[2] = int(input(""))
while True:
    tempText = input("")
    if tempText == "EOF":
        break
    elif tempText == "CLOSE":
        print("%i %i %i" %(infoList[0], infoList[0] - infoList[1], infoList[2]))
        infoList[0] = 0
        infoList[1] = 0
    elif tempText == "TAKE":
        infoList[0] += 1
        infoList[2] += 1
        if infoList[2] == 1000:
            infoList[2] = 1
    else:
        infoList[1] += 1
