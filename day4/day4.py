#open and read file
data = open("day4Data", "r")
lines = data.readlines()

i = 0
partResult = 0
totalResult = 0
copies = [1]*len(lines)


for iline,line in enumerate(lines):
    game = line.split(":")
    gameInfo = game[1]
    gameWinners = gameInfo.split("|")[0].split()
    gameNum = gameInfo.split("|")[1].split()

    for gnum in gameNum:
        if gnum in gameWinners:
            partResult += 1

    for i in range(1, partResult+1):
        if iline+i < len(lines):
            copies[iline+i] += copies[iline]
    partResult = 0

for copNum in copies:
    totalResult += copNum 

print("Final result =",totalResult)