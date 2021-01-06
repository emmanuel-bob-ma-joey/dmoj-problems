import sys
from itertools import combinations

ingredients = int(sys.stdin.readline())
ingredientList = [[int(i) for i in (sys.stdin.readline().split())] for x in range(ingredients)]

difference = 999999
for x in range(1,ingredients+1):
    poop = list(combinations(ingredientList,x))
    poop = [list(i) for i in poop]
    for i in poop:
        first = 1
        second = 0
        for z in i:
            second+=z[1]
            first*=z[0]
        if abs(second-first) < difference:
            difference = abs(second-first)
print(difference)
