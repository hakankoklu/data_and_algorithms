# You're given a board game which is a row of squares, each labeled with an integer.
# This can be represented by a list, e.g.
# [1, 3, 2, 0, 5, 2, 8, 4, 1]
#
# Given a start position on the board, you "win" by landing on a zero, where you move
# by jumping from square to square either left or right the number of spaces specified
# on the square you're currently on.
#
# Your task is to implement the function:
#
# def can_win(board, pos): returns True if you can win the board from that starting pos, False otherwise

from random import randint

def make_board(board_size):
    board = []
    for i in xrange(board_size):
        board.append(randint(0, 10))
    return board

def solve_board(board):
    spare_squares = set()
    new_square = True
    while new_square:
        new_square = False
        for ind, jump in enumerate(board):
            if ind in spare_squares:
                continue
            first_jump = (ind - jump) % len(board)
            second_jump = (ind + jump) % len(board)
            if first_jump in spare_squares or second_jump in spare_squares \
                or board[first_jump] == 0 or board[second_jump] == 0:
                spare_squares.add(ind)
                new_square = True
        #print spare_squares
    return spare_squares

def can_win(board, pos):
    winners = solve_board(board)
    return pos in winners

board = make_board(30)
print board
print solve_board(board)
print can_win(board, 12)
