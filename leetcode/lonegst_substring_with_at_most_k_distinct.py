from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self._solve(s, k)

    def _solve(self, s, k):
        if not s or not k:
            return 0
        dist_count = 1
        char_count = defaultdict(int)
        char_count[s[0]] = 1
        start_ind = 0
        end_ind = 0
        max_len = 1
        while end_ind < len(s) - 1:
            if dist_count <= k:
                end_ind += 1
                char_count[s[end_ind]] += 1
                dist_count = len(char_count)
                if dist_count <= k:
                    max_len = max(max_len, end_ind - start_ind + 1)
            else:
                start_ind += 1
                char_count[s[start_ind - 1]] -= 1
                if char_count[s[start_ind - 1]] == 0:
                    char_count.pop(s[start_ind - 1])
                dist_count = len(char_count)
        return max_len


if __name__ == '__main__':
    s = Solution()
    tests = [
        ('eceba', 2),
        ('aa', 1),
        ('ababaabcd', 2)
    ]
    for st, k in tests:
        print(s.lengthOfLongestSubstringKDistinct(st, k))

