import sys
nodes,edges = [int(i) for i in (sys.stdin.readline().split())]
poop = 'abcdefghijklmnopqrstuvwxyz'
alphabetList = [i for i in poop]

stringList = [[] for i in range(nodes+1)]
visitedList = [False for i in range(nodes+1)]

if edges>0:
    node1,node2 = [int(i) for i in (sys.stdin.readline().split())]
    stringList[node1] = [1]
    visitedList[node1] = True
    stringList[node2] = [0,2]
    visitedList[node2] = True

for j in range(edges-1):
    node1,node2 = [int(i) for i in (sys.stdin.readline().split())]
    
    if not visitedList[node2]:
        for i in stringList[node1]:
            if i+1 not in stringList[node2]:
                stringList[node2].append(i+1)
            if i-1 not in stringList[node2]:
                stringList[node2].append(i-1)
        visitedList[node2] = True
        
    elif not visitedList[node1]:
        for i in stringList[node2]:
            if i+1 not in stringList[node1]:
                stringList[node1].append(i+1)
            if i-1 not in stringList[node1]:
                stringList[node1].append(i-1)
        visitedList[node1] = True
        
    else:
        if len(stringList[node2])>len(stringList[node1]):
            for i in stringList[node2]:
              if (i+1 in stringList[node1]) or (i-1 in stringList[node1])or (i in stringList[node1]):
                    pass
                else:
                    stringList[node2].remove(i)
        else:
            for i in stringList[node1]:
                if (i+1 in stringList[node2]) or (i-1 in stringList[node2]) or (i in stringList[node2]):
                    pass
                else:
                    stringList[node1].remove(i)
print(stringList)
