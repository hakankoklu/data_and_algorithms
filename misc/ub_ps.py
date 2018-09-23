"""

W    W    G    0    0
0    0    0    W    W
0    0    0    0    0
W    0    0    W    0
G    0    W    0    0

W = Wall
G = Guard
0 = Free space

replace 0 with min. number of steps to closest guard

up/down/left/right

W    W    G    1    2
3    2    1    W    W
4    3    2    3    4
W    2    3    W    5
G    1    W    0    0

W    W    G    1    2
0    2    1    W    W
0    3    2    3    4
W    2    3    W    5
G    1    W    0    6



"""

"""
W    W    G    1    2
3    2    1    W    W
4    3    2    3    4
W    2    3    W    5
G    1    W    7    6
"""

maze = [['W', 'W', 'G', '0', '0'], ['0', '0', '0', 'W', 'W'], ['0', '0', '0', '0', '0'], ['W', '0', '0', 'W', '0'],
        ['G', '0', 'W', '0', '0']]


def solution(maze):
    not_done = True
    count = 0
    while not_done:
        not_done = False
        for row in range(len(maze)):
            for j in range(len(maze[row])):
                update_min(maze, row, j)
                not_done = not_done or maze[row][j] == '0'
                # should have been not_done = not_done or maze[row][j] != temp
        # print(maze)
        # count += 1
        # if count > 5:
        #     break
    return maze


def update_min(maze, row, col):
    result = 99999
    if maze[row][col] not in ['G', 'W']:
        # up
        if row > 0:
            if maze[row - 1][col] == 'G':
                result = 1
            elif maze[row - 1][col] not in ['W', '0']:
                temp = int(maze[row - 1][col]) + 1
                if int(maze[row][col]) == 0:
                    result = temp
                else:
                    result = min(int(maze[row][col]), temp)
                    # should have been result = min(int(maze[row][col]), temp, result)
        # down
        if row < len(maze) - 1:
            if maze[row + 1][col] == 'G':
                result = 1
            elif maze[row + 1][col] not in ['W', '0']:
                temp = int(maze[row + 1][col]) + 1
                if int(maze[row][col]) == 0:
                    result = temp
                else:
                    result = min(int(maze[row][col]), temp)
                    # should have been result = min(int(maze[row][col]), temp, result)
        # left
        if col > 0:
            if maze[row][col - 1] == 'G':
                result = 1
            elif maze[row][col - 1] not in ['W', '0']:
                temp = int(maze[row][col - 1]) + 1
                if int(maze[row][col]) == 0:
                    result = temp
                else:
                    result = min(int(maze[row][col]), temp)
                    # should have been result = min(int(maze[row][col]), temp, result)
        # right
        if col < len(maze[row]) - 1:
            if maze[row][col + 1] == 'G':
                result = 1
            elif maze[row][col + 1] not in ['W', '0']:
                temp = int(maze[row][col + 1]) + 1
                if int(maze[row][col]) == 0:
                    result = temp
                else:
                    result = min(int(maze[row][col]), temp)
                    # should have been result = min(int(maze[row][col]), temp, result)
        if result != 99999:
            maze[row][col] = str(result)


print(solution(maze))