import sys
nums = [int(i) for i in (sys.stdin.readline().split())]
infoList = []
for i in range(nums[0]):
    poop = [0,sys.stdin.readline()]
    infoList.append(poop)
for i in range(nums[1]):
    minutes = [int(x) for x in (sys.stdin.readline().split())]
    for x in range(len(minutes)):
        infoList[x][0] += minutes[x]
infoList.sort(reverse = True)
for i in range(3,nums[0]+3):
    print('{}.'.format(i),infoList[i-3][1])
