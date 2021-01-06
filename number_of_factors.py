import sys

primeList = [2,3,5,7,11,13,15]
for i in range(5):
    num = int(sys.stdin.readline())
    primeNums = 0
    for x in primeList:
        loop = True
        while loop:
            if (num%x == 0) and (num!= 0):
                primeNums+=1
                num /= x
            else:
                loop = False
    if primeNums ==1:
        primeNums-= 1
    print(primeNums)
