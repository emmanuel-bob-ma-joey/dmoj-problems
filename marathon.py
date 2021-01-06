import sys
nums = [int(i) for i in (sys.stdin.readline().split())]
episodes = nums[0]
queries = nums[1]
sumList = [0]
sumList.extend([int(i) for i in (sys.stdin.readline().split())])
for i in range(1,len(sumList)):
    sumList[i] += sumList[i-1]
total = sumList[episodes]
for i in range(queries):
    poop = [int(i) for i in (sys.stdin.readline().split())]
    print(total - (sumList[poop[1]] - sumList[poop[0]-1]))
