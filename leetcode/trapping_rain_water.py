"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it is able to trap after raining.

https://leetcode.com/problems/trapping-rain-water/description/
"""


class Solution:

    def trap(self, height):
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        current_max = 0
        for ind in range(1, len(height)):
            current_max = max(current_max, height[ind - 1])
            left_max[ind] = current_max
        current_max = 0
        for ind in range(len(height) - 2, -1, -1):
            current_max = max(current_max, height[ind + 1])
            right_max[ind] = current_max
        water = 0
        for ind in range(len(height)):
            water += max(0, min(left_max[ind], right_max[ind]) - height[ind])
        return water


if __name__ == '__main__':
    h = [2,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(h))