import sys
nums = [int(i) for i in (sys.stdin.readline().split())]
adjacencyList = [[] for i in range(nums[0]+1)]
for i in range(nums[1]):
    path = [int(i) for i in (sys.stdin.readline().split())]
    adjacencyList[path[0]].append(path[1])

masterMinList = [[9999 for i in range(nums[0]+1)] for i in range(nums[0]+1)]
masterVisitedList = [[False for i in range(nums[0]+1)] for i in range(nums[0]+1)]

for i in range(1,nums[0]+1):
    queue = [i]
    masterVisitedList[i][i] = True
    masterMinList[i][i] = 0
    while queue:
        n = queue.pop(0)
        #might have to code stop when adjacencyList = []
        for e in adjacencyList[n]:
            if masterVisitedList[i][e] == False:
                masterVisitedList[i][e] = True
                masterMinList[i][e] = masterMinList[i][n]+nums[2]
                queue.append(e)
for i in range(int(sys.stdin.readline())):
    query = [int(x) for x in (sys.stdin.readline().split())]
    poop = masterMinList[query[0]][query[1]]
    if poop == 9999:
        print('Not enough hallways!')
    else:
        print(poop)
        
