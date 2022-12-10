sum = 0

def createStartEnd(input):
    separated = input.split(',')
    elf1 = separated[0].split('-')
    elf2 = separated[1].split('-')
    elf1A = int(elf1[0])
    elf1B = int(elf1[1])
    elf2A = int(elf2[0])
    elf2B = int(elf2[1])
    return elf1A, elf1B, elf2A, elf2B

def createList(r1, r2):
    return list(range(r1, r2+1))

def checkRange(r1, r2):
    overlap = list(set(r1) & set(r2))
    if len(overlap)>0:
        return True
    else:
        return False
    

with open("input/04.txt") as file:
    for line in file:
        line = line.strip()

        allpoints = createStartEnd(line)
        
        range1 = createList(allpoints[0], allpoints[1])
        range2 = createList(allpoints[2], allpoints[3])
        result = checkRange(range1, range2)
        if result == True:
            sum += 1

print(sum)