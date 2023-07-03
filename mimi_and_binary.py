import sys
binary = sys.stdin.readline()
binaryList = [int(binary[i]) for i in range(len(binary)-1)]
poop = len(binaryList)
sumZero = [0 for i in range(poop+1)]
sumOne = [0 for i in range(poop+1)] 
zeroList = [-1 for i in range(poop+1)]
oneList = [-1 for i in range(poop+1)]
#sumArray
for i in range(1,poop+1):
    if binaryList[i-1] == 1:
        sumOne[i] = sumOne[i-1]+1
        sumZero[i]= sumZero[i-1]
    else:
        sumZero[i] = sumZero[i-1]+1
        sumOne[i] = sumOne[i-1]
    if zeroList[sumZero[i]] == -1:
        zeroList[sumZero[i]] = i
    if oneList[sumOne[i]] == -1:
        oneList[sumOne[i]] = i

#answering queries
for i in range(int(sys.stdin.readline())):
    peep = [int(i) for i in (sys.stdin.readline().split())]
    if peep[2] == 1:
        if sumOne[peep[0]-1]+peep[1] <= poop:
            print(oneList[sumOne[peep[0]-1]+peep[1]])
        else:
            print(-1)
            
    else:
        if sumZero[peep[0]-1]+peep[1] <= poop:
            print(zeroList[sumZero[peep[0]-1]+peep[1]])
        else:
            print(-1)
