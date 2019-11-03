import sys

for i in range(int(sys.stdin.readline())):
    info = [int(i) for i in (sys.stdin.readline()).split()]
    numPins = info[0]
    numBalls = info[1]
    width = info[2]

    resultList = [[0 for x in range(numPins+1)] for x in range(numBalls + 1)]
    savedList = [0 for i in range(numPins)]
    pinList = list(savedList)

    for y in range(numPins-1,-1,-1):
        pinList[y] = (int(sys.stdin.readline()))
        for m in range(width):
            if (y + m) <numPins:
                savedList[y] += pinList[y + m]
    for x in range(numBalls):
        for j in range((numPins-1),-1,-1):
            if j + (width)>= numPins:
                resultList[x][j] = savedList[j]
            else:
                resultList[x][j] = savedList[j] + resultList[x-1][j+width]
                if resultList[x][j] < resultList[x][j+1]:
                    resultList[x][j] = resultList[x][j+1]
                    
    print(resultList[numBalls - 1][0])
