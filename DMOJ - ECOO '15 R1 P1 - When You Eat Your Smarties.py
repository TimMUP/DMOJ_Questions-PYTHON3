from math import *
colorList = ["orange", "blue", "green", "yellow", "pink", "violet", "brown"]

for i in range(10):
    itemList = []
    timeRequired = 0

    while True:
        tempText = input("")
        if tempText != "end of box":
            itemList.append(tempText)
        else:
            break


    for i in colorList:
        if itemList.count(i) > 0:
            timeRequired += (ceil(itemList.count(i)/7)*13)

    timeRequired += itemList.count("red")*16

    print(timeRequired)