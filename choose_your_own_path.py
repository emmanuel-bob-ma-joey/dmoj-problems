import sys
pages = int(sys.stdin.readline())
adjacencyList = [[]for i in range(pages+1)]
for i in range(1,pages+1):
    numList = [int(i) for i in (sys.stdin.readline()).split()]
    for e in range(1,len(numList)):
        adjacencyList[i].append(numList[e])

visitedList = [False for i in range(pages + 1)]
queue = [1]

minList = [1 for i in range(pages + 1)]
endList = []

while queue:
    n = queue.pop(0)
    if visitedList[n] == False:
        visitedList[n] = True
    if adjacencyList[n] == []:
        endList.append(minList[n])
    else:
        for i in adjacencyList[n]:
            if not visitedList[i]:
                visitedList[i] = True
                queue.append(i)
                minList[i] = minList[n] + 1

peep = True
for i in range(1,len(visitedList)):
    if visitedList[i] == False:
        peep = False
if peep:
    print('Y')
else:
    print('N')

print(min(endList))
