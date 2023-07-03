import sys

for z in range(int(sys.stdin.readline())):
    factorList = []
    poop = int(sys.stdin.readline())
    num = poop
    while num%2 == 0:
        factorList.append(2)
        num/=2
    
        
    for i in range(3,int(poop**(1/2))+2,2):
        while num%i == 0:
            factorList.append(i)
            num /= i
        
    if (poop != num) and num != 1:
        factorList.append(int(num))
    
    if factorList == []:
        print(num)
    else:
        print(*factorList)
