sum = 0

def splitmonkey(input):
    string1 = input[0].strip()
    string2 = input[1].strip()
    string3 = input[2].strip()

    return string1, string2, string3

def checkmonkey(string1, string2, string3):
    result = set(string1).intersection(string2, string3)
    char = result.pop()
    return char

def countmonkey(char):
    if char.islower() == True:
        number = ord(char) - 96
    else:
        number = ord(char) - 64 + 26
    return number

chunked_list = list()
chunk_size = 3

with open("input/03.txt") as file:
    sample = file.readlines()

    for i in range(0, len(sample), chunk_size):
        chunked_list.append (sample[i:i+chunk_size])

for count, value in enumerate(chunked_list):
    setty = splitmonkey(value)
    char = checkmonkey(setty[0], setty[1], setty[2])
    number = countmonkey(char)
    sum += number

print(sum)