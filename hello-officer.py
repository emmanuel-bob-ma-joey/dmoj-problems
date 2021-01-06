import sys
houses,roads,current,queries = [int(i) for i in (sys.stdin.readline().split())]
adjacencyList = [[] for i in range(houses+1)]
minList = [float('inf') for i in range(houses+1)]
minList[current] = 0
inQueue = [False for i in range(houses+1)]
queue = []
queue.append(current)

for i in range(roads):
    start,end,length = [int(i) for i in (sys.stdin.readline().split())]
    adjacencyList[start].append([end,length])
    adjacencyList[end].append([start,length])

while queue:
    current = queue.pop(0) 
    inQueue[current] = False
    for neighbour in adjacencyList[current]:
        temp = minList[current]+neighbour[1]
        if temp< minList[neighbour[0]]:
            minList[neighbour[0]] = temp
            if not inQueue[neighbour[0]]:
                inQueue[neighbour[0]] = True
                queue.append(neighbour[0])
                

for i in range(queries):
    poop = int(sys.stdin.readline())
    if minList[poop] == float('inf'):
        print(-1)
    else:
        print(minList[poop])
