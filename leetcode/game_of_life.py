"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""


class Solution:
    def game_of_life(self, board):
        row = [0] * len(board[0])
        board2 = []
        for _ in board:
            new_row = row[:]
            board2.append(new_row)
        for i in range(len(board)):
            for j in range(len(board[0])):
                value = self.next_value(board, i, j)
                board2[i][j] = value
        for i, row in enumerate(board):
            board[i] = board2[i]

    def game_of_life_inplace(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                value = self.next_value(board, i, j)
                if board[i][j] != value:
                    if board[i][j] == 0:
                        board[i][j] = 2
                    else:
                        board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def next_value(self, board, i, j):
        count = 0
        # left top
        if i > 0 and j > 0:
            count += board[i-1][j-1] % 2
        # top
        if i > 0:
            count += board[i-1][j] % 2
        # right top
        if i > 0 and j < len(board[0]) - 1:
            count += board[i-1][j+1] % 2
        # right
        if j < len(board[0]) - 1:
            count += board[i][j+1] % 2
        # bottom right
        if i < len(board) - 1 and j < len(board[0]) - 1:
            count += board[i+1][j+1] % 2
        # bottom
        if i < len(board) - 1:
            count += board[i+1][j] % 2
        # bottom left
        if i < len(board) - 1 and j > 0:
            count += board[i+1][j-1] % 2
        # left
        if j > 0:
            count += board[i][j-1] % 2

        # under-pop
        if count < 2:
            return 0
        elif count > 3:
            return 0
        elif count == 3:
            return 1
        else:
            return board[i][j]


if __name__ == '__main__':
    inp = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print(inp)
    board2 = Solution().game_of_life(inp)
    print(inp)
    print(board2)