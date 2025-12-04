inputTxtSmall = "inputSmall.txt"
inputTxtBig = "inputBig.txt"

with open(inputTxtBig, 'r') as file:
    total = 0
    for line in file:
        line = line.strip()
        print(line)
        biggest = 0
        nextBiggest = 0
        for index, number in enumerate(line):
            number = int(number)
            if number > biggest and index != len(line) - 1:
                biggest = number
                nextBiggest = int(line[index + 1])
            elif number > nextBiggest:
                nextBiggest = number
        newNum = str(biggest) + str(nextBiggest)
        total += int(newNum)
    print(total)