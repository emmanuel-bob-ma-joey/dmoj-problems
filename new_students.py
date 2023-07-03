studentNum = int(input())
markList = []

for i in range(studentNum):
    studentMark = int(input())
    markList.append(studentMark)

initialTotal = sum(markList)

transferNum = int(input())

if (transferNum == 0) and (studentNum != 0):
    print(initialTotal/studentNum)
else:
    for i in range(transferNum):
        transferMark = int(input())
        initialTotal = initialTotal + transferMark

        output = (initialTotal)/(studentNum+(i+1))
        print(round(output,3))
