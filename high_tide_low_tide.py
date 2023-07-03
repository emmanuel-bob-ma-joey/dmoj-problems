import sys
num = int(sys.stdin.readline())
tideList = [int(i) for i in (sys.stdin.readline().split())]
tideList.sort()
lowtide = list(tideList[0:num - int(num/2)])
hightide = list(tideList[num - 1 - int(num/2)+1:(num)])

lowtide.sort(reverse=True)
loop = True
poop = []
while loop:
    if lowtide:
        poop.append(lowtide.pop(0))
        if hightide:
            poop.append(hightide.pop(0))
    else:
        loop = False
print(*poop)
