import random

board = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]


# this function prints our board in a neat format 
def printBoard(bo):
	for i in range(len(bo)):
		if i % 3 == 0 and i != 0:
			print('-'*21)
		for j in range(len(bo[0])):
			if j % 3 == 0 and j!= 0:
				print('| ', end='')
			# i = row j = col
			if j == 8:
				print(bo[i][j])
			else:
				print(bo[i][j], end=' ')

#this function finds the next empty square in our board and returns its location
#if all locations are filled, it returns False to indicate a complete board
def empty(bo):
	for x in range(len(bo)):
		for y in range(len(bo[0])):
			if bo[x][y] == 0:
				return (x,y) #row, col
	return False

#this function will test numbers 1 thru 9 to fill a certain board location and 
#check to see if the conditions of row, col, and box are met
def checkValid(bo, num, pos): #(board, number to test, position)
	#check row
	for i in range(len(bo)):
		if bo[pos[0]][i] == num and pos[1]!= i:
			return False
	#check col
	for i in range(len(bo)):
		if bo[i][pos[1]] == num and pos[0]!= i:
			return False
	#check box
	boxRow = (pos[0]//3)*3
	boxCol = (pos[1]//3)*3
	for i in range(boxRow,boxRow+3):
		for j in range(boxCol,boxCol+3):
			if bo[i][j] == num and (i,j)!= pos:
				return False
	return True

# this is our main solver
#it first calls empty() to find the postion of the next open square
#then it calls checkValid() to find a valid number to insert into the open square
#if a number is found, it will insert the new number in the spot
	# then call a solver() again recursively 
	#as long as it is True we keep solving next square
		#if false then set the square back to 0 and test the numbers until 9 to find another that fits
#else return false so that the recursion will trigger backtracking of previous 
def solver(bo):
	emptyPos = empty(bo)
	if emptyPos == False:
		return True
	else:
		row, col = emptyPos
	for i in range(1,10):
		if checkValid(bo,i,(row,col)):
			bo[row][col] = i
			if solver(bo) == True:
				return True
			else:
				bo[row][col] = 0
			
	return False


def fillBoard(bo):
	emptyPos = empty(bo)
	if emptyPos == False:
		return True
	else:
		row, col = emptyPos
	x = list(range(1,10))
	random.shuffle(x)
	for i in x:
		if checkValid(bo,i,(row,col)):
			bo[row][col] = i
			if fillBoard(bo) == True:
				return True
			else:
				bo[row][col] = 0
			
	return False

def checkSol(bo):
	global counter
	counter = 0
	emptyPos = empty(bo)
	if emptyPos == False:
		return True
	else:
		row, col = emptyPos
	for i in range(1,10):
		if checkValid(bo,i,(row,col)):
			bo[row][col] = i
			if checkSol(bo) == True:
				counter+=1
			bo[row][col] = 0



def randBox():
	return random.randint(0,8),random.randint(0,8)

def removeNum(bo,lvl):
	global attempts
	global counter

	while attempts < lvl:
		row, col = randBox()
		if bo[row][col] != 0:
			testNum = bo[row][col]
			bo[row][col] = 0

			copyBoard = []
			for r in range(0,9):
				copyBoard.append([])
				for c in range(0,9):
					copyBoard[r].append(bo[r][c])
			checkSol(copyBoard)
			if counter!= 1:
				bo[row][col] = testNum
				attempts+=1
global attempts
attempts = 0
def main():
	print('Welcome to the Sudoku Puzzle Generator!')
	print('This program will generate a unique Sudoku puzzle based on a difficulty level')
	print(format('Easy - 1','<12s')+format('Medium - 2','<12s')+format('Hard - 3', '<12s'))
	level = int(input('Please Enter Difficulty Level: '))
	if level == 1:
		level = 10
	elif level == 2:
		level = 15
	elif level == 3:
		level = 20
	print('Generating...')
	print()
	fillBoard(board)
	removeNum(board,level)
	print('Here is your board!')
	print()
	printBoard(board)
	input('Press Enter to Solve:')
	solver(board)
	print('-'*21)
	printBoard(board)
	input('Thanks For Playing! Hit Enter to exit!')

main()

