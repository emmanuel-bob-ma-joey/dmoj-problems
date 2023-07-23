import sys

alpacas,happy = [int(i) for i in (sys.stdin.readline().split())]

if (alpacas-happy)%2==1:
    print(-1)
else:
    alpacaList = [0]*alpacas
    for i in range(0,(alpacas-happy),2):
        alpacaList[i] = 1
    print(*alpacaList)
