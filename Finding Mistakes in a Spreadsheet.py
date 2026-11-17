#Finding Mistakes in a Spreadsheet

import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

#Print the number of the row with the wrong result

for line in range(2, ss[0].rowCount + 1):
    if not (int(ss[0].getRow(line)[0]) \
            * int(ss[0].getRow(line)[1]) == int(ss[0].getRow(line)[2])):
        print('Mistake on line: ', line)
        break
