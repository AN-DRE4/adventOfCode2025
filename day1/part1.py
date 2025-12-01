lista = [x for x in range(100)]

current_position = 50
password = 0

with open('puzzleInputPart1.txt', 'r') as file:
    for line in file:
        side = line[0]
        steps = int(line[1:])
        if side == 'L':
            current_position -= steps
        elif side == 'R':
            current_position += steps
        while current_position < -100:
            current_position = current_position + 100
        while current_position >= 100:
            current_position = current_position - 100
        if lista[current_position] == 0:
            password += 1
    print(password)