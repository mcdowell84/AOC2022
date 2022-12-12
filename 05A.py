def crateCleaner(input):
    #create baselist
    crates = []
    stringlength = len(input[0])
    for i in range(stringlength):
        crates.append('')
    
    #add alphanumerics to list, remove other characters
    for count, value in enumerate(input):
        for charcount, char in enumerate(value):
            if char.isupper() == True:
                oldstring = crates[charcount]
                newstring = oldstring + char
                crates[charcount] = newstring
            else:
                continue
    # clean up emtpies
    crates = list(filter(None, crates))
    
    return crates


with open("input/05.txt") as file:
    sample = file.readlines()
    #manually adjust the splitpoint
    splitpoint = 8
    messy_crates = sample[0:splitpoint]

    messy_crates.reverse()

    guide = sample[splitpoint+2:]
    crates = crateCleaner(messy_crates)
    
    #process the guide
    for line in guide:
        line = line[5:].strip()
        line = line.replace(' from ', ',')
        line = line.replace(' to ', ',')
        command = line.split(',')
        command = [int(x) for x in command]

        amt = command[0]
        src = command[1]
        tgt = command[2]
        #remove payload from target
        crates[src-1], payload = crates[src-1][:-amt], crates[src-1][-amt:]
        
        #reverse and place
        payload = payload[::-1]
        crates[tgt-1] = crates[tgt-1] + payload

answer = ''
for line in crates:
    answer = answer + line[-1]
print(answer)