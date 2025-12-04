from icecream import ic

inputTxtSmall = "inputSmall.txt"
inputTxtBig = "inputBig.txt"

global mapMatrix 
mapMatrix = []
global total 
total = 0

def checkSurroundings(index, index2, mapMatrix):
    surrounding = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if index+i < 0 or index+i >= len(mapMatrix) or index2+j < 0 or index2+j >= len(mapMatrix[0]):
                continue
            if mapMatrix[index+i][index2+j] == '@':
                surrounding.append(mapMatrix[index+i][index2+j])
    return 1 if len(surrounding) < 4 else 0

with open(inputTxtBig, 'r') as file:
    for line in file:
        mapMatrix.append(list(line.strip()))

def checkMap(mapMatrix):
    for index, row in enumerate(mapMatrix):
        for index2, cell in enumerate(row):
            if cell == '.':
                continue
            else:
                removable = checkSurroundings(index, index2, mapMatrix)
                if removable == 1:
                    mapMatrix[index][index2] = '.'
                    global total
                    total += 1
    return total

global previousTotal
alterationsDone = True

while alterationsDone:
    previousTotal = total
    alterationsDone = checkMap(mapMatrix)
    if previousTotal == total:
        alterationsDone = False

ic(total)