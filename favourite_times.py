import sys

def findSequence(minutes):
    clock = [1,2,0,0]
    counter = 0
    if minutes <= 720:
        for i in range(minutes):
            clock[3] += 1
            if clock[3] == 10:
                clock[3] = 0
                clock[2] +=1
                if clock[2] == 6:
                    clock[2] = 0
                    clock[1] +=1
                    if clock[1] == 3:
                        if clock[0] == 1:
                            clock[0] = 0
                            clock[1] = 1
                    elif clock[1] == 10:
                        clock[0]+=1
                        clock[1] = 0
            if clock[0] == 0:
                if (clock[3]-clock[2]) == (clock[2]-clock[1]):
                    counter+=1
            else:
                if (clock[3]-clock[2]) == (clock[2]-clock[1])==(clock[1]-clock[0]):
                    counter+=1
    return counter
minutes = int(sys.stdin.readline())
if minutes <= 720:
    print(findSequence(minutes))
else:
    multiply = minutes//720
    answer = findSequence(minutes%720)
    print(answer+(multiply*31))
