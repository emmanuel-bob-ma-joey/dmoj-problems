import sys
slices = int(sys.stdin.readline())
people = int(sys.stdin.readline())
savedList = [[0 for i in range(slices+1)] for i in range(people+1)]
for i in range(1,slices+1):
    savedList[1][i] = 1

for n in range(1,people+1):
    savedList[n][n] = 1
total = 0

for currentPeopleIndex in range(2,(people+1)):
    for currentSliceIndex in range(currentPeopleIndex+1,slices+1):
        num = 0
        for i in range(currentPeopleIndex,-1,-1):
            num+= savedList[i][currentSliceIndex - currentPeopleIndex]
        savedList[currentPeopleIndex][currentSliceIndex] = num
print(savedList[people][slices])
