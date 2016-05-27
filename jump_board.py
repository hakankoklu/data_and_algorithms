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

board = make_board(100)
print board
print solve_board(board)
