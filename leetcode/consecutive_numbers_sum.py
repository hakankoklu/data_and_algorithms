"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9
"""


class Solution:

    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self._consecutive_sum(N)

    def _consecutive_sum(self, num):
        if num <= 2:
            return 1
        run_sum = 1
        low = 1
        high = 1
        ways = 0
        while high <= (num // 2) + 1:
            if run_sum == num:
                ways += 1
                high += 1
                run_sum += high
            elif run_sum < num:
                high += 1
                run_sum += high
            else:
                run_sum -= low
                low += 1
        return ways + 1


if __name__ == '__main__':
    s = Solution()
    tests = [5, 9, 15, 10, 397174, 649869]
    for test in tests:
        print(s.consecutiveNumbersSum(test))
