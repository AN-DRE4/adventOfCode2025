import numpy as np

last_position = None
current_position = 50
password = 0

inputTxtBig = "puzzleInputBig.txt"
inputTxtSmall = "puzzleInputSmall.txt"

with open(inputTxtBig, 'r') as file:
    signal = True
    for line in file:
        side = line[0]
        steps = int(line[1:])
        while steps >= 100:
            steps = steps - 100
            password += 1
        if side == 'L':
            last_position = current_position
            current_position = current_position - steps
            if current_position == 0:
                password += 1
            elif current_position < 0:
                current_position = current_position + 100
                if last_position != 0:
                    password += 1
        elif side == 'R':
            last_position = current_position
            current_position = current_position + steps
            if current_position == 100:
                password += 1
                current_position = current_position%100
            elif current_position > 100:
                password += 1
                current_position = current_position%100
        print(password)
        
        