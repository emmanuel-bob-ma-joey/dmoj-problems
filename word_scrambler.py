import sys
from itertools import permutations

letters = input()

sortedLetters = sorted(letters)
finishedString = ''.join(sortedLetters)

[print(''.join(i)) for i in permutations(finishedString)]
