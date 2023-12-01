#open and read file
data = open("data", "r")
lines = data.readlines()

firstFound = False
firstIndex = 0
secondIndex = 0
numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
totalSum = 0

#correct answer: 52834 

for line in lines:

    #manage numerical numbers(1,2,...)
    for char in line:
        if char.isnumeric() and not firstFound:
            firstNumber = char
            firstFound = True
            firstIndex = line.index(char)
        if char.isnumeric() and firstFound:
            secondNumber = char   
            secondIndex = line.index(char)
    
    #manage text numbers (one,two,...)
    for number in numbers:
        if number in line: 
            textNum = numbers[number]
            textNumIndex = line.index(number)
            
            if textNumIndex < firstIndex: 
                firstNumber = textNum
                firstIndex = textNumIndex
                
            for i in range(line.count(number)): # using a for bc some number in text is reppeated
                textNumIndex = line.index(number,textNumIndex + i) 
                if textNumIndex > secondIndex: 
                    secondNumber = textNum
                    secondIndex = textNumIndex 


    if secondNumber == None : secondNumber = firstNumber
    totalSum += int(str(firstNumber)+str(secondNumber))

    # reset values
    firstNumber = None
    secondNumber = None
    firstFound = False
    firstIndex = 0
    secondIndex = 0

print("Final sum result = ", totalSum)
