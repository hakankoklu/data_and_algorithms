from collections import defaultdict


class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if len(words[0]) == 1:
            return [[word] for word in words]
        prefixes = self.get_prefixes(words)
        squares = []
        for word in words:
            self.build(prefixes, [word], squares)
        return squares

    def build(self, prefixes, square, squares):
        if len(square) == len(square[0]) - 1:
            pref = ''.join([word[-1] for word in square])
            if pref in prefixes:
                for word in prefixes[pref]:
                    squares.append(square + [word])
            return
        else:
            pref = ''.join([word[len(square)] for word in square])
            for word in prefixes[pref]:
                self.build(prefixes, square + [word], squares)

    def get_prefixes(self, words):
        pref = defaultdict(list)
        for word in words:
            for i in range(1, len(word)):
                pref[word[:i]].append(word)
        return pref


if __name__ == '__main__':
    s = Solution()
    # words = ["area","lead","wall","lady","ball"]
    words = ["abat", "baba", "atan", "atal"]
    print(s.wordSquares(words))
