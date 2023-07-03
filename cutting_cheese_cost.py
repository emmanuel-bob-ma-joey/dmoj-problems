def partition(array, leftPointer,rightPointer):
    pIndex = leftPointer
    for i in range(leftPointer,rightPointer):
        if array[i]<=array[rightPointer]: #the pivot is the right pointer
            array[pIndex],array[i] = array[i],array[pIndex]
            pIndex+=1
    array[rightPointer],array[pIndex] = array[pIndex],array[rightPointer]
    return (pIndex)


def quickSort(array, leftPointer,rightPointer):
    if leftPointer<rightPointer:
        pivot = partition(array, leftPointer,rightPointer)
        quickSort(array,leftPointer,pivot-1)
        quickSort(array,pivot+1,rightPointer)

blocks,coupons = [int(i) for i in (sys.stdin.readline().split())]
total = 0
differenceList = []
for i in range(blocks):
    regular, discount = [int(i) for i in (sys.stdin.readline().split())]
    total+=regular
    differenceList.append(regular-discount)
quickSort(differenceList,0,blocks-1)
for i in range(blocks-1,blocks-coupons-1,-1):
    total-=differenceList[i]
print(total)
