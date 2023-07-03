import sys

#getting input
nums = [int(i) for i in sys.stdin.readline().split()]
#making the field
field = [[] for i in range(nums[0])]
templist = []
for i in range(nums[0]):
    terrain = sys.stdin.readline()
    for e in range(nums[1]):
                   field[i].append(terrain[e])

#making the queue
Xqueue = []
Yqueue = []

#making minList/visitedList
minList = [[-1 for e in range(nums[1])] for i in range(nums[0])]
visitedList = [[False for e in range(nums[1])] for i in range(nums[0])]

#finding startPos and endPos

Xstart = 0
Ystart = 0
Xend = 0
Yend = 0
for i in range(nums[0]):
  for e in range(len(field[i])):
        if field[i][e] == 's':
            Ystart = i
            Xstart = e
        elif field[i][e] == 'e':
            Yend = i
            Xend = e
visitedList[Ystart][Xstart] = True

Xqueue.append(Xstart)
Yqueue.append(Ystart)
#remember there are limits on x and y coordinates

dx = [-1,+1,0,0]
dy = [0,0,+1,-1]
newX = 0
newY = 0
while Xqueue:
    x = Xqueue.pop(0)
    y = Yqueue.pop(0)
    if field[y][x] == 'e':
        pass
    else:
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if (-1<newX<nums[1]) and (-1<newY< nums[0]):
                if (visitedList[newY][newX] == False) and (field[newY][newX] != 'X'):
                    visitedList[newY][newX] = True
                    Xqueue.append(newX)
                    Yqueue.append(newY)
                    minList[newY][newX] = minList[y][x] + 1
               
print(minList[Yend][Xend])
