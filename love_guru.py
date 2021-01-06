import sys
boy = sys.stdin.readline().lower()
girl = sys.stdin.readline().lower()
cycles = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [0]]
answer = 0
for i in range(len(boy)-1):
    poop = (ord(boy[i])-96)%10
    answer+= cycles[poop][(i+1)%len(cycles[poop])-1]
answer%= 10
if answer == 0:
    answer = 10
    
output = 0

for i in range(len(girl)-1):
    poop = (ord(girl[i])-96)%10
    output += cycles[poop][(i+1)%len(cycles[poop])-1]
output %= 10
if output == 0:
    output = 10
print(answer+output)
