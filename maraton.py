import sys
dimensions = int(sys.stdin.readline())
grid = [list(sys.stdin.readline()) for i in range(dimensions)]
#print(grid)
dx = [-1,+1,0,0]
dy = [0,0,-1,+1]
answer = 'ongoing'
for i in range(dimensions-2):
    for x in range(dimensions-2):
        if grid[i][x] != '.':
            if grid[i][x] == grid[i+1][x] == grid[i+2][x]:
                answer = grid[i][x]
                break
            elif grid[i][x] == grid[i][x+1] == grid[i][x+2]:
                answer = grid[i][x]
                break
            elif grid[i][x] == grid[i+1][x+1] == grid[i+2][x+2]:
                answer = grid[i][x]
                break
            elif (i-2) >=0:
                if grid[i][x] == grid[i-1][x+1] == grid[i-2][x+2]:
                    answer = grid[i][x]
                    break
                
    if answer != 'ongoing':
        break
if answer != 'ongoing':
    print(answer)
else:
    for i in range(dimensions-2,dimensions):
        for x in range(dimensions):
            if grid[i][x] != '.':
                if grid[i][x] == grid[i-1][x+1] == grid[i-2][x+2]:
                    answer = grid[i][x]
                    break
                elif grid[i][x] == grid[i][x+1] == grid[i][x+2]:
                    answer = grid[i][x]
                    break
                    
        if answer != 'ongoing':
            break
    if answer != 'ongoing':
        print(answer)
    else:
        for i in range(dimensions-2):
            for x in range(dimensions-2,dimensions):
                if grid[i][x] != '.':
                    if grid[i][x] == grid[i+1][x] == grid[i+2][x]:
                        answer = grid[i][x]
                        break
            if answer != 'ongoing':
                break
        print(answer)
