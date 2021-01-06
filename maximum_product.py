totalNum = int(input())
posList = []
negList = []
if totalNum == 1:
    num = int(input())
    print(num)
else:

    for i in range(totalNum):
        num = int(input())
        if num < 0:
            negList.append(num)
        elif num > 0:
            posList.append(num)
        elif num == 0:
            pass

    negList.sort()
    posProduct = 0
    negProduct = 0

    for i in range(len(posList)):
        if i == 0:
            posProduct = posList[i]
        else:
            posProduct = posProduct*posList[i]

    if (len(posList) != 0) and (len(negList) == 1):
        print(posProduct)
    elif (len(posList) == 0) and (len(negList) == 0):
        print(0)
    elif (len(posList) == 0) and (len(negList)%2 == 0):
        for i in range(len(negList)):
            if i == 0:
                negProduct = negList[0]
            else:
                negProduct = negProduct*negList[i]
        print(negProduct)
    elif (len(posList) == 0) and (len(negList)%2 == 1):
        for i in range(len(negList) - 1):
            if i == 0:
                negProduct = negList[0]
            else:
                negProduct = negProduct*negList[i]
        print(negProduct)
    elif (len(posList) > 0) and (len(negList) == 0):
        print(posProduct)
    elif (len(posList) > 0) and (len(negList) > 0):
        if (len(negList)%2 == 0):
            for i in range(len(negList)):
                if i == 0:
                    negProduct = negList[0]
                else:
                    negProduct = negProduct*negList[i]
            print(negProduct*posProduct)

        else:
            for i in range(len(negList) - 1):
                if i == 0:
                    negProduct = negList[0]
                else:
                    negProduct = negProduct*negList[i]
            print(negProduct*posProduct)
