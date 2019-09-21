import numpy as np


class Board:

    def __init__(self, ships):
        self.hits = np.zeros((10,10), np.bool)
        self.dimensions = dimensions
        self.ships = ships

    def update_board(self, new_board):
        self.board = new_board

    def return_board(self):
        return self.board

    def update_board(self, coords):
        self.board[coords[1]][coords[0]] = True

    def print_board_boats(self):
        print('-' * (self.dimensions[0] + 2 ), end='')
        for row in self.board:
            print()
            for item in row:
                if item:
                    print('[' + 'X' + ']', end='')
                else:
                    print('[ ]', end='')

    def print_board_hits(self):


class Ship:
    def __init__(self, length, horizontal):
        self.length = length
        self.destroyed = False
        self.boat = np.zeros(length)
        self.horizontal = horizontal

