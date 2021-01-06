import sys

for z in range(10):
    emails = int(sys.stdin.readline())
    mailList = [[] for i in range(emails)]
    for i in range(emails):
        poop = sys.stdin.readline()
        poop = poop.lower()
        ignore = False
        met = False
        for x in range(len(poop)):
            if poop[x] == '@':
                met  = True
                ignore = False
                mailList[i].append(poop[x])
            elif poop[x] == '.' and (met == False):
                pass
            elif (poop[x] == '+') and (ignore == False) and (met == False):
                ignore = True
            elif ignore == False:
                mailList[i].append(poop[x])
            #elif ignore == True:
                #pass
    newList = []
    for i in mailList:
        newList.append(''.join(i))
    print(len(list(set(newList))))
