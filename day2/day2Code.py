#open and read file
data = open("dataDay2", "r")
lines = data.readlines()

minBlue = minGreen = minRed = 0
finalNum = 0

for line in lines:
    allInfo = line.split(":")
    gameNumber = allInfo[0].split()[1]
    cubes = allInfo[1].split(";")
    
    for cube in cubes:
        cubeInfo = cube.split(",")
        for cubeNumColor in cubeInfo:
            cubeNumColorSep = cubeNumColor.split()
            number = int(cubeNumColorSep[0])
            color = cubeNumColorSep[1]
            if color == "red" and number > minRed: minRed = number
            elif color == "green" and number > minGreen: minGreen = number
            elif color == "blue" and number > minBlue: minBlue = number
    
    finalNum += (minBlue * minGreen * minRed)
    minBlue = minGreen = minRed = 0


print("Final Result:",finalNum)

