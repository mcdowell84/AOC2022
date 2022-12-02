sum = 0


with open("input/02.txt") as file:
    for line in file:
        line = line.strip()
        
        if line[2] == 'X':
            sum += 1
        if line[2] == 'Y':
            sum += 2
        if line[2] == 'Z':
            sum += 3

        line = line.replace("A", "X")
        line = line.replace("B", "Y")
        line = line.replace("C", "Z")
        
        if line[0] == line[2]:
            sum += 3
            continue

        

        if line[0] == 'X' and line[2] == 'Y':
            sum += 6
        if line[0] == 'X' and line[2] == 'Z':
            sum += 0
        
        if line[0] == 'Y' and line[2] == 'X':
            sum += 0
        if line[0] == 'Y' and line[2] == 'Z':
            sum += 6

        if line[0] == 'Z' and line[2] == 'X':
            sum += 6
        if line[0] == 'Z' and line[2] == 'Y':
            sum += 0

print(sum)