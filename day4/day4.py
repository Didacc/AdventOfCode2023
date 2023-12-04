#open and read file
data = open("day4Data", "r")
lines = data.readlines()

i = 0
partResult = 0
totalResult = 0

#correct answer: 27454

for line in lines:
    game = line.split(":")
    gameInfo = game[1]
    gameWinners = gameInfo.split("|")[0].split()
    gameNum = gameInfo.split("|")[1].split()

    for gnum in gameNum:
        if gnum in gameWinners:
            if partResult >= 1: partResult = partResult * 2
            else: partResult = 1
            
    totalResult += partResult
    partResult = 0

print("Final result =",totalResult)