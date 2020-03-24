import sys
import chess
import random

#check https://www.chessprogramming.org/Simplified_Evaluation_Function for position values
bPawnPosValue = [0,  0,  0,  0,  0,  0,  0,  0,
				50, 50, 50, 50, 50, 50, 50, 50,
				10, 10, 20, 30, 30, 20, 10, 10,
				5,  5, 10, 25, 25, 10,  5,  5,
				0,  0,  0, 20, 20,  0,  0,  0,
				5, -5,-10,  0,  0,-10, -5,  5,
				5, 10, 10,-20,-20, 10, 10,  5,
				0,  0,  0,  0,  0,  0,  0,  0]

wPawnPosValue = [0,  0,  0,  0,  0,  0,  0,  0,
				5, 10, 10,-20,-20, 10, 10,  5,
				5, -5,-10,  0,  0,-10, -5,  5,
				0,  0,  0, 20, 20,  0,  0,  0,
				5,  5, 10, 25, 25, 10,  5,  5,
				10, 10, 20, 30, 30, 20, 10, 10,
				50, 50, 50, 50, 50, 50, 50, 50,
				0,  0,  0,  0,  0,  0,  0,  0]

bKnightPosValue = [-50,-40,-30,-30,-30,-30,-40,-50,
				-40,-20,  0,  0,  0,  0,-20,-40,
				-30,  5, 15, 20, 20, 15,  5,-30,
				-30,  0, 15, 20, 20, 15,  0,-30,
				-30,  5, 10, 15, 15, 10,  5,-30,
				-30,  0, 10, 15, 15, 10,  0,-30,
				-40,-20,  0,  5,  5,  0,-20,-40,
				-50,-40,-30,-30,-30,-30,-40,-50]

wKnightPosValue = [-50,-40,-30,-30,-30,-30,-40,-50,
				-40,-20,  0,  5,  5,  0,-20,-40,
				-30,  0, 10, 15, 15, 10,  0,-30,
				-30,  5, 10, 15, 15, 10,  5,-30,
				-30,  0, 15, 20, 20, 15,  0,-30,
				-30,  5, 15, 20, 20, 15,  5,-30,
				-40,-20,  0,  0,  0,  0,-20,-40,
				-50,-40,-30,-30,-30,-30,-40,-50]

bBishopPosValue = [-20,-10,-10,-10,-10,-10,-10,-20,
				-10,  5,  0,  0,  0,  0,  5,-10,
				-10, 10, 10, 10, 10, 10, 10,-10,
				-10,  0, 10, 10, 10, 10,  0,-10,
				-10,  5,  5, 10, 10,  5,  5,-10,
				-10,  0,  5, 10, 10,  5,  0,-10,
				-10,  0,  0,  0,  0,  0,  0,-10,
				-20,-10,-10,-10,-10,-10,-10,-20]

wBishopPosValue = [-20,-10,-10,-10,-10,-10,-10,-20,
				-10,  0,  0,  0,  0,  0,  0,-10,
				-10,  0,  5, 10, 10,  5,  0,-10,
				-10,  5,  5, 10, 10,  5,  5,-10,
				-10,  0, 10, 10, 10, 10,  0,-10,
				-10, 10, 10, 10, 10, 10, 10,-10,
				-10,  5,  0,  0,  0,  0,  5,-10,
				-20,-10,-10,-10,-10,-10,-10,-20]

bRookPosValue = [ 0,  0,  0,  0,  0,  0,  0,  0,
				5, 10, 10, 10, 10, 10, 10,  5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				0,  0,  0,  5,  5,  0,  0,  0]

wRookPosValue = [0,  0,  0,  5,  5,  0,  0,  0,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				-5,  0,  0,  0,  0,  0,  0, -5,
				5, 10, 10, 10, 10, 10, 10,  5,
				0,  0,  0,  0,  0,  0,  0,  0]

bQueenPosValue = [-20,-10,-10, -5, -5,-10,-10,-20,
			-10,  0,  0,  0,  0,  0,  0,-10,
			-10,  0,  5,  5,  5,  5,  0,-10,
			-5,  0,  5,  5,  5,  5,  0, -5,
			0,  0,  5,  5,  5,  5,  0, -5,
			-10,  5,  5,  5,  5,  5,  0,-10,
			-10,  0,  5,  0,  0,  0,  0,-10,
			-20,-10,-10, -5, -5,-10,-10,-20]

wQueenPosValue = [-20,-10,-10, -5, -5,-10,-10,-20,
				-10,  0,  5,  0,  0,  0,  0,-10,
				-10,  5,  5,  5,  5,  5,  0,-10,
				0,  0,  5,  5,  5,  5,  0, -5,
				-5,  0,  5,  5,  5,  5,  0, -5,
				-10,  0,  5,  5,  5,  5,  0,-10,
				-10,  0,  0,  0,  0,  0,  0,-10,
				-10,  0,  0,  0,  0,  0,  0,-10,
				-20,-10,-10, -5, -5,-10,-10,-20]

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
		#print(i,end=" ")
		boardEval += getValue(str(board.piece_at(i))) + posFactor(str(board.piece_at(i)),i)
		#print(board.piece_at(i))
	return boardEval

def posFactor(piece,pos):
	return 0
	if piece == "p":
		return -bPawnPosValue[pos]
	elif piece == "P":
		return wPawnPosValue[pos]
	elif piece == "n":
		return -bKnightPosValue[pos]
	elif piece == "N":
		return wKnightPosValue[pos]
	elif piece == "b":
		return -bBishopPosValue[pos]
	elif piece == "B":
		return wBishopPosValue[pos]
	elif piece == "q":
		return -bQueenPosValue[pos]
	elif piece == "Q":
		return wQueenPosValue[pos]
	else:
		return 0

def getValue(piece): 		#check-out https://www.chessprogramming.org/Simplified_Evaluation_Function
	if piece == None:
		return 0
	elif piece == "p":
		return -100
	elif piece == "P":
		return 100
	elif piece == "n":
		return -320
	elif piece == "N":
		return 320
	elif piece == "b":
		return -330	
	elif piece == "B":
		return -330		
	elif piece == "r":
		return -500
	elif piece == "R":
		return 500
	elif piece == "q":
		return -900
	elif piece == "Q":
		return 900
	elif piece == "k":
		return -20000
	elif piece == "K":
		return 20000
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

#print(evaluate(board))

#print(legal_moves[randMoveIndex])	
print(bestMove)