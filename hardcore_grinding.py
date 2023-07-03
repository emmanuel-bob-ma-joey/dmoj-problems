import sys
tasks = int(sys.stdin.readline())
diffList = [0 for i in range(10000000)]
for i in range(tasks):
    start,end = [int(i) for i in (sys.stdin.readline().split())]
    diffList[start-1]+=1
    diffList[end-1]-=1
for i in range(1,len(diffList)):
    diffList[i] += diffList[i-1]
print(max(diffList))
