loopCount = int(input(""))
for i in range(0, loopCount):
   inputTemp = input("")
   int1 = int(inputTemp[0:inputTemp.find(" ")])
   int2 = int(inputTemp[inputTemp.find(" "):])
   print(int1 - int2)