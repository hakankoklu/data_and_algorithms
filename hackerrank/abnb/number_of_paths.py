"""Same as robot grid, inputs are a bit different. Input is a array of 1,0s:
[1, 1, 1]
[0, 1, 1]
"""

def number_of_paths(a):
    row_no = len(a)
    col_no = len(a[0])
    top_row = [1] * (col_no)
    grid = [top_row]
    for _ in range(row_no - 1):
        new_row = top_row[:]
        grid.append(new_row)
    for i in range(row_no):
        for j in range(col_no):
            if i == j == 0:
                if a[i][j] == 0:
                    return 0
            elif a[i][j] == 0:
                grid[i][j] = 0
            elif i == 0:
                grid[i][j] = grid[i][j - 1]
            elif j == 0:
                grid[i][j] = grid[i - 1][j]
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[-1][-1]


if __name__ == '__main__':
    a1 = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    a2 = [[1,1], [0, 1]]
    a3 = [[1,1,0,1], [1,1,1,1]]
    print(number_of_paths(a1))
    print(number_of_paths(a2))
    print(number_of_paths(a3))