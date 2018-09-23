"""Imagine a robot sitting on the upper left corner with an X by Y grid.
The robot can only move in two directions: right and down.
How many possible paths are there for the robot to go from (0, 0) to (X, Y)?

FOLLOW UP: Imagine certain spots are "off-limits", such that the robot cannot step on them. Design an algorithm to
find a path for the robot from the top left to the bottom right."""

def robot_move(x, y):
    top_row = [1] * (y + 1)
    grid = [top_row]
    for _ in range(x):
        new_row = top_row[:]
        grid.append(new_row)
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[x][y]


def robot_move_restricted(x, y, off_points):
    top_row = [1] * (y + 1)
    grid = [top_row]
    for _ in range(x):
        new_row = top_row[:]
        grid.append(new_row)
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            if (i, j) == (0, 0):
                continue
            elif (i, j) in off_points:
                grid[i][j] = 0
                continue
            elif i == 0:
                grid[i][j] = grid[i][j - 1]
            elif j == 0:
                grid[i][j] = grid[i - 1][j]
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[x][y]

X, Y = [int(x) for x in input().split()]
# print(robot_move(X, Y))
off_p_count = int(input())
off_ps = []
for _ in range(off_p_count):
    i, j = [int(x) for x in input().split()]
    off_ps.append((i, j))
print(robot_move_restricted(X, Y, off_ps))