import sys
input = sys.stdin.readline()
input = input.split()
input = [int(i) for i in input]
postCoordinate = [input[0],input[1]]
corner1 = [input[2],input[3]]
corner2 = [input[4],input[5]]

minDistanceX = 99999
for i in range(corner1[0],corner2[0]+1):
    distance = abs(postCoordinate[0] - i)
    if distance < minDistanceX:
        minDistanceX = distance

minDistanceY = 99999
for i in range(corner1[1],corner2[1]+1):
    distance = abs(postCoordinate[1] - i)
    if distance < minDistanceY:
        minDistanceY = distance


output = (((minDistanceX**2) + (minDistanceY**2))**(1/2))
print (format(output, '.3f'))
