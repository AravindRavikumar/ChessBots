#check https://www.chessprogramming.org/Simplified_Evaluation_Function for position values

bPawnPosValue = [0,  0,  0,  0,  0,  0,  0,  0,
				50, 50, 50, 50, 50, 50, 50, 50,
				10, 10, 20, 30, 30, 20, 10, 10,
				5,  5, 10, 25, 25, 10,  5,  5,
				0,  0,  0, 20, 20,  0,  0,  0,
				5, -5,-15, -10,-10,-15, -5,  5,
				5, 10, 10,-20,-20, 10, 10,  5,
				0,  0,  0,  0,  0,  0,  0,  0]

wPawnPosValue = [0,  0,  0,  0,  0,  0,  0,  0,
				5, 10, 10,-20,-20, 10, 10,  5,
				5, -5,-15,-10,-10,-15, -5,  5,
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
				0,  0,  10,  20,  20, 10,  0,  0]

wRookPosValue = [0,  0,  10, 20,  20, 10,  0,  0,
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

bKingPosValue = [-30,-40,-40,-50,-50,-40,-40,-30,
				-30,-40,-40,-50,-50,-40,-40,-30,
				-30,-40,-40,-50,-50,-40,-40,-30,
				-30,-40,-40,-50,-50,-40,-40,-30,
				-20,-30,-30,-40,-40,-30,-30,-20,
				-10,-20,-20,-20,-20,-20,-20,-10,
				20, 20,  0,  0,  0,  0, 20, 20,
				20, 30, 10,  0,  0, 10, 30, 20]

wKingPosValue = [20, 30, 10,  0,  0, 10, 30, 20,
				20, 20,  0,  0,  0,  0, 20, 20,
				-10,-20,-20,-20,-20,-20,-20,-10,
				-20,-30,-30,-40,-40,-30,-30,-20,
				-30,-40,-40,-50,-50,-40,-40,-30,
				-30,-40,-40,-50,-50,-40,-40,-30,
				-30,-40,-40,-50,-50,-40,-40,-30,
				-30,-40,-40,-50,-50,-40,-40,-30]

def posFactor(piece,pos):
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
	elif piece == "r":
		return -bRookPosValue[pos]
	elif piece == "R":
		return wRookPosValue[pos]
	elif piece == "q":
		return -bQueenPosValue[pos]
	elif piece == "Q":
		return wQueenPosValue[pos]
	else:
		return 0
