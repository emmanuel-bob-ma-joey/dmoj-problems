def checklimit(limit,colourlength,total):
    if limit >= colourlength:
        result = colourlength
    elif limit < colourlength:
        result = total - colourlength +1
    return(result)

totalLen = int(input())

redList = []
orangeList = []
yellowList = []
greenList = []
blueList = []
blackList = []

if totalLen <1:
    output = 0
    print(int(output))


else:
    colours = input()
    colourList = colours.split()


    for i in range(len(colourList)):
        colour = colourList[i]
        if colour == "red":
            redList.append(colour)
        elif colour == "orange":
            orangeList.append(colour)
        elif colour == "yellow":
            yellowList.append(colour)
        elif colour == "green":
            greenList.append(colour)
        elif colour == "blue":
            blueList.append(colour)
        else:
            blackList.append(colour)

    redLen = len(redList)
    orangeLen = len(orangeList)
    yellowLen = len(yellowList)
    greenLen = len(greenList)
    blueLen = len(blueList)
    blackLen = len(blackList)

    if totalLen%2 == 0:
        limit = totalLen/2
    else:
        limit = (totalLen+1)/2

    if (redLen or orangeLen or yellowLen or greenLen or blueLen or blackLen) == totalLen:
        output = 1
    elif totalLen == 0:
        output = 0

    else:
        output = int(checklimit(limit,redLen,totalLen) + checklimit(limit,orangeLen,totalLen) + checklimit(limit,yellowLen,totalLen) + checklimit(limit,greenLen,totalLen) + checklimit(limit,blueLen,totalLen) + checklimit(limit,blackLen,totalLen))

    print(output)
