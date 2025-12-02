inputTxtSmall = "puzzleInputSmall.txt"
inputTxtBig = "puzzleInputBig.txt"

with open(inputTxtBig, 'r') as file:
    total = 0
    for line in file:
        line = line.strip()
        line = line.split(',')
        for rng in line:
            rng = rng.split('-')
            rngLeft = int(rng[0])
            rngRight = int(rng[1])
            lista = [x for x in range(rngLeft, rngRight + 1)]
            for item in lista:
                itemSize = len(str(item))
                leftSide = str(item)[:itemSize//2]
                rightSide = str(item)[itemSize//2:]
                #print(leftSide, rightSide)
                if leftSide == rightSide:
                    total += item
    print(total)