import numpy as np


class Piece:
    def __init__(self, position) -> None:
        self.position = position
        self.possible_moves = []
        pass

    def move(self):
        for move in self.moves.values():
            


class King(Piece):
    def movement(self):
        self.moves = {
            'up':[0,-1],
            'down':[0,1],
            'left':[-1,0],
            'right':[1,0],
        }
        pass

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class Knight(Piece):
    pass

class Rook(Piece):
    pass

class Pawn(Piece):
    pass

class Square(Piece):
    pass