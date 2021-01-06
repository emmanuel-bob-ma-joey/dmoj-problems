import sys
tests = int(sys.stdin.readline())
for z in range(tests):
    questions,right,wrong,score = [int(i) for i in (sys.stdin.readline().split())]
    if questions*right<score:
        print(-1)
    else:
        number = int((questions*right-score)/(right+wrong))
        print(questions-number)
