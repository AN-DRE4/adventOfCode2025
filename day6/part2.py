from icecream import ic

smallInput = "inputSmall.txt"
bigInput = "inputBig.txt"

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= int(number)
    return total

total = 0
numberInColumnBiggestSize = []
with open(bigInput, "r") as file:
    lines = file.readlines()
    problemMatrix = []
    for line in lines:
        line = line.strip()
        line = line.split()
        problemMatrix.append(line)
    for j in range(len(problemMatrix[0])):
        biggestSize = 0
        for i in range(len(problemMatrix)):
            if len(problemMatrix[i][j]) > biggestSize:
                biggestSize = len(problemMatrix[i][j])
        numberInColumnBiggestSize.append(biggestSize)
    newMatrix = []
    numberInColumnBiggestSize = numberInColumnBiggestSize[::-1]
    for line in lines:
        line = line.replace("\n", "")
        line = list(line)
        line.reverse()
        newLine = []
        for number in numberInColumnBiggestSize:
            newLine.append(line[:number])
            line = line[number+1:]
        newMatrix.append(newLine)
    for j in range(len(newMatrix[0])):
        signal = ''
        numbers = []
        for k in range(numberInColumnBiggestSize[j]):
            number = ''
            for i in range(len(newMatrix)):
                if newMatrix[i][j][k] == '+':
                    signal = '+'
                elif newMatrix[i][j][k] == '*':
                    signal = '*'
                number += newMatrix[i][j][k] if newMatrix[i][j][k] != ' ' and i != len(newMatrix) - 1 else ''
            numbers.append(number)
        if signal == '+':
            total += sum(int(number) for number in numbers)
        elif signal == '*':
            total += multiply(int(number) for number in numbers)
    print(total)