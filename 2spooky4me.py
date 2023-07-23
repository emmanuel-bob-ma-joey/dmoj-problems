import sys, collections

decorations, houses, limit = [int(i) for i in (sys.stdin.readline().split())]
hashmap = {}

for i in range(decorations):
    start, end, spookiness = [int(i) for i in (sys.stdin.readline().split())]
    if start not in hashmap:
        hashmap[start] = spookiness
    else:
        hashmap[start]+=spookiness
    if (end+1) not in hashmap:
        hashmap[end+1] = -spookiness
    else:
        hashmap[end+1]+=(-spookiness)

hashmap = collecqtions.OrderedDict(sorted(hashmap.items()))

output = houses
previousKey = 0
totalSpookiness = 0
for key, value in hashmap.items():
    #print(key,value)
    if totalSpookiness>=limit:
        output-=(key-previousKey)
    previousKey = key
    totalSpookiness+=value
    
    #print(output)
if totalSpookiness>=limit:
    output-=(houses-previousKey)
print(output)

