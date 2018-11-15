"""Write an algorithm to print all ways of arranging 8 queens on an n x n chessboard so that none of them share the
same row, column or diagonal. In this case, “diagonal” means all diagonals, not just the two that bisect the board."""


def nqueens(size):
    board = []
    rr = []
    _nqueen_util(size, board, rr)
    return rr


def _nqueen_util(size, board, result):
    if len(board) == size:
        result.append(board[:])
        return
    for col in range(size):
        if is_safe(board, col):
            board.append(col)
            _nqueen_util(size, board, result)
            board.pop()


def is_safe(board, col):
    row = len(board)
    for ind, b in enumerate(board):
        if b == col:
            return False
        if (row - ind) == (col - b) or (row - ind) == (b - col):
            return False
    return True


if __name__ == '__main__':
    result = nqueens(4)
    print(result)
    print(len(result))
