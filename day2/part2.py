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
                for i in range(1, itemSize):
                    # if the itemSize%i is 0, then check if all the parts are the same
                    if itemSize%i == 0:
                        parts = [str(item)[j:j+i] for j in range(0, itemSize, i)]
                        if all(parts[0] == part for part in parts):
                            print(item)
                            total += item
                            break
    print(total)