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
            #print("Steps are bigger than 100, password increased", line.strip())
        if side == 'L':
            last_position = current_position
            current_position = current_position - steps
            if current_position == 0:
                password += 1
                #print("Current position is 0, password increased", line.strip(), last_position, current_position)
            elif current_position < 0:
                current_position = current_position + 100
                if last_position != 0:
                    password += 1
                #print("Sign changed or current position is divisible by 100, password increased", line.strip(), last_position, current_position)
        elif side == 'R':
            last_position = current_position
            current_position = current_position + steps
            if current_position == 100:
                password += 1
                current_position = current_position%100
                #print("Current position is 0, password increased", line.strip(), last_position, current_position)
            elif current_position > 100:
                password += 1
                current_position = current_position%100
                #print("Current position is more than 99 away from last position, password increased", line.strip(), last_position, current_position)
        print(password)
        
        