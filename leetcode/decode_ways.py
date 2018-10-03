"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:

    DECODE_MAP = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if all([x == '0' for x in s]) or not s:
            return 0
        results = set()
        self.num_decodings(s, results, '')
        return len(results)

    def num_decodings(self, s, results, current=''):
        if not s:
            results.add(current)
        elif len(s) == 1:
            current += self.DECODE_MAP[int(s)]
            self.num_decodings('', results, current)
        elif len(s) == 2 and s[1] == '0' and int(s) < 27:
            self.num_decodings(s[2:], results, current + self.DECODE_MAP[int(s[:2])])
        else:
            self.num_decodings(s[1:], results, current + self.DECODE_MAP[int(s[0])])
            if int(s[:2]) < 27:
                self.num_decodings(s[2:], results, current + self.DECODE_MAP[int(s[:2])])


if __name__ == '__main__':
    ss = [('12', 2),
          ('226', 3),
          ('230', 1)]
    S = Solution()
    for inp, out in ss:
        print(S.numDecodings(inp))
        # assert S.numDecodings(inp) == out
