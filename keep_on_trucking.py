minDistance = int(input())
maxDistance = int(input())
motelNum = int(input())
motelList = [0,990,1010,1970,2030,2940,3060,3930,4060,4970,5030,5990,6010,7000]

if motelNum != 0:
    for i in range(motelNum):
        motel = int(input())
        motelList.append(motel)
    motelList.sort()

routeList = []
for i in range(7001):
    routeList.append(0)

distanceList = []
for i in range(len(motelList)):
    distanceList.append(7000)
for i in range(len(motelList) - 1):
    tempList = []
    for x in range(1,len(motelList) - i):
        distance = (motelList[x + i] - motelList[i])
        if minDistance <= distance <= maxDistance:
            tempList.append(distance)
        else:
            tempList.append(7001)
    distanceList[i] = tempList
distanceList[len(distanceList) - 1] = [0]

def findRoutes(distanceList,motelList,routeList,min,max,currentMotelIndex,routes):
    if routeList[(motelList[currentMotelIndex])] == 0:
        if motelList[currentMotelIndex] == 7000:
            routes = 1
            return routes
        else:
            for i in range((currentMotelIndex +1),len(motelList)):
                if distanceList[currentMotelIndex][i - currentMotelIndex -1] != 7001:
                    routeList[motelList[currentMotelIndex]] += findRoutes(distanceList,motelList,routeList,min,max,i,routes)
    return routeList[motelList[currentMotelIndex]]

poop = findRoutes(distanceList,motelList,routeList,minDistance,maxDistance,0,0)
print(poop)
