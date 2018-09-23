"""Write an algorithm to print all ways of arranging 8 queens on an n x n chessboard so that none of them share the
same row, column or diagonal. In this case, “diagonal” means all diagonals, not just the two that bisect the board."""

MAPS = []


def n_queens(size, board=[]):
    if len(board) >= size:
        MAPS.append(board)
        return True
    good = False
    for col in range(size):
        if is_safe(board, col):
            board.append(col)
            good = n_queens(size, board) or good
            if not good:
                board.pop()
    return good


def is_safe(board, col):
    row = len(board)
    for ind, b in enumerate(board):
        if b == col:
            return False
        if (row - ind) == (col - b) or (row - ind) == (b - col):
            return False
    return True


if __name__ == '__main__':
    n_queens(4)
    print(MAPS)
