listLength = int(input())
numList = []
for i in range(listLength):
    num = int(input())
    numList.append(num)
numList.sort()
for i in range(len(numList)):
    print(numList[i])
