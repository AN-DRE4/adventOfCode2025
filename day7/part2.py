from icecream import ic

smallInput = "inputSmall.txt"
bigInput = "inputBig.txt"

total = 0
with open(bigInput, "r") as file:
    lines = file.readlines()
    beamsLocations = ''.zfill(len(lines[0].strip()))
    beamsLocations = list(map(int, beamsLocations))
    for index, char in enumerate(lines[0].strip()):
        if char == 'S':
            beamsLocations[index] = 1
            break
    for index1, line in enumerate(lines[1:]):
        line = line.strip()
        for index, char in enumerate(line):
            if char == '^' and beamsLocations[index] != 0:
                beamsLocations[index-1] += beamsLocations[index]
                beamsLocations[index+1] += beamsLocations[index]
                beamsLocations[index] = 0
    total = sum(beamsLocations)
    ic(total)