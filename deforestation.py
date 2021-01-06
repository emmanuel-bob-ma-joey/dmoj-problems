import sys
trees = int(sys.stdin.readline())
sumArray = [0 for i in range(trees+1)]
for i in range(1,trees+1):
    sumArray[i] = sumArray[i-1] + int(sys.stdin.readline())
#queries
for i in range(int(sys.stdin.readline())):
    poop = [int(i) for i in (sys.stdin.readline().split())]
    print(sumArray[poop[1]+1] - sumArray[poop[0]])
