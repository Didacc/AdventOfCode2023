#open and read file
data = open("day3Data", "r")
lines = data.readlines()
symbols = "!@#$%^&*()_-+={}[]"

partialNumSum = 0

before_number = ''
after_number = ''
partNum = ''
previousPartNum = 99

for iline,line in enumerate(lines):
    for ichar,char in enumerate(line):
        if char.isnumeric():
            if iline<len(lines)-1: adjacents = [lines[iline+1][ichar], lines[iline-1][ichar], lines[iline][ichar+1], lines[iline][ichar-1], 
                         lines[iline+1][ichar-1], lines[iline-1][ichar-1], lines[iline+1][ichar+1],lines[iline-1][ichar+1]]
            elif ichar<len(line)-1: adjacents = [lines[iline-1][ichar], lines[iline][ichar+1], lines[iline][ichar-1], 
                          lines[iline-1][ichar-1],lines[iline-1][ichar+1]]
                
            for adjacent in adjacents:
                if adjacent in symbols:
                    
                    for charr in reversed(line[:ichar]):
                        if charr.isnumeric():
                            before_number = charr + before_number
                        else:
                            break  # Stop when a non-number character is encountered
                    for charr in line[ichar:]:
                        if charr.isnumeric():
                            after_number += charr
                        else:
                            break 
                    

                    if abs(ichar-previousPartNum) > 2: partNum = before_number+after_number
                    else: 
                        after_number = ''
                        before_number = ''
                        continue



                    print("partnum: ", partNum, ", previouspartnum:",previousPartNum," with index: ",ichar,' in line: ',iline+1)
                    partialNumSum += int(partNum)
                    after_number = ''
                    before_number = ''
                    previousPartNum = ichar
    previousPartNum = 99

#475145
print(partialNumSum)

          


