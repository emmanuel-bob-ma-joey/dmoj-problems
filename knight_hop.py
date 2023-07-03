import sys

startPos = (sys.stdin.readline()).split()
endPos = (sys.stdin.readline()).split()
startPos = [int(i) for i in startPos]
endPos = [int(i) for i in endPos]

dfsList = [[999 for i in range(10)] for i in range(10)]
#visited saves how many ways to get to that index/point'
def findRoutes(startPos,endPos,moves):
    if dfsList[startPos[0]][startPos[1]] > moves:
        dfsList[startPos[0]][startPos[1]] = moves
        if startPos != endPos:
            possibleList = [[startPos[0] - 2, startPos[1] - 1], [startPos[0] - 2, startPos[1] + 1],
                            [startPos[0] - 1, startPos[1] - 2], [startPos[0] - 1, startPos[1] + 2],
                            [startPos[0] + 1, startPos[1] - 2], [startPos[0] + 1, startPos[1] + 2],
                            [startPos[0] + 2, startPos[1] - 1], [startPos[0] + 2, startPos[1] + 1]]
            for i in possibleList:
                if (0<i[0]< 9) and (0<i[1]<9) and (dfsList[i[0]][i[1]] > moves + 1):
                    findRoutes(i,endPos,(moves + 1))

findRoutes(startPos,endPos,0)
print(dfsList[endPos[0]][endPos[1]])
