import sys

poop = int(sys.stdin.readline())

for z in range(poop):

    #getting input
    nums = [int(i) for i in (sys.stdin.readline().split())]
    
    #making the field
    field = [[] for i in range(nums[1])]
    for i in range(nums[1]):
        terrain = sys.stdin.readline()
        for e in range(nums[0]):
                       field[i].append(terrain[e])

    #implementing bidirectional bfs
    #making the queue
    Xqueue1 = []
    Yqueue1 = []
    
    Xqueue2 = []
    Yqueue2 = []

    #making minList/visitedList
    minList1 = [[0 for e in range(nums[0])] for i in range(nums[1])]
    minList2 = [[0 for e in range(nums[0])] for i in range(nums[1])]
    
    visitedList1 = [[False for e in range(nums[0])] for i in range(nums[1])]
    visitedList2 = [[False for e in range(nums[0])] for i in range(nums[1])]

    #finding startPos and endPos
    for i in range(nums[1]):
        for e in range(nums[0]):
            if field[i][e] == 'C':
                Ystart = i
                Xstart = e
            elif field[i][e] == 'W':
                Yend = i
                Xend = e
    visitedList1[Ystart][Xstart] = True
    visitedList2[Yend][Xend] = True

    Xqueue1.append(Xstart)
    Yqueue1.append(Ystart)
    
    Xqueue2.append(Xend)
    Yqueue2.append(Yend)

    dx = [-1,+1,0,0]
    dy = [0,0,+1,-1]
    loop = True
    
    while Xqueue1 and Xqueue2 and loop:
        x1 = Xqueue1.pop(0)
        y1 = Yqueue1.pop(0)
        
        x2 = Xqueue2.pop(0)
        y2 = Yqueue2.pop(0)
        
        if field[y1][x1] == 'W':
            break
        elif (visitedList1[y1][x1] and visitedList2[y1][x1]):
            minList1[Yend][Xend] = minList1[y1][x1] + minList2[y1][x1]
            break
        elif (visitedList1[y2][x2] and visitedList2[y2][x2]):
            minList1[Yend][Xend] = minList1[y2][x2] + minList2[y2][x2]
            break
            
        else:
            for n in range(4):
                newX1 = x1 + dx[n]
                newY1 = y1 + dy[n]
                
                newX2 = x2 + dx[n]
                newY2 = y2 + dy[n]
                if (-1<newX1<nums[0]) and (-1<newY1< nums[1]):
                    if (visitedList1[newY1][newX1] == False) and (field[newY1][newX1] != 'X'):
                        visitedList1[newY1][newX1] = True
                        Xqueue1.append(newX1)
                        Yqueue1.append(newY1)
                        minList1[newY1][newX1] = minList1[y1][x1] + 1
                        
                        if (visitedList1[newY1][newX1] and visitedList2[newY1][newX1]):
                            minList1[Yend][Xend] = minList1[newY1][newX1] + minList2[newY1][newX1]
                            loop = False
                            break
                        
                if (-1<newX2<nums[0]) and (-1<newY2< nums[1]):
                    if (visitedList2[newY2][newX2] == False) and (field[newY2][newX2] != 'X'):
                        visitedList2[newY2][newX2] = True
                        Xqueue2.append(newX2)
                        Yqueue2.append(newY2)
                        minList2[newY2][newX2] = minList2[y2][x2] + 1
                        
                        if (visitedList1[newY2][newX2] and visitedList2[newY2][newX2]):
                            minList1[Yend][Xend] = minList1[newY2][newX2] + minList2[newY2][newX2]
                            loop = False
                            break
                    
             
    if 0< minList1[Yend][Xend] < 60:
        print(minList1[Yend][Xend])
    else:
        print('#notworth')
