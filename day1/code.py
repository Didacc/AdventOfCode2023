data = open("data", "r")
lines = data.readlines()
firstFound = False
firstIndex = 0
secondIndex = 0
numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
totalSum = 0

#answer: 52834 

for line in lines:
    for char in line:
        if char.isnumeric() and not firstFound:
            firstNumber = char
            firstFound = True
            firstIndex = line.index(char)
        if char.isnumeric() and firstFound:
            secondNumber = char   
            secondIndex = line.index(char)
    
    
    for number in numbers:
        if number in line: 
            textNum = numbers[number]
            textNumIndex = line.index(number)
            print("number: ",textNum,", with index: ",textNumIndex, ", with ocurrences: ",line.count(number))
            if textNumIndex < firstIndex: 
                firstNumber = textNum
                firstIndex = textNumIndex
            elif textNumIndex > secondIndex: 
                secondNumber = textNum
                secondIndex = textNumIndex
                
            if line.count(number) > 1: #case when the same number in text appears more than once
                textNumIndex = line.index(number,textNumIndex+1) 
                if textNumIndex > secondIndex: 
                    secondNumber = textNum
                    secondIndex = textNumIndex
            
            if line.count(number) > 2:
                textNumIndex = line.index(number,textNumIndex+1) 
                if textNumIndex > secondIndex: 
                    secondNumber = textNum
                    secondIndex = textNumIndex 


    if secondNumber == None : secondNumber = firstNumber
    print("first: ",firstNumber,"\nsecond: ",secondNumber,"\n")
    totalSum += int(str(firstNumber)+str(secondNumber))

    # reset values
    firstNumber = None
    secondNumber = None
    firstFound = False
    firstIndex = 0
    secondIndex = 0

print(totalSum)
