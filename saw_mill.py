sawNum = int(input())
sawEnergy = input()
logLength = input()

sawList = [int(i) for i in (sawEnergy.split())]
logList = [int(i) for i in (logLength.split())]
sawList.sort()
logList.sort(reverse = True)

total = 0
for i in range(sawNum):
    total += (logList[i] * sawList[i])
print(total)
