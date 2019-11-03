import sys
dimensions = [int(i) for i in (sys.stdin.readline().split())]
grid = [[] for i in range(dimensions[0])]
for i in range(dimensions[0]):
    poop = sys.stdin.readline()
    for x in range(dimensions[1]):
        grid[i].append(poop[x])

routeList = [[0 for i in range(dimensions[1]+1)] for x in range(dimensions[0]+1)]
routeList[1][1] = 1

for y in range(1,dimensions[0]+1):
    for x in range(1,dimensions[1]+1):
        if routeList[y][x] != 1:
            if grid[y-1][x-1] != '#':
                routeList[y][x] = routeList[y-1][x] + routeList[y][x-1]
                
print(routeList[dimensions[0]][dimensions[1]]%(10**9+7))
