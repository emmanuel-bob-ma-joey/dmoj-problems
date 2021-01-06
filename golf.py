import sys

hole = int(sys.stdin.readline())
club = int(sys.stdin.readline())
clubList = []
for i in range(club):
    poop = int(input())
    clubList.append(poop)

minClub = [9999]*(hole+ 1)
minClub[0] = 0
for i in range(1,len(minClub)):
    for x in clubList:
        if i - x >= 0:
            temp = (minClub[i - x]+ 1)
            if temp< minClub[i]:
                minClub[i] = temp
        else:
            pass
output = (minClub[hole])

if output == 9999:
    print("Roberta acknowledges defeat.")
else:

    print("Roberta wins in",output,"strokes.")
