import sys
from itertools import permutations

num = sys.stdin.readline()

poopList = []
for i in range(len(num)-1):
    poopList.append(int(num[i]))
peepList = list(poopList)
peepList.sort(reverse = True)
nums = list(permutations(peepList))
answer = False
poopList = [str(i) for i in poopList]
for i in reversed(nums):
    i = [str(x) for x in i]
    if int("".join(i)) > int("".join(poopList)):
        print(int("".join(i)))
        answer = True
        break
if answer == False:
    print(0)
