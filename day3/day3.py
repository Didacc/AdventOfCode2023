#open and read file
data = open("day3Data", "r")
lines = data.readlines()
symbols = "!@#$%^&*()_-+={}[]"

if [8,44 ,554] in [4,68,2,44]:
    print('h2h2')

before_number = ''
after_number = ''

for iline,line in enumerate(lines):
    for ichar,char in enumerate(line):
        if char.isnumeric():
            adjacents = [lines[iline+1][ichar], lines[iline-1][ichar], lines[iline][ichar+1], lines[iline][ichar-1], 
                         lines[iline+1][ichar-1], lines[iline-1][ichar-1], lines[iline+1][ichar+1],lines[iline-1][ichar+1]]
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

                    print("char: ",before_number+after_number, " with index: ",ichar,' in line: ',iline+1)
                    after_number = ''
                    before_number = ''

          


