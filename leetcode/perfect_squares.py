"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import math


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._num_squares(n)

    def _num_squares(self, n):
        top_root = int(math.sqrt(n))
        sqarr = [x ** 2 for x in range(1, top_root + 1)]
        dynarr = list(range(n + 1))
        dynarr[0] = 0
        for i in range(1, n + 1):
            min_sq = float("inf")
            for sq in sqarr:
                if i >= sq:
                    min_sq = min(min_sq, dynarr[i - sq] + 1)
            dynarr[i] = min_sq
        return dynarr[-1]


if __name__ == '__main__':
    s = Solution()
    tests = [12, 13]
    for test in tests:
        print(s.numSquares(test))
