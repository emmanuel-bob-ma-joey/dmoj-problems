import sys
info = [int(i) for i in sys.stdin.readline().split()]

adjacencyList = [[] for i in range(info[0]+1)]
#print(adjacencyList)
for i in range(info[1]):
    poop = [int(i) for i in sys.stdin.readline().split()]
    adjacencyList[poop[0]].append(poop[1])
    adjacencyList[poop[1]].append(poop[0])
#print(adjacencyList)

resultList = [0 for i in range(info[0] + 1)]
if info[2]< info[3]:
    startPos = info[2]
    endPos = info[3]
else:
    startPos = info[3]
    endPos = info[2]

def findRoutes(currentPos,endPos,iterations):
    if resultList[currentPos] == 0:
        if currentPos == endPos:
            routes = 1
            return routes

        else:
            if iterations < 15:
            #for all the places i can go to
                for i in (adjacencyList[currentPos]):
                    resultList[currentPos] += findRoutes(i,endPos,iterations+1)
    return resultList[currentPos]

poop = findRoutes(startPos, endPos,1)
#print(resultList)
if poop != 0:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")
