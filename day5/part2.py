from icecream import ic

smallInput = "smallInput.txt"
bigInput = "bigInput.txt"

with open(bigInput, "r") as file:
    ranges, _ = file.read().strip().split("\n\n")
    ranges = ranges.split("\n")
    ranges = [tuple(map(int, line.split('-'))) for line in ranges]
    ranges.sort()
    finalRanges = []
    currentLow, currentHigh = ranges[0]
    for newLow, newHigh in ranges[1:]:
        if newLow <= currentHigh:
            currentHigh = max(currentHigh, newHigh)
        else:
            finalRanges.append((currentLow, currentHigh))
            currentLow, currentHigh = newLow, newHigh
    finalRanges.append((currentLow, currentHigh))
    total = sum(high - low + 1 for low, high in finalRanges)
    print(total)