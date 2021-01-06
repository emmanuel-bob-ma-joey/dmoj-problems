import sys
verses = int(sys.stdin.readline())
poemList = [[sys.stdin.readline().split() for i in range(4)]for x in range(verses)]
for i in poemList:
    syllableList = []
    for x in i:
        lastWord = x[len(x)-1]
        for letter in range(len(lastWord)-1,-1,-1):
                if lastWord[letter].lower() == 'a' or lastWord[letter].lower() == 'e' or lastWord[letter].lower() == 'i' or lastWord[letter].lower() == 'o' or lastWord[letter].lower() == 'u':
                    syllable = lastWord[letter:]
                    syllable = syllable.lower()
                    syllableList.append(syllable)
                    break
                elif letter == 0:
                    syllable = lastWord
                    syllable.lower()
                    syllableList.append(syllable)
    if len(list(set(syllableList))) == 1:
        print('perfect')
    elif (syllableList[0] == syllableList[1]) and (syllableList[2] == syllableList[3]) :
        print('even')
    elif (syllableList[0] == syllableList[3]) and (syllableList[1] == syllableList[2]):
        print('shell')
    elif (syllableList[0] == syllableList[2]) and (syllableList[1] == syllableList[3]):
        print('cross')
    else:
        print('free')
