def stringSeperation(x):
    numList = []
    for i in range(0, x.count(" ")):
        numList.append(int(x[:x.find(" ")]))
        x = x[x.find(" ") + 1:]
    numList.append(int(x))
    return(numList)

for w in range(10):
    markWeightPreset = stringSeperation(input(""))
    for mark in range(4):
        markWeightPreset[mark] = markWeightPreset[mark]*0.01

    passedStudent = 0
    studentNum = int(input(""))
    for i in range(studentNum):
        studentMark = stringSeperation(input(""))
        studentMarkTotal = 0.0
        for x in range(4):
            studentMarkTotal += (markWeightPreset[x]* studentMark[x])
        if studentMarkTotal >= 50:
            passedStudent += 1
    print(passedStudent)