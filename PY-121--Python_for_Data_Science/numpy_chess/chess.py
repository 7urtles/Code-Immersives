from ast import Continue
from matplotlib.pyplot import axis
import numpy as np
'''
layout is a 2d numpy array.
Each value represents a chess piece or empty square
'''


# setting piece values
piece_values = {
    4:Rook,
    2:Knight,
    3:Bishop,
    5:Queen,
    6:King,
    0:Square,
    1:Pawn,
}
size = 8
# create 8x8 board
board = np.empty([size,size], dtype=object)

# place pieces except kings and pawns
for num,piece in enumerate(piece_values.keys()):
    board[0:size:size-1,0+num:size-num] = piece_values(piece)

# place kings
board[0:1, 3], board[7:8, 4] = King

# place pawns
board[1:7:5,:] = Pawn

for piece in np.nditer(board):
    if not piece:
        continue 

    piece_values(np.ndindex(piece))


print(board)
