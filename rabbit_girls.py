import sys

girls = int(sys.stdin.readline())
groupSize = int(sys.stdin.readline())

time = 0
if girls % groupSize == 0:
    print(time)
else:
    num = (girls - (girls%groupSize))/groupSize
    if num == 0:
        time = abs(int(groupSize - (girls%groupSize)))

    else:
        remainder = (girls - (groupSize*num))
        if remainder >= groupSize/2:
            time = int(abs(groupSize - remainder))
        else:
            time = int(remainder)
    print(time)
