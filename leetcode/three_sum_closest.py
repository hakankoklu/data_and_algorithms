"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._three_sum(nums, target)

    def _three_sum_naive(self, nums, target):
        target_miss = float("inf")
        close_sum = None
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    temp_sum = nums[i] + nums[j] + nums[k]
                    if abs(target - temp_sum) < target_miss:
                        target_miss = abs(target - temp_sum)
                        close_sum = temp_sum
        return close_sum

    def _three_sum(self, nums, target):
        nums.sort()
        abs_miss = float("inf")
        close_sum = None
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                temp_sum = nums[i] + nums[low] + nums[high]
                if abs(temp_sum - target) < abs_miss:
                    abs_miss = abs(temp_sum - target)
                    close_sum = temp_sum
                if temp_sum == target:
                    return target
                elif temp_sum > target:
                    high -= 1
                else:
                    low += 1
        return close_sum


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
