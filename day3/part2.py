inputTxtSmall = "inputSmall.txt"
inputTxtBig = "inputBig.txt"

with open(inputTxtBig, 'r') as file:
    total = 0
    for line in file:
        #for line in file:
        line = line.strip()
        line = list(map(int, str(line)))
        numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][::-1]
        strbiggestNumber = ""
        while len(strbiggestNumber) < 12:
            for number in numberList:
                numberIndex = 0
                if number in line:
                    numberIndex = line.index(number)
                else:
                    continue
                sizeToCheck = len(line) - 12 + len(strbiggestNumber)
                if numberIndex <= sizeToCheck:
                    strbiggestNumber += str(number)
                    line = line[numberIndex+1:]
                    break
        total += int(strbiggestNumber)
    print("Total: ", total)