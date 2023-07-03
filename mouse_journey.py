import sys

dimensions = [int(i) for i in sys.stdin.readline().split()]
rows = dimensions[0]
columns = dimensions[1]
grid = [[0]*columns for i in range(rows)]
routeList = grid
numCages = int(sys.stdin.readline())
for i in range(numCages):
    coordinate = [int(i) for i in sys.stdin.readline().split()]
    grid[coordinate[0] - 1][coordinate[1] -1] = 'CAT'

def findPaths(startPos,endPos,routes):
    if routeList[startPos[0]][startPos[1]] == 0:
        if startPos == endPos:
            routes = 1
            return routes
        else:
            if startPos[0] + 1 <= rows - 1:
                if grid[startPos[0] + 1][startPos[1]] != 'CAT':
                    grid[startPos[0]][startPos[1]] += findPaths([startPos[0] + 1,startPos[1]],endPos,routes)
            if (startPos[1] + 1) <= columns - 1:
                if grid[startPos[0]][startPos[1] + 1] != 'CAT':
                    grid[startPos[0]][startPos[1]] += findPaths([startPos[0],startPos[1] + 1],endPos,routes)
    return routeList[startPos[0]][startPos[1]]

print(findPaths([0,0],[rows - 1,columns - 1],0))
