import sys

limit,buildings,roads,stores = [int(i) for i in (sys.stdin.readline().split())]
storeList = [False for i in range(buildings+1)]
visitedList = [False for i in range(buildings+1)]   
adjacencyList = [[] for i in range(buildings+1)]

for i in range(stores):
    storeList[int(sys.stdin.readline())] = True
    
for i in range(roads):
    buildingA,buildingB,length = [int(i) for i in (sys.stdin.readline().split())]
    adjacencyList[buildingA].append([buildingB,length])
    
minList = [float('inf') for i in range(buildings+1)]
inQueue = [False for i in range(buildings+1)]
queue = [0]
inQueue[0] = True
minList[0] = 0
answer = 0

while queue:
    current = queue.pop(0)
    inQueue[current] = False
    
    if minList[current] <limit:
        if storeList[current] and not visitedList[current]:
            answer+=1
            visitedList[current] = True
            
        for neighbours in adjacencyList[current]:
            temp = minList[current]+neighbours[1]
            
            if temp< minList[neighbours[0]]:
                minList[neighbours[0]] = temp
                if not inQueue[neighbours[0]]:
                    inQueue[neighbours[0]] = True
                    queue.append(neighbours[0])
                    
print(answer)
