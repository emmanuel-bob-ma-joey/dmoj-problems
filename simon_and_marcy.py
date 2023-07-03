import sys
poop = [int(i) for i in (sys.stdin.readline()).split()]
numCages = poop[0]
timeCapacity = poop[1]

#2-D array with the length being capacity minutes and height being with using different cages (minutes)
resultArray = [[0 for i in range(timeCapacity + 1)]for i in range(numCages + 1)]

#in valueArray, each index is a cage, with valueArray[0] being the number of princesses and valueArray[1] being the amount of time it takes
valueArray = [[int(i) for i in (sys.stdin.readline().split())] for x in range(numCages)]

#bottom-up
for i in range(numCages):
    for e in range(timeCapacity + 1):
        if e < valueArray[i][1]:
            resultArray[i][e] = resultArray[i-1][e]
        else:
           if resultArray[i-1][e - valueArray[i][1]] == 0:
               temp = max(resultArray[i-1][e],valueArray[i][0])
           else:
               temp = max(resultArray[i-1][e],(resultArray[i-1][e - valueArray[i][1]] + valueArray[i][0]))
           resultArray[i][e] = temp

print(max(resultArray[numCages-1]))
