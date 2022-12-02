sum = 0

def lose(input):
    hand = input[0]
    if hand == "A":
        return 3
    if hand == "B":
        return 1
    if hand == "C":
        return 2

def draw(input):
    hand = input[0]
    if hand == "A":
        return 4
    if hand == "B":
        return 5
    if hand == "C":
        return 6

def win(input):
    hand = input[0]
    if hand == "A":
        return 8
    if hand == "B":
        return 9
    if hand == "C":
        return 7


with open("input/02.txt") as file:
    for line in file:
        line = line.strip()
        
        if line[2] == 'X':
            sum += lose(line)
        if line[2] == 'Y':
            sum += draw(line)
        if line[2] == 'Z':
            sum += win(line)

print(sum)