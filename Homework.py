import sys
factorList = [0 for i in range(10000001)]
poop = 1
while poop*2 < 10000001:
    factorList[poop*2]+=1
    poop+=1
for i in range(3,10000001,2):
    if factorList[i] == 0:
        poop = 1
        while poop*i < 10000001:
            factorList[poop*i] += 1
            poop+=1

for z in range(int(sys.stdin.readline())):
    nums = [int(i) for i in (sys.stdin.readline().split())]
    answer = 0
    for i in factorList[nums[0]:nums[1]+1]:
        if i == nums[2]:
            answer+=1
    print('Case #'+str(z+1)+': '+str(answer))
