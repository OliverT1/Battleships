import numpy as np
import random
import time
import pandas as pd


class Board:

    def __init__(self):
        self.defeated = False
        self.ships = [2, 3, 4, 5]
        self.ships_sum = sum(self.ships)
        self.turn = 0
        self.just_hit = False
        self.x = 0
        self.y = 0
        self.win = False
        self.ship_board = np.zeros((10, 10))
        self.generate_board()

    # Generate a random board, uses trial and error to ensure no overlapping ships
    def generate_board(self):
        self.ship_board = np.zeros((10, 10))
        for item in self.ships:
            self.place_ship(item)

    def place_ship(self, item):
        valid = False
        count = 0

        while not valid:
            vertical = random.choice([True, False])
            x = 0
            y = 0

            # Random location ensuring ship all contained on board
            if vertical:
                x = random.randint(0, (10 - item))
                y = random.randint(0, 9)
            else:
                y = random.randint(0, (10 - item))
                x = random.randint(0, 9)

            # Check if ship place is not already taken
            for a in range(item):
                if vertical:
                    if self.ship_board[(x + a)][y] == 1:
                        break
                    elif a == (item - 1):
                        valid = True

                else:
                    if self.ship_board[x][(y + a)] == 1:
                        count += 1
                        break
                    elif a == (item - 1):
                        valid = True

        for a in range(item):

            if vertical:
                self.ship_board[(x + a)][y] = 1

            else:
                self.ship_board[x][(y + a)] = 1

    # Return voard containing with only location of hit ships and hit empties, converts all 1s to 0
    def return_visible_board(self):
        visible_board = np.copy(self.ship_board)
        visible_board[visible_board == 1] = 0
        return visible_board

    # 0 is empty, 1 is ship, 2 is hit ship, 3 is hit empty
    def check_shot(self, coords):

        target = self.ship_board[coords[0]][coords[1]]

        if target == 0:
            self.ship_board[coords[0]][coords[1]] = 3
            self.turn += 1
            self.just_hit = False
            return True

        elif target == 1:
            self.ship_board[coords[0]][coords[1]] = 2
            self.ships_sum -= 1
            self.turn += 1
            self.just_hit = True
            self.x, self.y = coords
            return True

        else:
            return False


def turn(board):

    valid = False
    tries = 0

    while not valid:

        if board.just_hit and tries < 10:
            x = board.x + random.choice([-1, 1])
            y = board.y + random.choice([-1, 1])
            tries += 1

        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        if x == 10:
            x = 9
        if x == -1:
            x = 0
        if y == 10:
            y = 9
        if y == -1:
            y = 0
        if board.check_shot((x, y)):

            valid = True

    if board.ships_sum == 0:

        return board.turn
    else:
        return turn(board)




start_time = time.time()
turns_taken =[]
for x in range(10000):
    new_board = Board()
    turns_taken.append(turn(new_board))
    del new_board
print((time.time()-start_time))

np_turns = np.array(turns_taken)

print('Mean is ', np_turns.mean())
print('STD is ', np_turns.std())
