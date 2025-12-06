smallInput = "smallInput.txt"
bigInput = "bigInput.txt"

with open(bigInput, "r") as file:
    ranges, numbers = file.read().strip().split("\n\n")
    ranges = ranges.split("\n")
    numbers = numbers.split("\n")
    total = 0
    newRanges = []
    for numberRange in ranges:
        numberRange = numberRange.split("-")
        numberRange = [int(x) for x in numberRange]
        newRanges.append(tuple(numberRange))
    numbers = [int(number) for number in numbers]
    for number in numbers:
        for numberRange in newRanges:
            if number >= numberRange[0] and number <= numberRange[1]:
                total += 1
                break
    print(total)