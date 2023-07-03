import sys

poop = []
for x in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        if command[1] not in poop:
            print('true')
            poop.append(command[1])
        else:
            print('false')
    elif command[0] == '2':
        if command[1] in poop:
            print('true')
            poop.remove(command[1])
        else:
            print('false')
    elif command[0] == '3':
        if command[1] in poop:
            print(poop.index(command[1]))
        else:
            print(-1)
    elif command[0] == '4':
        if poop == ['true','false']:
            print('false true')
        else:
            print(*poop)
