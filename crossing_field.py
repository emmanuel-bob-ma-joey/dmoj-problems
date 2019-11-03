import sys

nums = [int(i) for i in (sys.stdin.readline().split())]

#making the field
field = []
for i in range(nums[0]):
    field.append([int(i) for i in (sys.stdin.readline().split())])

endY = nums[0]
endX = nums[0]

#starting position always [0,0]
Yqueue = [0]
Xqueue = [0]

#yay dont need minList, just visitedList
visitedList = [[False for i in range(nums[0])] for x in range(nums[0])]
visitedList[0][0] = True

dx = [-1,+1,0,0]
dy = [0,0,+1,-1]

while Xqueue:
    y = Yqueue.pop(0)
    x = Xqueue.pop(0)
    if (x == (nums[0] - 1)) and (y == (nums[0]-1)):
        pass
    else:
        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]
            if (-1<newx<nums[0]) and (-1<newy<nums[0]):
                if (visitedList[newy][newx] == False) and (abs(field[y][x] - field[newy][newx])<=nums[1]):
                    visitedList[newy][newx] = True
                    Yqueue.append(newy)
                    Xqueue.append(newx)
            
if visitedList[nums[0]-1][nums[0]-1]:
    print('yes')
else:
    print('no')
