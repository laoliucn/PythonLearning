# catNames = []

# while True:
# 	print("Please input the number ", len(catNames)+1, " of cat's name, or input nothing to stop.")
# 	currentCat = input()
# 	if currentCat == '':
# 		break
# 	catNames = catNames + [currentCat]
# print("The cat Names are: ")
# for name in catNames:
# 	print(name, " ")

#spam = ['apples', 'bananas', 'tofu', 'cats']

# def printStrList(myList):
# 	output = ""
# 	for item in myList: 
# 		if myList[0] == item:
# 			output += item
# 		elif myList[-1] == item:
# 			output += (" and " + item)
# 		else:	
# 			output += (", "	+ item)
# 	return output
# print(printStrList(spam))	

grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]
#print(grid[0][6])

for i in range(len(grid[0])):
	for j in range(len(grid)+5):
		try:
			print(grid[j][i], end = " ")
		except Exception as e:
			print(e.__context__, "i = ", i, "j = ", j)
			exit()
		
	print() 

