import sys

for i in range(int(sys.stdin.readline())):
    words = sys.stdin.readline().split()
    times = [1 for i in range(len(words))]
    for x in range(len(words)):
        for n in range(x+1,len(words)):
            if words[x] == words[n]:
                times[x] += 1
    poop = []
    for i in range(len(times)):
        if times[i] == max(times):
            poop.append(words[i])
    if len(poop) != 1:
        print('???')
    else:
        print(poop[0])
