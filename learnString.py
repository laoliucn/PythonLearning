import pyperclip

# print('''Dear Alice

# Eve\'s cat

# Sincerely,
# Bob''')

# print('Hello'.center(20, '*'))

# pyperclip.copy('Hello my clipboard!!!!!!')
# print(pyperclip.paste())

tableData = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'], 
            ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    colWidths = [0]*len(tableData)
    
    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            if colWidths[i] < len(tableData[i][j]):
                colWidths[i] = len(tableData[i][j])

    #print(colWidths)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()

printTable(tableData)
