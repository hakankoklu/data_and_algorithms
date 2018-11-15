"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

0, 10
3, 9
5, 12
"""
from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter_set = set(t)
        num_let = len(letter_set)
        found_set = set()
        tmap = {x: None for x in letter_set}
        min_max = None
        for ind, letter in enumerate(s):
            if letter in letter_set:
                found_set.add(letter)
                tmap[letter] = ind
            if len(found_set) == num_let:
                min_ind = min(tmap.values())
                max_ind = max(tmap.values())
                if min_max is None:
                    min_max = (min_ind, max_ind)
                else:
                    if (max_ind - min_ind) < (min_max[1] - min_max[0]):
                        min_max = (min_ind, max_ind)
        if not min_max:
            return ''
        return s[min_max[0]:min_max[1] + 1]

    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter_count = defaultdict(int)
        letter_set = set(t)
        for letter in t:
            letter_count[letter] += 1
        left = right = 0
        if s[0] in letter_set:
            letter_count[s[0]] -= 1
        min_win = s
        current_window = s[0]
        found = False
        while right < len(s):
            if self.check_found(letter_count):
                found = True
                if len(current_window) < len(min_win):
                    min_win = current_window
                if s[left] in letter_set:
                    letter_count[s[left]] += 1
                left += 1
                current_window = current_window[1:]
            else:
                right += 1
                if right < len(s):
                    if s[right] in letter_set:
                        letter_count[s[right]] -= 1
                    current_window = current_window + s[right]
        if found:
            return min_win
        else:
            return ""

    def check_found(self, d):
        return all([value <= 0 for value in d.values()])


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow2("A", "AA"))
