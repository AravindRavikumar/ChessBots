import sys
import chess
import random

def minmaxBest(depth, board):
	moveList = board.legal_moves
	valBest = 10000
	moveBest = ""
	for moveItr in moveList:
		board.push(moveItr)
		#print(moveItr,end=" ")
		value = minmax(depth-1, board, True)
		#print(value)
		board.pop()
		if value == valBest:
			if random.random()*100 < 20:
				moveBest = moveItr
		if value < valBest:
			valBest = value
			moveBest = moveItr
	return moveBest

def minmax(depth, board, isMax):
	if depth == 0:
		return evaluate(board)
	else:
		moveList = board.legal_moves
		if isMax:
			value = -10000
			for moveItr in moveList:
				board.push(moveItr)
				value = max(value, minmax(depth-1, board, False))
				board.pop()
			return value
		else:
			value = 10000
			for moveItr in moveList:
				board.push(moveItr)
				value = min(value, minmax(depth-1, board, True))
				board.pop()
			return value
    			
def evaluate(board):
	boardEval = 0
	for i in range(0,64):
		boardEval += getValue(str(board.piece_at(i)))
		#print(board.piece_at(i))
	return boardEval

def getValue(piece):
	if piece == None:
		return 0
	elif piece == "p":
		return -1
	elif piece == "P":
		return 1
	elif piece == "n" or piece == "b":
		return -3
	elif piece == "N" or piece == "B":
		return 3
	elif piece == "r":
		return -5
	elif piece == "R":
		return 5
	elif piece == "q":
		return -9
	elif piece == "Q":
		return 9
	elif piece == "k":
		return -100
	elif piece == "K":
		return 100
	else:
		return 0

boardPos = ""

for eachArg in sys.argv[1:]:   
	boardPos = boardPos + eachArg + " "

board = chess.Board(boardPos)
legal_moves = [x for x in board.legal_moves] 	#check https://github.com/niklasf/python-chess/issues/226

#print(board.legal_moves)

#randMoveIndex = random.randint(0,len(legal_moves)-1)
bestMove = minmaxBest(3,board)

#print(legal_moves[randMoveIndex])	
print(bestMove)