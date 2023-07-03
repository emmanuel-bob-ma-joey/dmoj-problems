import sys
#import math
nums = [int(i) for i in (sys.stdin.readline().split())]

distanceList = []
for i in range(nums[0]):
    poop = [int(i) for i in (sys.stdin.readline().split())]
    #distanceList.append(math.hypot(poop[0],poop[1]))
    distanceList.append(((poop[0]**2) + (poop[1]**2))**(1/2))
distanceList.sort()
for i in range(nums[1]):
    
    radius = int(sys.stdin.readline())
    if distanceList[nums[0]-1] < radius:
        print(nums[0])
    elif distanceList[0]>radius:
        print(0)
    else:
        start = 0
        end = nums[0]-1
        while (end-start > 1):
            middle = int((start+end)/2)
            if distanceList[middle] > radius:
                end = middle
            else:
                start = middle
        print(end)
