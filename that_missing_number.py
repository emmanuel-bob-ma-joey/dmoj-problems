import sys
for z in range(5):
    numsremaining = int(sys.stdin.readline())
    numList = [0 for i in range(numsremaining+1)]
    for i in range(numsremaining):
        poop = int(sys.stdin.readline())
        numList[poop-1] = poop
    for i in range(len(numList)):
        if numList[i] == 0:
            print(i+1)
