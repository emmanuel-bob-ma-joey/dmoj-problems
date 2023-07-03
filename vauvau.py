import sys
nums = [int(i) for i in (sys.stdin.readline().split())]
queries = [int(i) for i in (sys.stdin.readline().split())]
dog1 = nums[0]+nums[1]
dog2 = nums[2]+nums[3]
for time in queries:
    answer = 0
    if 0<time%dog1 <= nums[0]:
        answer+=1
    if 0<time%dog2 <= nums[2]:
        answer+=1
    
    if answer == 0:
        print('none')
    elif answer == 1:
        print('one')
    else:
        print('both')
