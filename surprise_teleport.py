import sys

dimensions = [int(i) for i in (sys.stdin.readline().split())]
startPoint = [(int(i)) for i in (sys.stdin.readline().split())]
endPoint = [(int(i)) for i in (sys.stdin.readline().split())]
grid = [[] for i in range(dimensions[0])]

for i in range(dimensions[0]):
    poop = sys.stdin.readline()
    for e in range(dimensions[1]):
        grid[i].append(poop[e])

derp = False
for i in range(int(sys.stdin.readline())):
    teleport = [(int(i)) for i in (sys.stdin.readline().split())]
    grid[teleport[0]][teleport[1]] = 'T'
    if (startPoint[0] == teleport[0]) and (startPoint[1] == teleport[1]):
        derp = True

#min/visited/queue list
minList = [[0 for i in range(dimensions[1])] for n in range(dimensions[0])]
visitedList = [[False for i in range(dimensions[1])] for n in range(dimensions[0])]
visitedList[startPoint[0]][startPoint[1]] = True

Yqueue = []
Xqueue = []
Yqueue.append(startPoint[0])
Xqueue.append(startPoint[1])
Teleport = False
minTeleport = 0

dx = [-1,+1,0,0]
dy = [0,0,-1,+1]

while Xqueue:
    y = Yqueue.pop(0)
    x = Xqueue.pop(0)
    if (y == endPoint[0]) and (x == endPoint[1]):
        break
    else:
        if grid[y][x] == 'T':
            if not Teleport:
                minTeleport = minList[y][x]
                Teleport = True
        for i in range(4):
            newY = y + dy[i]
            newX = x + dx[i]
            if (-1<newY<dimensions[0]) and (-1<newX<dimensions[1]):
                if (visitedList[newY][newX] == False) and (grid[newY][newX]!= 'X'):
                    visitedList[newY][newX] = True
                    minList[newY][newX] = minList[y][x] + 1
                    Yqueue.append(newY)
                    Xqueue.append(newX)

if derp:
    print(minList[endPoint[0]][endPoint[1]])
    pass
else:
    if minTeleport == 0:
        print(0)
    else:
        savedTime = (minList[endPoint[0]][endPoint[1]] - minTeleport)
        if savedTime>0:
            print(savedTime)
        else:
            print(0)
            

    
                    
                    
        
            




        

        
