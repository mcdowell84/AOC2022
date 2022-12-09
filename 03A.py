sum = 0

def splitmonkey(input):
    string1 = input[0:len (input) //2]
    string2 = input[len(input)//2: len(input)]
    return string1, string2

def checkmonkey(string1, string2):
    result = set(string1).intersection(string2)
    char = result.pop()
    return char

def countmonkey(char):
    if char.islower() == True:
        number = ord(char) - 96
    else:
        number = ord(char) - 64 + 26
    return number

with open("input/03.txt") as file:
    for line in file:
        line = line.strip()
        result = splitmonkey(line)
        char = checkmonkey(result[0], result[1])
        number = countmonkey(char)
        sum += number

print(sum)