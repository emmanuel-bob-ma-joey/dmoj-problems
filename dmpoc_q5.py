import sys
import math

students,k = [int(i) for i in (sys.stdin.readline().split())]

if k == 1:
    answer = []
    for i in range(students):
        answer.append(sys.stdin.readline().strip('\n'))
    print("".join(answer))
    
else:
    answer = []
    stringList = []
    studentList = [[] for i in range(students)]
    
    for i in range(students):
        poop = sys.stdin.readline().strip('\n')
        for x in poop:
            studentList[i].append(x)
            
    stringLength = students+k-1
    index = math.ceil(stringLength/k)

    stringList.append(studentList.pop(0))
    for i in studentList:
        if i[0] == stringList[len(stringList)-1][k-1]:
            stringList.append(i)
            studentList.remove(i)
            
    for i in studentList:
        if i[k-1] == stringList[0][0]:
            stringList.insert(0,i)
            studentList.remove(i)
            
    for i in studentList:
        stringList.append(i) 
        
    stringList = stringList[0:index]
    
    try:
        for i in range(int(stringLength/k)):
            del stringList[i+1][0]
            
        for i in stringList:
            for x in i:
                answer.append(x)
                
        poop = "".join(answer)
        if len(poop) == stringLength:
            print(poop)
        else:
            print(-1)
    except:
        print(-1)
