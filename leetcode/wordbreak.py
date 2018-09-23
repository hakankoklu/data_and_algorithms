"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self._word_break(s, wordDict)

    def _word_break(self, s, wordDict, cache={}):
        if not s:
            return True
        for word in wordDict:
            if word == s[:len(word)]:
                result = self._word_break(s[len(word):], wordDict)
            if not result:
                contonue
        return False


if __name__ == "__main__":
    s = [
        # ("leetcode", ["leet", "code"]),
        # ("applepenapple", ["apple", "pen"]),
        # ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("cars", ['car', 'ca', 'rs']),
        ]
    for t in s:
        print(Solution().wordBreak(t[0], t[1]))
