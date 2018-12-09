binaryNum = input()
finalAnswer = ""

stringReminder = len(binaryNum)%3

while len(binaryNum) % 3 != 0:
    binaryNum = '0' + binaryNum

for i in range (0, len(binaryNum)//3):
    if binaryNum[-3:] == "000":
        finalAnswer = '0' + finalAnswer
    elif binaryNum[-3:] == "001":
        finalAnswer = '1' + finalAnswer
    elif binaryNum[-3:] == "010":
        finalAnswer = '2' + finalAnswer
    elif binaryNum[-3:] == "011":
        finalAnswer = '3' + finalAnswer
    elif binaryNum[-3:] == "100":
        finalAnswer = '4' + finalAnswer
    elif binaryNum[-3:] == "101":
        finalAnswer = '5' + finalAnswer
    elif binaryNum[-3:] == "110":
        finalAnswer = '6' + finalAnswer
    else:
        finalAnswer = '7' + finalAnswer
    binaryNum = binaryNum[:-3]

print (finalAnswer)
