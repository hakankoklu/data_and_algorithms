"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution(object):
    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        grid = [list(x) for x in grid]
        row_count = len(grid)
        column_count = len(grid[0])
        island_count = 0
        for i in range(row_count):
            for j in range(column_count):
                if grid[i][j] == '1':
                    island_count += 1
                    self.mark_island(grid, i, j)
        return island_count

    def mark_island(self, grid, i, j):
        queue = [(i, j)]
        while queue:
            i, j = queue.pop()
            grid[i][j] = '-1'
            # left
            if j > 0 and grid[i][j - 1] == '1':
                queue.append((i, j - 1))
            # right
            if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
                queue.append((i, j + 1))
            # top
            if i > 0 and grid[i - 1][j] == '1':
                queue.append((i - 1, j))
            # bottom
            if i < len(grid) - 1 and grid[i + 1][j] == '1':
                queue.append((i + 1, j))

grid = [
'01010',
'00111',
'10010',
'01100',
'10101']
print(Solution().num_islands(grid))