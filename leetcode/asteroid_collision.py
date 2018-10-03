"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000].
"""


class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        return self._asteroid_collusion(asteroids)

    def _asteroid_collusion(self, arr):
        if len(arr) <= 1:
            return arr
        change = True
        while change:
            change = False
            result = [arr[0]]
            popped = False
            for ind, ast in enumerate(arr[1:], 1):
                if popped:
                    popped = False
                    continue
                current = result[-1]
                if not self.is_collusion(current, ast):
                    result.append(ast)
                else:
                    col_res = self.collide(current, ast)
                    if col_res:
                        change = True
                        result[-1] = col_res
                    else:
                        result.pop()
                        popped = True
                        if ind + 1 < len(arr):
                            result.append(arr[ind + 1])
            arr = result[:]
        return arr

    def is_collusion(self, one, two):
        if one > 0 and two < 0:
            return True
        return False

    def collide(self, one, two):
        diff = one + two
        if diff > 0:
            return one
        elif diff < 0:
            return two
        return None


if __name__ == '__main__':
    s = Solution()
    tests = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [-2, -1, 1, 2],
        [2, -1, -2, -2]
    ]
    for test in tests:
        print(s.asteroidCollision(test))
