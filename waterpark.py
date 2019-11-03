import sys

pointNum = int(sys.stdin.readline())
slideList = [[0] for i in range(pointNum)]
stop = False
#gets the coordinate input as long as not [0,0]
while not stop:
    connection = (sys.stdin.readline()).split()
    if connection == ['0', '0']:
        stop = True
    else:
        connection = [int(connection[i]) for i in range(2)]
        slideList[connection[0]].append(connection[1])

#just takes out the unnecessary zeroes in slidelist
for i in range(1,len(slideList)):
    del slideList[i][0]

routeList = [0]*(pointNum + 1)

def dfs(slideList,routeList,currentSlideIndex,routes):
    if routeList[currentSlideIndex] == 0:
        if currentSlideIndex == pointNum:
            return 1
        else:
            for i in slideList[currentSlideIndex]:
                routeList[currentSlideIndex] += dfs(slideList,routeList,i,routes)
    return routeList[currentSlideIndex]

print(dfs(slideList,routeList,1,0))
