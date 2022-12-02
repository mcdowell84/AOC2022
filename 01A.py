lines = []
calories = []

with open("input/01.txt") as file:
    sum = 0
    for line in file:
        line = line.strip()
        if line != '':
            sum += int(line)
        if line == '':    
            calories.append(sum)
            sum = 0

max_cal = max(calories)

print(max_cal)