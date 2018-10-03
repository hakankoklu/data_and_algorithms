"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = []
        candidates.sort()
        self._combination_sum(candidates, target, l)
        return l

    def _combination_sum(self, candidates, target, l, current=[]):
        for candidate in candidates:
            if target - candidate == 0:
                current = current + [candidate]
                l.append(current)
            elif target - candidate > 0:
                current = current + [candidate]
                target -= candidate
                self._combination_sum(candidates, target, l, current)
            else:
                popped = current.pop()
                target
                break


if __name__ == '__main__':
    s = Solution()
    arr = [2, 3, 6, 7]
    t = 7
    l = s.combinationSum(arr, t)
    print(l)