import sys

nums = [int(i) for i in (sys.stdin.readline().split())]
adjacencyList = [[] for i in range(nums[0]+1)]

for i in range(nums[1]):
    edge = [int(x) for x in (sys.stdin.readline().split())]
    adjacencyList[edge[0]].append(edge[1])
    adjacencyList[edge[1]].append(edge[0])
    
for e in range(nums[2]):
    visitedList1 = [False for i in range(nums[0]+1)]
    visitedList2 = [False for i in range(nums[0]+1)]
    
    minList1 = [0 for i in range(nums[0]+1)]
    minList2 = [0 for i in range(nums[0]+1)]
    
    poop = [int(i) for i in (sys.stdin.readline().split())]
    startQueue = []
    endQueue = []
    startPos = poop[0]
    endPos = poop[1]
    
    visitedList1[startPos] = True
    visitedList2[endPos] = True
    
    startQueue.append(startPos)
    endQueue.append(endPos)
    
    while startQueue and endQueue:
        startNode = startQueue.pop(0)
        endNode = endQueue.pop(0)
        
        if visitedList1[startNode] and visitedList2[startNode]:
            minList1[endPos] = minList1[startNode]+minList2[startNode]
            break
            
        elif visitedList1[endNode] and visitedList2[endNode]:
            minList1[endPos] = minList1[endNode]+minList2[endNode]
            break
            
        else:
            for i in adjacencyList[startNode]:
                if visitedList1[i] == False:
                    visitedList1[i] = True
                    startQueue.append(i)
                    minList1[i] = minList1[startNode]+1
                    
            for i in adjacencyList[endNode]:
                if visitedList2[i] == False:
                    visitedList2[i] = True
                    endQueue.append(i)
                    minList2[i] = minList2[endNode]+1
                    
    if minList1[endPos] != 0:
        print(minList1[endPos])
    else:
        print(-1)
        

    
