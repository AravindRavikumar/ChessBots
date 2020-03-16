import sys
import chess
import random

boardPos = ""

for eachArg in sys.argv[1:]:   
	boardPos = boardPos + eachArg + " "

board = chess.Board(boardPos)
legal_moves = [x for x in board.legal_moves] #check https://github.com/niklasf/python-chess/issues/226

randMoveIndex = random.randint(0,len(legal_moves))

print(legal_moves[randMoveIndex])