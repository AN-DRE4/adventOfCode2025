from icecream import ic

smallInput = "inputSmall.txt"
bigInput = "inputBig.txt"

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= int(number)
    return total

with open(bigInput, "r") as file:
    lines = file.readlines()
    problemMatrix = []
    for line in lines:
        line = line.strip()
        line = line.split()
        problemMatrix.append(line)
    total = 0
    for j in range(len(problemMatrix[0])):
        sumTotal = 0
        multTotal = 1
        for i in range(len(problemMatrix)):
            if problemMatrix[i][j].isdigit():
                sumTotal += int(problemMatrix[i][j])
                multTotal *= int(problemMatrix[i][j])
            elif problemMatrix[i][j] == '+':
                total += sumTotal
                sumTotal = 0
                multTotal = 1
            elif problemMatrix[i][j] == '*':
                total += multTotal
                sumTotal = 0
                multTotal = 1
    print(total)