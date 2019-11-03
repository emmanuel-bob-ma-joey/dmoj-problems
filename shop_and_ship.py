import sys

cities = int(sys.stdin.readline())
adjacencyMatrix = [[float('inf') for i in range(cities+1)] for x in range(cities+1)]

for i in range(int(sys.stdin.readline())):
    city1,city2,cost = [int(i) for i in (sys.stdin.readline().split())]
    if cost<adjacencyMatrix[city1][city2]:
        adjacencyMatrix[city1][city2] = cost
        adjacencyMatrix[city2][city1] = cost
        
minList = [float('inf') for i in range(cities+1)]

for i in range(int(sys.stdin.readline())):
    city,cost = [int(x) for x in (sys.stdin.readline().split())]
    minList[city] = cost
    
visitedList = [False for i in range(cities+1)]
destination = int(sys.stdin.readline())

loop = True
while loop:
    current = 0
    for city in range(1,cities+1):
        if minList[city] < minList[current] and not visitedList[city]:
            current = city
    if current == destination:
        print(minList[current])
        break
        
    visitedList[current] = True
    for city in range(1,cities+1):
        if adjacencyMatrix[current][city]!= float('inf'):
            if minList[city] > (minList[current]+adjacencyMatrix[current][city]):
                minList[city] = minList[current]+adjacencyMatrix[current][city]
