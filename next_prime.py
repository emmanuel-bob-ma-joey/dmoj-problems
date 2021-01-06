import sys
num = int(sys.stdin.readline())
if num == 1 or num == 2:
    print(2)

else:
    loop = True
    add = 0
    while loop:

        if (num+add)%2 ==1:
            prime = True
            for i in range(3,int((num+add)**(1/2))+1,2):
                if (num+add)%i == 0:
                    prime = False
                    break
            if prime == True:
                print(num+add)
                loop = False
        add+=1
