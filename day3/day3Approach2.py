#open and read file
data = open("day3Data", "r")
lines = data.readlines()
symbols = "!@#$%^&*()_-+={}[]"
symbolsCoord = []
numberCoord = []
numSymCoord = []
totalSum = 0

for iline, line in enumerate(lines):
    for ichar, char in enumerate(line):
        if char in symbols:
            symbolsCoord.append([iline,ichar])
        elif char.isnumeric():
            numberCoord.append([iline,ichar])        

for number in numberCoord:
    for symbol in symbolsCoord:
        if abs(number[0] - symbol[0]) <= 1 and abs(number[1] - symbol[1]) <= 1:
            if len(numSymCoord) == 0:
                numSymCoord.append(number)
            elif not(number[0] == numSymCoord[-1][0] and abs(number[1]-numSymCoord[-1][1]) < 3):
                numSymCoord.append(number)

before_number = after_number = ''
for numSym in numSymCoord:
    linePos = numSym[0]
    charPos = numSym[1]
    for charr in reversed(lines[linePos][:charPos]):
        if charr.isnumeric():
            before_number = charr + before_number
        else:
            break  # Stop when a non-number character is encountered
    for charr in lines[linePos][charPos:]:
        if charr.isnumeric():
            after_number += charr
        else:
            break 
    totalSum += int(before_number+after_number)
    print(before_number+after_number)
    before_number = after_number = ''


print(numSymCoord)

print("Final sum =",totalSum)

#564971